🏥 Healthcare Claims Anomaly Detection
This project analyzes Medicare Part D prescription claims data to identify potential anomalies that may indicate fraud, waste, or abuse. By applying unsupervised machine learning algorithms, we aim to flag unusual billing patterns and enhance claim verification processes.

🚀 Project Objective
To detect outlier patterns in healthcare claims using anomaly detection techniques like Isolation Forest and Local Outlier Factor (LOF)—helping reduce financial losses and support proactive fraud prevention.

📊 Dataset
Source: Kaggle - Medicare Part D Prescriber Data
Key Features:

Provider ID: Unique identifier for each prescriber

Drug Name: Name of the prescribed drug

Total Claim Count: Number of prescription claims

Total Drug Cost: Total cost billed to Medicare

Total Days Supplied: Duration (in days) of drugs prescribed

🧠 Techniques Used
Data Cleaning & Aggregation (Pandas, NumPy)

Feature Scaling (StandardScaler)

Anomaly Detection

Isolation Forest

Local Outlier Factor (LOF)

Outlier Visualization (Box plots, Scatter plots)

📈 Deliverables
Interactive Dashboards (Power BI / Tableau) to visualize:

High-risk providers and drugs

Cost anomalies vs. peer benchmarks

Jupyter Notebook for:

Exploratory Data Analysis (EDA)

Model building and interpretation

GitHub Repository with:

Clean, modular code

Visual reports and findings

Version-controlled experimentation

🔧 Tech Stack
Languages: Python

Libraries: Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn

Visualization: Power BI / Tableau

Environment: Jupyter Notebook

Version Control: Git + GitHub

You can download the dataset from Kaggle here:
Healthcare Provider Fraud Detection Dataset
## 📊 Healthcare Claims Anomaly Detection

This end-to-end project analyzes Medicare claims data to detect potentially fraudulent healthcare providers. It applies both unsupervised (Isolation Forest) and supervised (Random Forest) machine learning models to identify anomalies in claim behavior.

### 💡 Highlights:
- Cleaned and explored real-world fraud labels
- Aggregated Inpatient & Outpatient claims to engineer features
- Created new features like average claim amounts and total reimbursements
- Trained two models:
  - Isolation Forest for anomaly detection
  - Random Forest for supervised fraud classification
- Visualized feature importance and confusion matrix
- Modularized code into reusable scripts and organized everything in a professional GitHub layout
