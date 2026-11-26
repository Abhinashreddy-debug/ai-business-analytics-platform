import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.impute import SimpleImputer
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
FEATURES=["units_sold","unit_price","discount_pct","marketing_spend","region","category","customer_type","payment_method","month_num"]
def train_profit_model(d):
    x=d.copy().sort_values("order_date"); x["month_num"]=x.order_date.dt.month
    split=int(len(x)*.8); X=x[FEATURES]; y=x.profit
    numeric=["units_sold","unit_price","discount_pct","marketing_spend","month_num"]
    categorical=["region","category","customer_type","payment_method"]
    prep=ColumnTransformer([("num",SimpleImputer(strategy="median"),numeric),
    ("cat",Pipeline([("imputer",SimpleImputer(strategy="most_frequent")),("onehot",OneHotEncoder(handle_unknown="ignore"))]),categorical)])
    model=Pipeline([("prep",prep),("rf",RandomForestRegressor(n_estimators=150,max_depth=14,min_samples_leaf=3,random_state=42,n_jobs=-1))])
    model.fit(X.iloc[:split],y.iloc[:split]); pred=model.predict(X.iloc[split:])
    metrics={"MAE":mean_absolute_error(y.iloc[split:],pred),"RMSE":mean_squared_error(y.iloc[split:],pred)**.5,"R2":r2_score(y.iloc[split:],pred)}
    return model,metrics,pd.DataFrame({"Actual profit":y.iloc[split:].values,"Predicted profit":pred})
