# Create the actual Power BI report (.pbix)

A `.pbix` is authored and saved in Microsoft Power BI Desktop. This project supplies tested source data, DAX measures, and a page blueprint; it does not claim to include a finished PBIX.

## Import
Power BI Desktop → Get data → Text/CSV → `data/sales_transactions.csv`. Set `order_date` to Date; numeric measures to Whole/Decimal Number; IDs and categories to Text.

## DAX
Use `DAX_MEASURES.md` to create Total Revenue, Total Profit, Total Orders, Units Sold, Average Order Value, Profit Margin %, and Average Discount %. Format currency as INR and margin/discount as percentages.

## Pages
**Executive Overview:** five KPI cards; monthly revenue line chart; revenue by category; profit by region; date, region and category slicers.

**Product & Customer:** revenue by product; orders by customer type; payment method mix; category profitability matrix.

**Profitability:** profit by region; profit margin by category; marketing spend vs profit scatter; date/region/category slicers.

## Save and validate
Save as `powerbi/AI_Business_Analytics_PowerBI.pbix`. Change slicers and compare totals with Streamlit using identical filters. Data is synthetic.
