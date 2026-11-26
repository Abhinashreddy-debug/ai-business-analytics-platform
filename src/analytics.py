def kpis(d):
    return {"Revenue":d.revenue.sum(),"Profit":d.profit.sum(),"Orders":d.order_id.nunique(),
    "Average order value":d.groupby("order_id").revenue.sum().mean(),
    "Profit margin":d.profit.sum()/d.revenue.sum()*100 if d.revenue.sum() else 0}
def monthly(d):
    return d.groupby("month",as_index=False).agg(revenue=("revenue","sum"),profit=("profit","sum"),orders=("order_id","nunique")).sort_values("month")
def by_category(d):
    return d.groupby("category",as_index=False).agg(revenue=("revenue","sum"),profit=("profit","sum"),units=("units_sold","sum")).sort_values("revenue",ascending=False)
def by_region(d):
    return d.groupby("region",as_index=False).agg(revenue=("revenue","sum"),profit=("profit","sum"),orders=("order_id","nunique")).sort_values("revenue",ascending=False)
