# Sales Dashboard (PySpark + Streamlit)

An interactive sales analysis dashboard built with Streamlit.  
Users can upload a CSV file, filter data, view visualizations, and download cleaned results.

## Features
- Upload your own `sales_data.csv`
- Filter by product category or region
- View charts:
  - Sales by category
  - Average discount by customer type
  - Sales trend over time
- Download cleaned data with profit column

## Tech Stack
- Python
- PySpark
- Pandas
- Streamlit
- Matplotlib

## Running the App Locally

```bash
pip install -r requirements.txt
streamlit run app.py
