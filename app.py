from pathlib import Path
import streamlit as st, pandas as pd, plotly.express as px
from dotenv import load_dotenv
from src.data_prep import load_and_clean
from src.analytics import kpis,monthly,by_category,by_region
from src.ml_model import train_profit_model
from src.insights import generate_insights
ROOT=Path(__file__).parent; load_dotenv(ROOT/".env")
st.set_page_config(page_title="AI Business Analytics",page_icon="📊",layout="wide")
st.title("📊 AI-Powered Business Analytics Platform")
st.caption("Python • Pandas • Machine Learning • Generative AI • Power BI")
with st.sidebar:
    st.header("Data")
    upload=st.file_uploader("Upload compatible sales CSV",type=["csv"])
source=upload if upload is not None else ROOT/"data/sales_transactions.csv"
d=load_and_clean(source)
with st.sidebar:
    dr=st.date_input("Date range",(d.order_date.min().date(),d.order_date.max().date()))
    regs=st.multiselect("Region",sorted(d.region.unique()),default=sorted(d.region.unique()))
    cats=st.multiselect("Category",sorted(d.category.unique()),default=sorted(d.category.unique()))
if isinstance(dr,tuple) and len(dr)==2:
    v=d[(d.order_date>=pd.Timestamp(dr[0]))&(d.order_date<pd.Timestamp(dr[1])+pd.Timedelta(days=1))&d.region.isin(regs)&d.category.isin(cats)].copy()
else: v=d[d.region.isin(regs)&d.category.isin(cats)].copy()
if v.empty: st.warning("No records match filters."); st.stop()
st.success(f"{len(d):,} cleaned records loaded; {len(v):,} selected")
k=kpis(v); cols=st.columns(5)
for col,(name,val) in zip(cols,k.items()):
    col.metric(name,f"₹{val:,.0f}" if name!="Orders" and name!="Profit margin" else (f"{val:.1f}%" if name=="Profit margin" else f"{val:,.0f}"))
st.subheader("Business performance")
m=monthly(v); a,b=st.columns(2)
a.plotly_chart(px.line(m,x="month",y="revenue",markers=True,title="Monthly revenue"),use_container_width=True)
b.plotly_chart(px.bar(by_category(v),x="category",y="revenue",color="category",title="Revenue by category"),use_container_width=True)
c,e=st.columns(2)
c.plotly_chart(px.bar(by_region(v),x="region",y="profit",color="region",title="Profit by region"),use_container_width=True)
pay=v.groupby("payment_method",as_index=False).agg(orders=("order_id","nunique"))
e.plotly_chart(px.pie(pay,names="payment_method",values="orders",hole=.4,title="Payment mix"),use_container_width=True)
st.subheader("AI-assisted business insights")
if st.button("Generate insights",type="primary"):
    with st.spinner("Analysing..."):
        text,source_name=generate_insights(v)
    st.caption("Insight source: "+source_name); st.markdown(text)
st.subheader("Machine Learning: transaction profit estimation")
st.write("Random Forest regression with an 80/20 chronological train/test split.")
if len(v)>=100:
    with st.spinner("Training and evaluating model..."):
        model,metrics,res=train_profit_model(v)
    x,y,z=st.columns(3); x.metric("MAE",f"₹{metrics['MAE']:,.0f}"); y.metric("RMSE",f"₹{metrics['RMSE']:,.0f}"); z.metric("R²",f"{metrics['R2']:.3f}")
    st.plotly_chart(px.scatter(res.head(250),x="Actual profit",y="Predicted profit",title="Actual vs predicted profit"),use_container_width=True)
else: st.info("Select at least 100 records to train the model.")
st.subheader("Cleaned transaction data")
st.dataframe(v.head(1000),use_container_width=True,hide_index=True)
st.download_button("Download cleaned CSV",v.to_csv(index=False).encode(),file_name="cleaned_sales_data.csv")
st.download_button("Download monthly Power BI summary",m.to_csv(index=False).encode(),file_name="monthly_kpi_summary.csv")
with st.expander("Data quality report"):
    st.write({"Rows":len(d),"Missing values after cleaning":int(d.isna().sum().sum()),"Date range":f"{d.order_date.min().date()} to {d.order_date.max().date()}"})
