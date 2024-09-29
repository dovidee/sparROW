import pandas as pd
import numpy as np
exc1 = pd.read_excel("oppgave2.xlsx") 
exc2 = pd.read_excel("oppgave2_rounded.xlsx") # Bruk denne 

def highest(exc): # A
    fixed = exc.replace(0, np.nan) # Fjern null
    highest_column = fixed.sort_values(['Y2023'], ascending=False) # Sorter
    # Ta første navn og første rad av Sted og 2023
    print(f"Høyeste gjennomsnitt i 2023 er {highest_column['Sted'].iloc[0]} med {round(highest_column['Y2023'].iloc[0])} prosent") 

def lowest(exc): # B
    fixed = exc.replace(0, np.nan) # Fjern null
    lowest_column = fixed.sort_values(['Y2023'], ascending=True) # Sorter
    # Ta første navn og første rad av Sted og 2023
    print(f"Laveste gjennomsnitt i 2023 er{lowest_column['Sted'].iloc[0]} med {round(lowest_column['Y2023'].iloc[0])} prosent")
    # Bruk print(lowest_column.head(10)) for å se duplikater

def meanest(exc): # C
    fixed = exc.replace(0, np.nan) # Fjern null
    fixed['mean'] = fixed.iloc[:, 1:].mean(axis=1) # Legg til en ny kolonne med mean
    highest_column = fixed.sort_values(['mean'], ascending=False)
    lowest_column = fixed.sort_values(['mean'], ascending=True)
    print(f"Høyeste gjennomsnittlige prosenten er {highest_column['Sted'].iloc[0]} med {round(highest_column['mean'].iloc[0])} prosent")
    print(f"Laveste gjennomsnittlige prosenten er{lowest_column['Sted'].iloc[0]}med {round(lowest_column['mean'].iloc[0])} prosent")

def highest_lowest_OVR(exc): # D og E
    fixed = exc.replace(0, np.nan) # Fjern null
    fixed['highest'] = fixed.iloc[:, 1:].max(axis=1) # Legg til en ny kolonne med høyest
    fixed['lowest'] = fixed.iloc[:, 1:].min(axis=1) # Legg til en ny kolonne med lavest
    highest_column = fixed.sort_values(['highest'], ascending=False)
    lowest_column = fixed.sort_values(['lowest'], ascending=True)
    # Ta første navn og første rad av high/low raden
    print(f"Høyeste gjennomsnittlige prosent er {highest_column['Sted'].iloc[0]} med {round(highest_column['highest'].iloc[0])} prosent")
    print(f"Laveste gjennomsnittlige prosent er{lowest_column['Sted'].iloc[0]} med {round(lowest_column['lowest'].iloc[0])}")

def meanest_OVR(exc): # F
    fixed = exc.replace(0, np.nan) # Fjern null
    fixed['mean'] = fixed.iloc[:, 1:].mean(axis=1) # Legg til en ny kolonne med mean
    print("Gjennomsnittlig prosent for alle kommuner mellom 2015 og 2023:" + "\n" f"{fixed}") # Vis all data
    
highest(exc2)
lowest(exc2)
meanest(exc2)
highest_lowest_OVR(exc2)
meanest_OVR(exc2)
