# Power BI DAX measures (table: sales_transactions)
```DAX
Total Revenue = SUM(sales_transactions[revenue])
Total Profit = SUM(sales_transactions[profit])
Total Orders = DISTINCTCOUNT(sales_transactions[order_id])
Units Sold = SUM(sales_transactions[units_sold])
Average Order Value = DIVIDE([Total Revenue], [Total Orders], 0)
Profit Margin % = DIVIDE([Total Profit], [Total Revenue], 0)
Average Discount % = AVERAGE(sales_transactions[discount_pct])
```
Format revenue, profit and AOV as INR currency; margin and discount as percentages.
