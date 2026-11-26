import sys, unittest
from pathlib import Path
import pandas as pd
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from src.data_prep import load_and_clean
from src.analytics import kpis,monthly,by_category,by_region
from src.ml_model import train_profit_model
from src.insights import generate_insights
class ProjectTests(unittest.TestCase):
 @classmethod
 def setUpClass(cls): cls.df=load_and_clean(ROOT/"data/sales_transactions.csv")
 def test_cleaning(self):
  self.assertEqual(int(self.df.isna().sum().sum()),0); self.assertEqual(self.df.order_id.nunique(),len(self.df))
 def test_kpis(self):
  k=kpis(self.df); self.assertGreater(k["Revenue"],0); self.assertGreater(k["Profit"],0); self.assertEqual(k["Orders"],len(self.df))
 def test_group_summaries(self):
  self.assertEqual(set(by_region(self.df).region),set(self.df.region.unique())); self.assertEqual(set(by_category(self.df).category),set(self.df.category.unique())); self.assertGreater(len(monthly(self.df)),1)
 def test_ml(self):
  _,m,p=train_profit_model(self.df); self.assertTrue(all(pd.notna(v) for v in m.values())); self.assertGreater(len(p),0); self.assertGreaterEqual(m["MAE"],0); self.assertGreaterEqual(m["RMSE"],0)
 def test_insights(self):
  t,s=generate_insights(self.df); self.assertTrue(t.strip()); self.assertIn(s,["Built-in analytics insight engine","Live LLM"])
if __name__=="__main__": unittest.main()
