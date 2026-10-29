"""Tag 4 – lokale Demo. Alle Daten fiktiv. Start: uv run streamlit run app.py"""
from pathlib import Path
from datetime import date, timedelta
import pandas as pd
import numpy as np
import streamlit as st

st.set_page_config(page_title='Tag 4 | KI und Daten', page_icon='📊', layout='wide')
DATA = Path(__file__).resolve().parent.parent / 'materialien'

def read_csv(name):
    return pd.read_csv(DATA / name, sep=';', encoding='utf-8-sig')

@st.cache_data
def training_data():
    return read_csv('01_schulungsdaten.csv')

@st.cache_data
def planning_data():
    return read_csv('04_materialstamm.csv'), read_csv('05_lagerbestand.csv'), read_csv('06_projektplanung.csv')

@st.cache_data
def historical_data():
    return read_csv('07_historischer_verbrauch.csv')


def simulate(materials, stock, projects, shift_gamma=0):
    """Educational greedy FEFO-like scheduling under explicit simplifying assumptions.

    Demand is consumed at the *start date*. Packs opened on that day may be used
    through opening_date + usable_days - 1 inclusive. Stock packs can be opened
    only if their unopened expiry is >= date. New purchases are assumed available
    exactly when required (the order-by date is an arithmetic indicator).
    """
    pending=[]
    for _,r in projects.iterrows():
        d=date.fromisoformat(str(r.startdatum)[:10])
        if str(r.projekt)=='Gamma': d += timedelta(days=shift_gamma)
        pending.append((d,str(r.material_id),str(r.projekt),int(r.bedarf_tests_am_starttag)))
    pending.sort()
    result=[]
    for _,material in materials.iterrows():
        mid=str(material.material_id); capacity=int(material.kapazitaet_tests_pro_packung)
        usable=int(material.nutzungsdauer_ab_oeffnung_tage); lead=int(material.lieferzeit_kalendertage)
        inv=stock.loc[stock.material_id.eq(mid)]
        unopened=[]
        for _,s in inv.iterrows():
            unopened.extend([date.fromisoformat(str(s.verfallsdatum_ungeoeffnet)[:10])]*int(s.packungen_ungeoeffnet))
        unopened.sort()
        openpacks=[]
        for d,m,project,amount in pending:
            if m != mid: continue
            initial=amount; orders=0; discarded=0
            remaining=[]
            for p in openpacks:
                if d > p['valid_until']:
                    discarded += p['remaining']
                else:
                    remaining.append(p)
            openpacks=remaining
            while amount>0:
                valid=[p for p in openpacks if p['remaining']>0]
                if valid:
                    p=min(valid,key=lambda v:v['valid_until'])
                else:
                    valid_stock_idx=next((i for i,e in enumerate(unopened) if e>=d),None)
                    if valid_stock_idx is not None:
                        unopened.pop(valid_stock_idx)
                    else:
                        orders+=1
                    p={'valid_until':d+timedelta(days=usable-1),'remaining':capacity}
                    openpacks.append(p)
                take=min(amount,p['remaining']);p['remaining']-=take;amount-=take
            result.append({'Projekt':project,'Datum':d.isoformat(),'Material':mid,'Bedarf (Tests)':initial,
                           'Neu benötigte Packungen':orders,'Bestellen spätestens':(d-timedelta(days=lead)).isoformat() if orders else '–',
                           'Bis dahin verfallene Resttests':discarded})
    return pd.DataFrame(result).sort_values(['Datum','Material']).reset_index(drop=True)

st.title('Tag 4 · Daten verstehen und Entscheidungen vorbereiten')
st.caption('Lokales Unterrichtsdashboard · ausschließlich fiktive Daten · kein Upload an einen KI-Dienst')
tab1,tab2,tab3 = st.tabs(['📋 Schulungsauswertung','📦 Materialplanung','📈 Prognose-Demo'])

with tab1:
    st.subheader('Schulungsfeedback analysieren')
    df=training_data()
    topics=sorted(df['thema'].dropna().unique())
    selected=st.multiselect('Schulungsthemen',topics,default=topics)
    f=df[df.thema.isin(selected)].copy()
    m1,m2,m3=st.columns(3)
    m1.metric('Datensätze (Zeilen)',len(f))
    m2.metric('Eindeutige Antwort-IDs',f.antwort_id.nunique())
    m3.metric('Ø Zufriedenheit (vor Bereinigung)',f.zufriedenheit_1_bis_5.mean().round(2) if len(f) else '–')
    st.info('Achtung: Die Datei enthält absichtlich einen doppelten Datensatz, fehlende Werte und unterschiedliche Schreibweisen. Ein Workshoppreis ist je Workshop hinterlegt und darf NICHT pro Antwortzeile summiert werden.')
    if not f.empty:
        st.bar_chart(f.groupby('thema',as_index=False)['zufriedenheit_1_bis_5'].mean(),x='thema',y='zufriedenheit_1_bis_5')
    st.dataframe(f,hide_index=True)
    st.download_button('Gefilterte Daten als CSV herunterladen',f.to_csv(index=False,sep=';').encode('utf-8-sig'),'schulungsdaten_gefiltert.csv',mime='text/csv')
    with st.expander('Qualitätskontrolle'):
        st.write('Doppelte Antwort-IDs:',int(f.antwort_id.duplicated().sum()))
        st.write('Fehlende Zufriedenheitsangaben:',int(f.zufriedenheit_1_bis_5.isna().sum()))
        st.write('Verschiedene Schreibweisen im Themenfeld werden nicht automatisch zusammengeführt.')

with tab2:
    st.subheader('Projektmaterial: Haltbarkeit nach Öffnung')
    st.caption('Annahmen: Verbrauch jeweils am Projektstart; Öffnungstag zählt als Tag 1; vorhandene unangebrochene Packungen werden verwendet, sofern ihr Verfallsdatum noch nicht überschritten ist. Beschaffung wird nur rechnerisch berücksichtigt.')
    master,stock,projects=planning_data()
    shift=st.slider('Projekt Gamma verschieben (Tage)',-5,14,0,1)
    scenario=simulate(master,stock,projects,shift)
    c1,c2,c3=st.columns(3)
    c1.metric('Geplante Verbrauchsvorgänge',len(scenario))
    c2.metric('Zusätzlich benötigte Packungen',int(scenario['Neu benötigte Packungen'].sum()))
    c3.metric('Verworfene Resttests bis zum jeweils nächsten Bedarf',int(scenario['Bis dahin verfallene Resttests'].sum()))
    st.dataframe(scenario,hide_index=True)
    st.download_button('Planung als CSV herunterladen',scenario.to_csv(index=False,sep=';').encode('utf-8-sig'),'material_planung.csv',mime='text/csv')
    st.warning('Nur ein Lehrmodell: keine Reservierungen, Bestellmengen, Feiertage, Lieferunsicherheit, Chargenfreigaben, Kosten oder Nachverfolgung tatsächlicher Bestellungen. Die Bestellfrist ist ohne Sicherheitspuffer gerechnet.')
    with st.expander('Rohdaten prüfen'):
        st.write('Materialstamm');st.dataframe(master,hide_index=True)
        st.write('Lagerbestand');st.dataframe(stock,hide_index=True)
        st.write('Projektbedarf');st.dataframe(projects,hide_index=True)

with tab3:
    st.subheader('Historischer Verbrauch und einfache Prognose')
    st.caption('Fiktive Monatswerte. Zum Vergleich: Durchschnitt der letzten drei Monate versus linearer Trend. Keine automatische Bestellentscheidung.')
    hist=historical_data().sort_values('monat').reset_index(drop=True)
    train=hist.iloc[:-6].copy(); test=hist.iloc[-6:].copy()
    actual=test.verbrauch_tests.astype(float).to_numpy()
    # simple walk-forward three-month average on known historic values
    all_values=hist.verbrauch_tests.astype(float).to_numpy()
    preds=[]
    for i in range(len(train),len(hist)):
        preds.append(float(all_values[i-3:i].mean()))
    mae=sum(abs(float(a)-float(p)) for a,p in zip(actual,preds))/len(preds)
    # Trained supervised linear regression (OLS), trained only on older months.
    # At inference we only use features assumed known in advance: month index
    # and calendar-month seasonality; no future actual demand or project count.
    def design(frame, offset):
        idx=np.arange(offset,offset+len(frame),dtype=float)
        month=pd.to_datetime(frame['monat'],format='%Y-%m').dt.month.to_numpy(dtype=float)
        return np.column_stack([np.ones(len(frame)),idx,np.sin(2*np.pi*month/12),np.cos(2*np.pi*month/12)])
    x_train=design(train,0); x_test=design(test,len(train))
    weights=np.linalg.lstsq(x_train,train.verbrauch_tests.astype(float).to_numpy(),rcond=None)[0]
    ml_preds=x_test@weights
    ml_mae=float(np.mean(np.abs(actual-ml_preds)))
    c1,c2,c3=st.columns(3)
    c1.metric('Testzeitraum',f'{len(test)} Monate')
    c2.metric('MAE · 3-Monats-Mittel',f'{mae:.1f} Tests')
    c3.metric('MAE · trainierte Regression',f'{ml_mae:.1f} Tests')
    chart=hist[['monat','verbrauch_tests']].copy().rename(columns={'verbrauch_tests':'Tatsächlich'})
    st.line_chart(chart,x='monat',y='Tatsächlich')
    compare=test[['monat','verbrauch_tests']].copy().rename(columns={'verbrauch_tests':'Tatsächlich'})
    compare['Prognose (rollierender Mittelwert)']=[round(p,1) for p in preds]
    compare['Prognose (trainierte Regression)']=[round(float(p),1) for p in ml_preds]
    st.dataframe(compare,hide_index=True)
    st.info('Die Regression ist tatsächlich auf den ersten 30 Monaten trainiert; die letzten 6 Monate dienen ausschließlich dem Test. Ein einmalig gut abschneidendes Modell ist noch kein verlässliches betriebliches Prognosesystem. Die Daten sind fiktiv.')
