import streamlit as st
from newdataset2 import plot
from newdataset2 import decreased_df
import plotly.express as px
import pandas as pd
st.set_page_config(page_title="My Streamlit App")






def main():

    menu = ["Home", "The Covid Effect", "Top 10 Startups Revenue generation wise", "The Affected Sectors"]
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
            "</div>"
            
            
            
            ,
            unsafe_allow_html=True
        )

        st.header("Key Questions to Explore:")
        st.markdown(
            "<div class='text'>"
            "<ul>"
            "<li>What are the top 10 startups in terms of revenue over the last 5 years?</li>"
            "<li>Give a location-wise distribution of the top 100 startups.</li>"
            "<li>Give a comparison between Foreign and domestic funds and the sectors they are investing in.</li>"
            "<li>Valuation based analysis on Fintech companies over the last 5 years.</li>"
            "<li>How did Covid affect funding for startups across different sectors?</li>"
            "<li>Which sectors have had the most number of new and emerging startups?</li>"
            "<li>Compare the growth rate of startups with their age.</li>"
            "<li>How do funding rounds affect the growth of startups?</li>"
            "<li>How has funding for different sectors, like EV evolved over time?</li>"
            "<li>Startups in which sectors have been stagnating or decreasing.</li>"
            "</ul>"
            "</div>",
            unsafe_allow_html=True
        )


        st.markdown(
            "<h4>To explore these questions, navigate through the pages using the sidebar on the left.</h4>",
            unsafe_allow_html=True
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

    elif choice == "The Affected Sectors":
        
        st.header("Startups in which sectors have been stagnating or decreasing.")
        st.markdown("""
        <ol class='big-font'>
            <li>Online Travel Agencies: The COVID-19 pandemic had a significant impact on travel-related startups in India. The restrictions on travel and reduced tourism affected the growth of online travel agencies.</li>
            <li>Hyperlocal Delivery Services: Hyperlocal delivery startups, particularly those focused on delivering groceries, faced stiff competition and margin pressures. Some experienced stagnation due to challenges in achieving profitability.</li>
            <li>FoodTech: The food delivery sector in India was highly competitive, with many startups struggling to achieve profitability. The market was saturated, and customer acquisition costs were high.</li>
            <li>Real Estate Tech: The real estate technology sector in India faced challenges due to market volatility and regulatory complexities. Startups in this space often found it difficult to scale.</li>
            <li>E-commerce: While e-commerce remained a significant sector, intense competition, and the dominance of major players made it challenging for newer startups to gain a foothold.</li>
            <li>Education Technology (EdTech): The EdTech sector was highly competitive, and some segments of the market were saturated. Regulatory changes also posed challenges for certain types of educational startups.</li>
            <li>Renewable Energy: Renewable energy startups faced challenges related to funding and regulatory complexities. The sector required substantial capital investment, which was not always readily available.</li>
            <li>Agriculture Tech: While agriculture technology had potential, adoption in traditional farming communities and complex supply chain issues were obstacles for startups in this sector.</li>
            <li>Fashion and Apparel: Fashion e-commerce startups faced challenges due to changing consumer preferences, high return rates, and the need for constant inventory updates.</li>
            <li>Gaming: The mobile gaming sector, while growing, was highly competitive. Monetization and user acquisition challenges led to stagnation for some gaming startups.</li>
            <li>Healthcare: While healthcare startups were growing, the sector was highly regulated, and startups faced challenges related to funding and scaling.</li>
        </ol>""",
        unsafe_allow_html=True)


if __name__ == "__main__":
    main()
