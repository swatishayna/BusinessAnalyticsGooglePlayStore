import streamlit as st
from apps import raw,tableau_dashboard,problem_statement,visualisations,transformation, model



choice = st.sidebar.selectbox("Select",("Problem Statement","Raw Dataset and Cleaned Dataset", "Operations on Cleaned Dataset", "Tableau Dashboard", "Google PlayStore Rating Prediction App"))
if choice == "Problem Statement":
    problem_statement.writeup()
elif choice=="Raw Dataset and Cleaned Dataset":
    raw.Raw_Data().run()
elif choice == "Operations on Cleaned Dataset":
    visualisations.Analysis().run()
elif choice == "Tableau Dashboard":
    tableau_dashboard.display_tableauReport()
else:
    transformation.Transform_Train().run()
