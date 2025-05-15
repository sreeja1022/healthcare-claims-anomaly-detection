def add_derived_features(df):
    df['Inpatient_Avg_Claim'] = df['Inpatient_Total_Reimbursed'] / df['Inpatient_Claim_Count']
    df['Outpatient_Avg_Claim'] = df['Outpatient_Total_Reimbursed'] / df['Outpatient_Claim_Count']
    df['Total_Claims'] = df['Inpatient_Claim_Count'] + df['Outpatient_Claim_Count']
    df['Total_Reimbursed'] = df['Inpatient_Total_Reimbursed'] + df['Outpatient_Total_Reimbursed']
    return df
