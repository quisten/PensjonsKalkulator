import streamlit as st

#########################################################################################
# Main
#########################################################################################
def main():
    st.title("Sparing i ASK vs IPS")
    st.text("For langsiktig sparing myntet på pensjon så vil det være fordeler og ulemper mellom IPS og ASK")
    st.text("ASK vil gjøre pengene tilgjenglig mens IPS gir noen skattemessige fordeler som er utsatt for politisk taskenspilleri. ")

#########################################################################################
# Init 
#########################################################################################
if __name__ == "__main__":
    st.set_page_config(
        "Privat Pensjonssparing",
        "📊",
        initial_sidebar_state="expanded",
        layout="wide",
    )
    main()

