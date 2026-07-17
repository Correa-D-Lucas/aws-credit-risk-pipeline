Credit Risk Project - Data Engineering & Analytics
================================================

Overview
--------
This project is a credit risk-focused data engineering and analytics workspace. It is designed to ingest raw loan and customer data, build a layered data architecture (Bronze → Silver → Gold), and produce business-ready datasets and dashboards to answer portfolio, underwriting, and collections questions.

Key business questions
- Portfolio health: default rate, trend over time, high-risk segments, expected loss, regional exposure.
- Underwriting: features most associated with default, scoring and cutoff optimization.
- Collections: prioritization of delinquent accounts and identification of accounts likely to cure.

Data required
- Customer data (application form): `customer_id`, `age`, `income`, `employment_status`, `years_employed`, `marital_status`, `region`, `education`.
- Loan data: `loan_id`, `customer_id`, `loan_amount`, `interest_rate`, `term_months`, `origination_date`, `loan_purpose`.
- Payment history: `payment_id`, `loan_id`, `payment_date`, `due_date`, `amount_due`, `amount_paid`, `days_past_due`.
- Default events: `loan_id`, `default_flag`, `default_date`, `charge_off_amount`, `recovery_amount`.

Architecture
------------
- Bronze (raw): store raw CSVs as-is (customers.csv, loans.csv, payments.csv, defaults.csv).
- Silver (cleaned): deduplicate, validate dates, handle missing values, standardize regions, create surrogate keys.
- Gold (business-ready): aggregated tables for Portfolio Summary, Customer Risk, and Loan Performance.

Dashboard ideas
---------------
- Executive: total exposure, default rate, loss rate, average credit score, active loans.
- Delinquency: 30/60/90 DPD breakdown, trending defaults.
- Geographic risk: exposure and default rate by region.
- Customer segmentation: income/age/employment bands.
- Vintage analysis: performance by origination month.

Data source
-----------
Initial dataset reference: https://www.kaggle.com/competitions/home-credit-default-risk/overview

Progress (from `progress_diary.txt`)
----------------------------------
Summary (English)
- Jul 14, 2026: Project re-started; defined scope (credit risk, data engineering + analytics); located dataset on Kaggle.
- Jul 15, 2026: Brainstormed project questions; downloaded and imported datasets into `data/`.
- Jul 16, 2026: Created folder structure and initial scripts: `src/ingestion/raw_to_bronze.py`, `src/utils/spark_session.py`, and `src/main.py`; updated `requirements.txt` and `docker/dockerfile`; built image `credit_risk_imagem` and container `credit-risk-container`.
- Jul 17, 2026: Resolved library conflicts (pandas/pyspark), rebuilt container, tested `src/main.py` (works), pushed updates to GitHub; used Copilot to draft this README.

Entradas originais (Português)
- 14 de Julho de 2026: voltei com o projeto; estudo do escopo; dataset encontrado no Kaggle.
- 15 de Julho de 2026: comecei o brainstorm; analisei o dataset; importei dados para `data/`.
- 16 de Julho de 2026: criei `ingestion/` e `utils/` e os arquivos `spark_session.py`, `raw_to_bronze.py` e `main.py`; reescrevi `requirements.txt` e `dockerfile`; criei imagem e container; criei `progress_diary.txt`.
- 17 de Julho de 2026: resolvi conflito de bibliotecas; atualizei `requirements.txt`, rebuild da imagem e container; testei `src/main.py`; force push para GitHub; usei Copilot para escrever o readme.rd.

Next steps
----------
- Continue ETL: implement Silver transforms and Gold aggregations.
- Add automated tests and CI for the ingestion pipeline.
- Build dashboard prototypes for executive and delinquency views.
- Optionally sync this content into `README.md`.

Files/Locations
---------------
- Ingestion code: `src/ingestion/raw_to_bronze.py`
- Spark session helper: `src/utils/spark_session.py`
- Entrypoint: `src/main.py`
- Data: `data/raw/`, `data/bronze/`, `data/silver/`, `data/gold/`

If you'd like, I can update `README.md` with this content or expand any section.
# aws-credit-risk-pipeline
AWS Data Engineering Pipeline using S3, Spark and dbt for Credit Risk Analytics.
