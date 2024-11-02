import pandas as pd
import numpy as np
exc1 = pd.read_excel("oppgave2.xlsx") 
exc2 = pd.read_excel("oppgave2_rounded.xlsx") # Bruk denne 

def highest(exc : dict) -> str: # A
    fixed = exc[(exc != 0).all(1)]
    highest_column = fixed.sort_values(['Y2023'], ascending=False) # Sorter høy
    # Ta første navn og første rad av Sted og 2023
    print(f"Høyeste prosenten i 2023 er {highest_column['Sted'].iloc[0]} med {round(highest_column['Y2023'].iloc[0])} prosent") 

def lowest(exc : dict) -> str: # B
    fixed = exc[(exc != 0).all(1)]
    lowest_column = fixed.sort_values(['Y2023'], ascending=True) # Sorter lav
    # Ta første navn og første rad av Sted og 2023
    print(f"Laveste prosenten i 2023 er{lowest_column['Sted'].iloc[0]} med {round(lowest_column['Y2023'].iloc[0])} prosent")
    # Bruk print(lowest_column.head(10)) for å se duplikater

# C gir ingen mening siden det er en duplikat av E men riktig ordbruk er "prosenten" i både D og E. 
# Høyste eller høyeste?

def meanest(exc : dict) -> str: # D og E
    fixed = exc[(exc != 0).all(1)]
    fixed['mean'] = fixed.iloc[:, 1:].mean(axis=1) # Legg til en ny kolonne med mean
    highest_column = fixed.sort_values(['mean'], ascending=False) # Sorter høy mean
    lowest_column = fixed.sort_values(['mean'], ascending=True) # Sorter lav mean
    print(f"Høyeste gjennomsnittlige prosenten er {highest_column['Sted'].iloc[0]} med {round(highest_column['mean'].iloc[0])} prosent")
    print(f"Laveste gjennomsnittlige prosenten er {lowest_column['Sted'].iloc[0]}med {round(lowest_column['mean'].iloc[0])} prosent")

def meanest_OVR(exc : dict, year : str) -> str: # F
    result = round(exc[year].mean())
    print(f"Gjennomsnittlig prosent for {year} er {result}")
    
highest(exc2)
lowest(exc2)
meanest(exc2)
meanest_OVR(exc2, 'Y2023')
