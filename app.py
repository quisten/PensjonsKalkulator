#########################################################################################
# Pensjonskalkuator en studie i UX Design
#  
# Pensjon avhenger i hovedsak av 3 ulike ordninger som bindes opp mot relative like 
# instrumenter men skattes noe ulikt. Det er ikke alltid like lett å vite hva som er 
# den beste strategien, særlig med et vekslende politisk klima som utsetter ordningene 
# for symbolpolitikk av verste sort. 
#
# Her er et verktøy for å studere dette, og samtidig gi forfatter en ypperlig sjanse for
# å prøve seg på noe mer krevende UX design. 
#
#########################################################################################

import streamlit as st
import matplotlib.pyplot as plt

#########################################################################################
# Constants  
#########################################################################################

Konstanter_2021 = {'1G': 106399,                       # NOK
              'Max_Pensjonsgivende_Inntekt': 7.1, # in G
              'Pensjonsprosent': 18.1,            # in prosent
              'Trygdeavgift': 5.2,                # in prosent
              'Grense_Formueskatt': 1.5e6,        # NOK
              'Formueskatt': 0.85,                # Prosent
              'Skatt_Gevinst_ASK': 31.68,         # Prosent
              'Skatt_IPS_Saldo': 22.0,            # Prosent  
              'Skatt_Utsatt_IPS': 22.0,           # Prosent
              'Inflasjon:': 2,                    # Prosent
}
Konstanter = Konstanter_2021

Profil_Norm = {'Brutto_Lonn': 600000, 
               'EstLonnsOkning': 2.0, 
               'PensjonsBeholdning': 1.5e6,
               'Alder': 40,
               }
Profil = Profil_Norm



#########################################################################################
# Functions  
#########################################################################################


#########################################################################################
# Main 
#########################################################################################


def main(): 
    
    with st.sidebar:
        st.write("This lives in the sidebar.")
    

        with st.expander("Profil", expanded=False):
            st.text_input("Nåværende Alder:", value=Profil['Alder'])
            st.text_input("Bruttolønn:", value=Profil['Brutto Lønn'], help="Lønn før skatt")
            st.text_input("Forventet lønnsvekst iforhold til Inflasjon:", value=Profil['Brutto Lønn'], help="Lønn før skatt")
            
        st.slider("Forventet Penjonsalder", min_value=62, max_value=75, value=65)
    
        
        with st.expander("Konstanter", expanded=False):
            
            st.number_input("InflasjonsRate (%)", value=2.0, format="%.2f")
            st.number_input("Forventet Lønnsvekst (%)", value=2.0, format="%.2f")
            
            
            st.write("Skatte Tabell")


    
    # Input for de ulike løsningene 

    with st.expander("Input for PensjonssparingsStrategi", expanded=True):    
        col1, col2, col3 = st.columns(3)

        with col1: 
            st.write("Alderspensjon")
        with col2:
            st.write("Arbeidsgiverskatt")
        with col3:
            st.write("IPS")

    # Output 

    with st.expander("Mellomberegninger", expanded=True):   
        col4, col5, col6, col7 = st.columns(4)
    
        with col4:
            st.write("Trinnskatt Beregning og Vederlag")
        with col5:
            st.write("Alderspensjon")
        with col6:
            st.write("Arbeidspensjon")
        with col7:
            st.write("IPS")

    st.write("Version 0.0 alpha")
    return True


#########################################################################################
# Init 
#########################################################################################
if __name__ == "__main__":
    st.set_page_config(
        "Pensjonskalkulator",
        "📊",
        initial_sidebar_state="expanded",
        layout="wide",
    )
    main()
