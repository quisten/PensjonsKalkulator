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
baseNumber_2022 = 111477
benefitsEKOM_rate = 4392 # Regardless of 1 or several services
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
  
    return (totalTax, taxComputation)


#########################################################################################
# Main 
#########################################################################################


def main(): 
    
    st.title("Forenklet Inntektsskatteberegning")
    ####################################################################################
    # Sidebar | Inputs
    ####################################################################################    
    with st.sidebar:

        with st.expander("Input Lønn", expanded=True):
            grossSalary = st.number_input("Bruttolønn:", value=600000, help="Lønn før skatt")
            grossBonus = st.number_input("Bonus", value=0000, help="Bonus før skatt")
            grossSalary += grossBonus
            
            pensionRate = st.number_input("Pensjonsinnskudd:", value=4.0, help="hva får du i pensjon?")
            pensionOverflow = st.checkbox("Økt Pensjon etter 6G?", value=False, help="Does the basePension increase for the salary overflowing 6G? Increase with basePension+18.1%% for overflowing income.")
            
            vacationAddition = st.number_input("Feriepenger:", value=12.0, help="Proent av feriepenge grunnlaget")
            vacationPeriod = st.number_input("Antall Ferieuker", value=5, help="Hvor mange uker ferie, brukes til å beregne trekk mot feriepenger")
    
            benefitsEKOM = st.checkbox("Telefon / Internett fra Arb.giver?", value=False, help="Betaler Arb.giver telefon eller internett?")
            
        with st.expander("Input Andre Inntekter", expanded=False):
            incomeRent = st.number_input("Inntekt Utleie:", value=0)
            incomeAksjer = st.number_input("Inntekt Aksjer:", value=0)
            incomeInterest = st.number_input("Inntekt Renter:", value=0)
            incomeOtherJobs = st.number_input("Andre Verv:", value=0)
    ####################################################################################
    # Main Window 
    ####################################################################################

    with st.expander("Beregning av Alminnelig Inntekt", expanded=True): 

        st.write("**Feriepenger er Skattpliktig Inntekt** (4u 10.2%, 5u 12% og 6u 14.3%)")
        feriePengeGrunnlag = grossSalary*(vacationAddition/100.0)
        st.write("Feriepengegrunnlaget er: %s" % f'{int(feriePengeGrunnlag):,}')

        st.markdown("**Pensjon er Skattepliktig Inntekt**")
        pensjonsGrunnlag = grossSalary*(pensionRate/100.0)
        #st.write("Tjeneste Pensjonen er estimert til: %d" % pensjonsGrunnlag)
       
        if pensionOverflow:
            pensjonsKompensasjon = max(0.0, grossSalary-6.0*baseNumber_2022)*(18.1/100.0)
            pensjonsGrunnlag += pensjonsKompensasjon
            st.write("Faktisk pensjonsprosent: %.2f%%" % (100.0*float(pensjonsGrunnlag/grossSalary)))
            st.write("Tjeneste Pensjonen er estimert til: %d hvoav %d er fra overskytende" % (pensjonsGrunnlag, pensjonsKompensasjon))

        else:
            st.write("Tjeneste Pensjonen er estimert til: %d" % pensjonsGrunnlag)

    with st.expander("Beregning av Skatt (kun basert på arbeidsinntekt)", expanded=True): 

        adjustGrossSalary = grossSalary*(52.0-vacationPeriod)/52.0
        alminneligInntekt = adjustGrossSalary+pensjonsGrunnlag+feriePengeGrunnlag
        
        st.write("Alminnelig Inntekt: %s" % f'{int(alminneligInntekt):,}')
        st.write("Skattepliktig Inntekt: %s  (minus personFradrag)" % f'{int(alminneligInntekt-personFradrag):,}')
        (totalTax, taxComputation) = getTaxTable(alminneligInntekt-personFradrag, taxProgressiveTable_2022)
        netSalary = grossSalary-totalTax

        if benefitsEKOM:
            netSalary -= benefitsEKOM_rate

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
