import streamlit as st
import pandas as pd
import plotly.express as px

# Title of the Streamlit app
st.title("Actual vs Predicted Weekly Rain Data for 2025")

# Path to the Excel file
file_path = "/content/SARIMA_forecasts_2025 (2).xlsx"

# Read the data from the Excel file
try:
    pred_df_from_file = pd.read_excel(file_path)

    # Convert the 'Date' column to datetime objects
    pred_df_from_file['Date'] = pd.to_datetime(pred_df_from_file['Date'])

    # Filter data for Max Frekuensi, Rain Fall (mm) and Rain Duration (jam)
    freq_data = pred_df_from_file[pred_df_from_file['Target'] == 'Freq. Rain_agg_max'].copy()
    rain_data = pred_df_from_file[pred_df_from_file['Target'] == 'Rain Fall (mm)_agg_max'].copy()
    dur_data = pred_df_from_file[pred_df_from_file['Target'] == 'Rain (Duration)_agg_max'].copy()

    # Create the interactive plot using Plotly Express
    fig = px.line()

    # Add Actual values
    fig.add_scatter(x=freq_data['Date'], y=freq_data['Actual'], mode='lines', name='Actual Max Frekuensi', line=dict(dash='dash'))
    fig.add_scatter(x=rain_data['Date'], y=rain_data['Actual'], mode='lines', name='Actual Rain Fall (mm)', line=dict(dash='dash'))
    fig.add_scatter(x=dur_data['Date'], y=dur_data['Actual'], mode='lines', name='Actual Rain Duration (jam)', line=dict(dash='dash'))

    # Add Predicted values
    fig.add_scatter(x=freq_data['Date'], y=freq_data['Forecast'], mode='lines', name='Pred Max Frekuensi')
    fig.add_scatter(x=rain_data['Date'], y=rain_data['Forecast'], mode='lines', name='Pred Rain Fall (mm)')
    fig.add_scatter(x=dur_data['Date'], y=dur_data['Forecast'], mode='lines', name='Pred Rain Duration (jam)')


    fig.update_layout(
        title='Actual vs Predicted Weekly Data for 2025',
        xaxis_title='Date',
        yaxis_title='Value'
    )

    # Display the Plotly chart in Streamlit
    st.plotly_chart(fig, use_container_width=True)

except FileNotFoundError:
    st.error(f"Error: The file was not found at {file_path}")
except KeyError as e:
    st.error(f"Error: Missing expected column in the data: {e}")
except Exception as e:
    st.error(f"An unexpected error occurred: {e}")
