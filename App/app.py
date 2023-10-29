import streamlit as st
from newdataset2 import plot
from newdataset2 import decreased_df
import plotly.express as px
import pandas as pd
st.set_page_config(page_title="My Streamlit App")



st.markdown(
    """
    <style>
        .theory, .text {
            font-size: 25px !important;
            text-align: justify;
        }
    </style>
    """,
    unsafe_allow_html=True
)

def main():
    menu = ["Home", "The Covid Effect", "Top 10 Startups Revenue generation wise", "Page 3"]
    choice = st.sidebar.selectbox("Select a page", menu)

    if choice == "Home":
        st.title("Welcome to the Indian Startup Ecosystem Analysis")
        st.markdown(
            "<div class='theory'>"
            "The Indian startup ecosystem has experienced remarkable growth and funding from 2018 to 2023, particularly"
            " in sectors like Artificial Intelligence (AI) and Electric Vehicles (EV). However, a comprehensive analysis of"
            " the market trends and underlying factors driving this growth is needed. This problem statement aims to address"
            " the challenges of conducting a detailed market analysis, identifying growth factors, deriving data-driven insights,"
            " and developing an interactive dashboard using Streamlit. By addressing these challenges, participants will"
            " contribute to a better understanding of the Indian startup ecosystem's growth in the AI and EV sectors, providing"
            " valuable insights for entrepreneurs, investors, policymakers, and other stakeholders. You can use openly available"
            " news and/or any publicly available datasets for performing this case study."
            "</div>",
            unsafe_allow_html=True
        )

        st.header("Key Questions to Explore:")

        st.markdown(
        """
        <Div class='theory'>
        <ul>
            <li>What are the top 10 startups in terms of revenue over the last 5 years?</li>
            <li>Give a location-wise distribution of the top 100 startups.</li>
            <li>Give a comparison between Foreign and domestic funds and the sectors they are investing in.</li>
            <li>Valuation based analysis on Fintech companies over the last 5 years.</li>
            <li>How did Covid affect funding for startups across different sectors?</li>
            <li>Which sectors have had the most number of new and emerging startups?</li>
            <li>Compare the growth rate of startups with their age.</li>
            <li>How do funding rounds affect the growth of startups?</li>
            <li>How has funding for different sectors, like EV evolved over time?</li>
            <li>Startups in which sectors have been stagnating or decreasing.</li>
        </ul>
        </Div>
        """,
        unsafe_allow_html=True
        )

        st.write(
            "To explore these questions, navigate through the pages using the sidebar on the left."
        )

    elif choice == "The Covid Effect":
        st.title("The Covid Effect")
        fig = plot(decreased_df, 'Industry', 'Decrease_Percentage')
        st.pyplot(fig)

    elif choice == "Top 10 Startups Revenue generation wise":
        from line_graph import process_data, create_line_chart
        data = "Book1.xlsx"
        df = process_data(data)
        st.write("## Revenue Growth Over the Years")
        st.pyplot(create_line_chart(df))

    elif choice == "Page 3":
        st.title("Page 3")
        st.write("This is page 3.")

if __name__ == "__main__":
    main()
