import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st  

def process_data(file_path):
    # Read the Excel data
    df = pd.read_excel(file_path)

    # Transpose the DataFrame
    df = df.set_index('Company').T

    # Get the top 5 companies by revenue
    top_companies = df.sum().sort_values(ascending=False).head(10).index

    # Filter the DataFrame to only include the top 5 companies and non-null values
    df = df[top_companies].dropna()

    return df


def create_line_chart(df):
    # Create the line chart
    fig, ax = plt.subplots(figsize=(10, 6))
    for company in df.columns:
        ax.plot(df.index.astype(str), df[company], label=company)

    ax.set_xlabel('Year')
    ax.set_ylabel('Revenue (in billions)')
    ax.set_title('Revenue Growth Over the Years')
    ax.legend()
    ax.grid(True)
    return fig


data = process_data("Book1.xlsx")
st.line_chart(data)
