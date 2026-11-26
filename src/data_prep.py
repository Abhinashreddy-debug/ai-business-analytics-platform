import pandas as pd
NUMERIC=["units_sold","unit_price","discount_pct","marketing_spend","revenue","cost","profit"]
def load_and_clean(source):
    d=pd.read_csv(source); d["order_date"]=pd.to_datetime(d["order_date"],errors="coerce")
    for c in NUMERIC: d[c]=pd.to_numeric(d[c],errors="coerce")
    for c in ["region","category","product","customer_type","payment_method"]:
        if d[c].isna().any():
            m=d[c].mode(); d[c]=d[c].fillna(m.iloc[0] if len(m) else "Unknown")
    for c in NUMERIC:
        if d[c].isna().any(): d[c]=d[c].fillna(d[c].median())
    d=d.dropna(subset=["order_date"]).drop_duplicates("order_id")
    d["month"]=d["order_date"].dt.to_period("M").astype(str)
    d["profit_margin_pct"]=(d.profit/d.revenue.replace(0,pd.NA)*100).fillna(0)
    return d
