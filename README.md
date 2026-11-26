# AI-Powered Business Analytics Platform
A portfolio project combining data preparation, descriptive analytics, interactive dashboards, a machine-learning model, optional LLM-assisted insights and Power BI exports.

## Features
- 3,000-row **synthetic** retail transaction dataset (not real company data).
- Data cleaning, missing-value imputation and duplicate removal using Pandas.
- KPIs: revenue, profit, order count, average order value and profit margin.
- Interactive Streamlit dashboard and Plotly charts.
- Random Forest regression to estimate transaction profit.
- Chronological 80/20 holdout evaluation using MAE, RMSE and R².
- Evidence-based built-in business insights; optional live LLM integration if an API key is configured.
- CSV exports and suggested Power BI DAX measures.

## Run on Windows 11
```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```
Open the local URL shown in the terminal. The included dataset loads automatically. No API key is required for the built-in insight engine.

## Optional live LLM
Copy `.env.example` to `.env`, add your own `OPENAI_API_KEY`, and optionally change `OPENAI_MODEL`. Never commit `.env` or expose the key. API usage may cost money.

## Power BI
Import `data/sales_transactions.csv` in Power BI Desktop, check data types, create measures from `powerbi/DAX_MEASURES.md`, and build an executive overview with KPI cards, monthly trend, category and regional charts, and slicers.

## Interview explanation (after you have run and understood it)
"I developed an end-to-end business analytics platform using Python and Pandas. It cleans transaction data, calculates business KPIs and presents interactive visualizations. I also trained a Random Forest regression model to estimate transaction profit and evaluated it using MAE, RMSE and R-squared on a chronological holdout set. The platform generates evidence-based business insights and exports cleaned data for Power BI."

## Limitations
The included data is synthetic. Model results are for learning and demonstration only and do not establish real-world business performance. Explain the target, features, data split and metrics honestly in interviews.

## Automated validation and outputs
Run `python -m unittest discover -s tests -v` from the project root. Model metrics, held-out predictions, business insight example and Power BI-ready summaries are in `artifacts/`.

## Power BI Desktop deliverable
Follow `powerbi/BUILD_THE_PBIX.md` to create and save the actual `.pbix`. The PBIX must be saved from Power BI Desktop; this source package contains the data, DAX and report blueprint.

## GitHub publishing
Upload the contents of this folder to a repository such as `ai-powered-business-analytics`. Do not upload `.env`, API keys, virtual environments or private data. Add your own dashboard screenshots after running the app. Clearly identify the sample dataset as synthetic.
