#########################################################################################
#
# Del 1 i Pensjonsprosjetet
# Finne egnede strukturerer for å elegant regne ut og presentere trinnskatten 
# 
#########################################################################################

import math
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

#########################################################################################
# Constants  
#########################################################################################

taxBase = 22.0
taxWelfare = 8.2
personFradrag = 58250
taxProgressiveTable_2022 = [[1.7,  190350, 267899], 
                            [4.0,  267900, 643799],
                            [13.4, 643800, 969199],
                            [16.4, 969200, 1999999],
                            [17.4, 2000000, math.inf]]


#########################################################################################
# Functions  
#########################################################################################

def getTaxTable(grossSalary, table):

    taxSteps = list() 
    taxComputation = list()                             # for modification by adding taxes per row
    baseTax = grossSalary*((taxBase+taxWelfare)/100.0)

    #st.write("Trinn 0:", baseTax)
    for step, row in enumerate(table):
        tax_step = max(0, min(grossSalary, row[2])-row[1])*(row[0]/100.0)
        if tax_step == 0:
            break
        taxSteps.append(tax_step)
        taxComputation.append(["%.2f" % row[0], f'{row[1]:,}', f'{row[2]:,}', f'{int(tax_step):,}'])
    
    totalTax = baseTax + sum(taxSteps)
    netSalary = grossSalary-totalTax

    return (totalTax, netSalary, taxComputation)


#########################################################################################
# Main 
#########################################################################################


def main(): 
    
    ####################################################################################
    # Sidebar 
    ####################################################################################    
    with st.sidebar:

        with st.expander("Input Data", expanded=True):
            grossSalary = st.number_input("Bruttolønn:", value=600000, help="Lønn før skatt")
            pensionRate = st.number_input("Pensjonsinnskudd:", value=4.0, help="hva får du i pensjon?")
            vacationAddition = st.number_input("Feriepenger:", value=10.2, help="Proent av feriepenge grunnlaget")
          
    

    ####################################################################################
    # Main Window 
    ####################################################################################

    with st.expander("Beregning av Alminnelig Inntekt", expanded=True): 

        st.write("Ferie")
        feriePengeGrunnlag = grossSalary*(vacationAddition/100.0)
        st.write(feriePengeGrunnlag)

        st.write("Pensjon")
        
    with st.expander("Beregning av Skatt (kun basert på arbeidsinntekt)", expanded=True): 

        (totalTax, netSalary, taxComputation) = getTaxTable(grossSalary-personFradrag, taxProgressiveTable_2022)

        df = pd.DataFrame(taxComputation, columns=['Skatt %', 'Fra', 'Til', 'Oppnådd skatt'], index=[("Trinn %d" % (x+1)) for x in range(len(taxComputation))])
        st.table(df)
        st.write("Estimert Skatt:.... %s kr" % f'{int(totalTax):,}')
        st.write("Skatteprosent:...%.2f%%" % float((totalTax/grossSalary)*100.0))
        st.write("Maks Lønn Per Mnd:.... %s kr" % f'{int(netSalary/12.0):,}')
        st.write("Allminnelig inntekt innbefatter flere vederlag enn arbeidsinntekt, derfor er skatt max lønn høyere enn det du ser på lønnslippen.")

    st.write("https://www.skatteetaten.no/satser/trinnskatt/#rateShowYear")
    st.write("Version 0.0 alpha")
    return True


#########################################################################################
# Init 
#########################################################################################
if __name__ == "__main__":
    st.set_page_config(
        "Trinnskatts Beregning",
        "📊",
        initial_sidebar_state="expanded",
        layout="wide",
    )
    main()
