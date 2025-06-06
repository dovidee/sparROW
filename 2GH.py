import altair as alt
import pandas as pd
import numpy as np
from functools import reduce

exc1 = pd.read_excel("oppgave2.xlsx")
exc2 = pd.read_excel("oppgave2_rounded.xlsx") # Bruk denne

def kommune_pie(kommune : str, exc : dict) -> None:
    matched = exc['Sted'].str.fullmatch(kommune)
    chosen = exc.loc[matched[matched].index] # Boolean indexing til å finne kommune index (wtf?)
    to_flatten = chosen.values.tolist() # Velg tallene
    reduced_row = reduce(lambda x,y: x+y, to_flatten) # Fjern listen ut av listen med flatten
    reduced_row.pop(0) # Fjern kommunen
    reduced_col = chosen.columns.difference(['Sted'])
    data = {"År":reduced_col, "perc":reduced_row} # Samle årene og tallene i data
    exc = pd.DataFrame(data) # Lag en dataframe ut av data
    base = alt.Chart(exc).mark_arc().encode( # Skap en chart
        theta=alt.Theta("perc", stack=True),
        color=alt.Color("År")
    )
    pie = base.mark_arc(outerRadius=100) # Lag en radius utenfor
    text = base.mark_text(
            radius=100, 
            size=10,
        ).encode( 
            text=alt.Text("perc"), # Prosent format
            color=alt.value("#605E5C"),
            tooltip=alt.Text("År"),
        )
    device_chart = alt.layer(pie, text) # Legg til teksten i radiusen utenfor
    device_chart.save(f"{kommune}.html") # Lagre chart i html

def kommune_top10(exc : dict) -> None:
    fixed = exc[(exc != 0).all(1)] # FJERN NULL FOR REAL
    fixed['mean'] = fixed.iloc[:, 1:].mean(axis=1) # Lag ny rad med gjennomsnitt
    highest_column = fixed.sort_values(['mean'], ascending=False) # Sorter rad etter høyeste
    top_10 = highest_column.head(11) # Top 10 Communities Of All Time
    top_10_places = []
    top_10_mean = []
    for places in top_10['Sted']:
        top_10_places.append(places) # Legg i ny liste
    for means in top_10['mean']:
        top_10_mean.append(round(means)) # Legg i ny liste
    data = {"Kommune":top_10_places, "Gjennomsnitt":top_10_mean} # Samle årene og tallene i data
    exc = pd.DataFrame(data) # Lag en dataframe ut av data
    base = alt.Chart(exc).mark_arc().encode( # Skap en chart
        theta=alt.Theta("Gjennomsnitt", stack=True),
        color=alt.Color("Kommune")
    )
    pie = base.mark_arc(outerRadius=100) # Lag en radius utenfor
    text = base.mark_text(
            radius=100, 
            size=10,
        ).encode( 
            text=alt.Text("Gjennomsnitt"), # Prosent format
            color=alt.value("#605E5C"),
            tooltip=alt.Text("Kommune"),
        )
    device_chart = alt.layer(pie, text) # Legg til teksten i radiusen utenfor
    device_chart.save(f"top10.html") # Lagre chart i html

# ignorer SettingWithCopyWarning, bare bruk 1 funksjon om gangen
kommune_pie("Kristiansand", exc2)
kommune_top10(exc2)
