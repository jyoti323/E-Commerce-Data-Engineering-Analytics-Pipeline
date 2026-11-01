# E-Commerce-Data-Engineering-Analytics-Pipeline
#OVERVIEW OF PROJECT:
<img width="959" height="549" alt="Ecommerce Pipeline Guide - Google Chrome 31-10-2026 12_09_28" src="https://github.com/user-attachments/assets/4045a326-60a6-415b-9a62-2d344aa7b5e7" />


#PROJECT OBJECTIVE:

Build an automated data pipeline that collects e-commerce data, cleans and transforms it, stores it in a data warehouse, and generates analytics to help businesses understand their sales, customers, products, and delivery performance.

Business problems you will solve:
- Which products generate the highest revenue?
- Which cities have the most customers?
- What is the monthly sales growth?
- Which products have the highest cancellation rates?
- How long does delivery take?
- Which customers make repeat purchases?
- Which product categories perform best?

#THE FLOW IS:

Data Source → Extract → Load → Transform → Data Warehouse → Analytics

This is called an ETL/ELT pipeline.
- ETL: Extract, Transform, Load.
- ELT: Extract, Load, Transform.
In your project, you can use an ELT approach: load raw data first and then transform it using dbt and SQL.

# Running the loader

Set the `DATABASE_URL` environment variable to a SQLAlchemy-compatible database URL before running `src/load.py`. Keep credentials in your environment or a local, ignored `.env` file; do not commit them.

#Phase 2 – Build the Python ETL pipeline

We will build:
1. extract.py – Extract data from all nine CSV files.
2. validate.py – Check data quality.
3. transform.py – Clean and transform data.
4. load.py – Load data into PostgreSQL.
5. main.py – Execute the complete pipeline.

We will also learn:
- ETL vs ELT.
- Data types and missing values.
- Duplicate detection.
- Primary and foreign keys.
- Error handling and logging
