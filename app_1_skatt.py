#########################################################################################
#
# Del 1 i Pensjonsprosjetet
# Finne egnede strukturerer for å elegant regne ut og presentere trinnskatten 
# 
#########################################################################################

import math
import streamlit as st
import matplotlib.pyplot as plt

#########################################################################################
# Constants  
#########################################################################################

taxBase = 22.0
taxWelfare = 8.2

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
    baseTax = grossSalary*((taxBase+taxWelfare)/100.0)

    st.write("Trinn 0:", baseTax)

    for step, row in enumerate(table):
        tax_step = max(0, min(grossSalary, row[2])-row[1])*(row[0]/100.0)
        if tax_step == 0:
            break
        taxSteps.append(tax_step)
        st.write(step+1, tax_step)
    

    totalTax = baseTax + sum(taxSteps)
    st.write("Total Tax:", totalTax)
    st.write("Tax Precentage:", (totalTax/grossSalary)*100.0)
    st.write("Montly Salary:", (grossSalary-totalTax)/12.0)

#########################################################################################
# Main 
#########################################################################################


def main(): 
    
    ####################################################################################
    # Sidebar 
    ####################################################################################    
    with st.sidebar:

        with st.expander("Input Data", expanded=True):
            salaryBase = st.number_input("Bruttolønn:", value=600000, help="Lønn før skatt")
          
    
    ####################################################################################
    # Main Window 
    ####################################################################################

    with st.expander("Beregning av Skatt", expanded=True): 

        getTaxTable(salaryBase, taxProgressiveTable_2022)

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
