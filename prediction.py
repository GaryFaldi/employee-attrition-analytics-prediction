import pandas as pd
import numpy as np
import joblib
import sys
import os

# ============================================================
#  Jaya Jaya Maju — Employee Attrition Prediction Script
#  Author : Kadek Gary Faldi
#  Email  : garyfaldi1@gmail.com
# ============================================================

MODEL_DIR = "models"


def load_artifacts():
    """Load model, scaler, encoders, dan feature names."""
    try:
        model         = joblib.load(os.path.join(MODEL_DIR, "best_model.pkl"))
        scaler        = joblib.load(os.path.join(MODEL_DIR, "scaler.pkl"))
        label_enc     = joblib.load(os.path.join(MODEL_DIR, "label_encoders.pkl"))
        feature_names = joblib.load(os.path.join(MODEL_DIR, "feature_names.pkl"))
        return model, scaler, label_enc, feature_names
    except FileNotFoundError as e:
        print(f"[ERROR] Artefak model tidak ditemukan: {e}")
        print("Pastikan notebook sudah dijalankan terlebih dahulu.")
        sys.exit(1)


def preprocess(df: pd.DataFrame, label_enc: dict, feature_names: list) -> pd.DataFrame:
    """Preprocessing input: drop kolom tidak relevan, encode kategorik."""
    drop_cols = ["EmployeeId", "Over18", "StandardHours", "Attrition"]
    df = df.drop(columns=[c for c in drop_cols if c in df.columns], errors="ignore")

    for col, le in label_enc.items():
        if col in df.columns:
            known = set(le.classes_)
            df[col] = df[col].apply(
                lambda x: x if str(x) in known else le.classes_[0]
            )
            df[col] = le.transform(df[col].astype(str))

    for col in feature_names:
        if col not in df.columns:
            df[col] = 0
    df = df[feature_names]

    df = df.fillna(df.median(numeric_only=True))

    return df


def predict_from_csv(filepath: str):
    """Prediksi dari file CSV."""
    print(f"\n{'='*55}")
    print(f"  Jaya Jaya Maju — Employee Attrition Prediction")
    print(f"{'='*55}")

    try:
        df_input = pd.read_csv(filepath)
    except FileNotFoundError:
        print(f"[ERROR] File tidak ditemukan: {filepath}")
        sys.exit(1)

    print(f"\nFile    : {filepath}")
    print(f"Records : {len(df_input)} karyawan\n")

    employee_ids = df_input["EmployeeId"].values if "EmployeeId" in df_input.columns else range(len(df_input))

    model, scaler, label_enc, feature_names = load_artifacts()

    df_proc = preprocess(df_input.copy(), label_enc, feature_names)
    X_scaled = scaler.transform(df_proc)

    y_pred = model.predict(X_scaled)
    y_prob = model.predict_proba(X_scaled)[:, 1]

    results = pd.DataFrame({
        "EmployeeId"       : employee_ids,
        "Attrition_Pred"   : y_pred,
        "Attrition_Label"  : ["Attrition" if p == 1 else "No Attrition" for p in y_pred],
        "Risk_Score (%)"   : (y_prob * 100).round(2),
        "Risk_Category"    : pd.cut(
            y_prob * 100,
            bins=[0, 30, 60, 100],
            labels=["Low Risk", "Medium Risk", "High Risk"]
        )
    })

    total       = len(results)
    attrition   = (results["Attrition_Pred"] == 1).sum()
    no_attrition = total - attrition
    rate        = attrition / total * 100

    print(f"{'─'*55}")
    print(f"  HASIL PREDIKSI")
    print(f"{'─'*55}")
    print(f"  Total karyawan dianalisis : {total}")
    print(f"  Prediksi Attrition (1)    : {attrition} ({rate:.1f}%)")
    print(f"  Prediksi No Attrition (0) : {no_attrition} ({100-rate:.1f}%)")
    print(f"{'─'*55}")
    print(f"\n  Distribusi Risk Category:")
    print(results["Risk_Category"].value_counts().to_string())
    print(f"{'─'*55}")

    high_risk = results[results["Attrition_Pred"] == 1].sort_values(
        "Risk_Score (%)", ascending=False
    ).head(10)

    if not high_risk.empty:
        print(f"\n  Top {len(high_risk)} Karyawan Berisiko Tinggi:")
        print(high_risk[["EmployeeId", "Risk_Score (%)", "Risk_Category"]].to_string(index=False))

    output_file = "prediction_results.csv"
    results.to_csv(output_file, index=False)
    print(f"\n  Hasil lengkap tersimpan di: {output_file}")
    print(f"{'='*55}\n")

    return results


def predict_manual():
    """Prediksi interaktif satu karyawan via input manual."""
    print(f"\n{'='*55}")
    print(f"  Mode Prediksi Manual — Satu Karyawan")
    print(f"{'='*55}\n")

    sample = {
        "Age"                      : 28,
        "BusinessTravel"           : "Travel_Frequently",
        "DailyRate"                : 500,
        "Department"               : "Sales",
        "DistanceFromHome"         : 25,
        "Education"                : 2,
        "EducationField"           : "Marketing",
        "EnvironmentSatisfaction"  : 1,
        "Gender"                   : "Male",
        "HourlyRate"               : 40,
        "JobInvolvement"           : 2,
        "JobLevel"                 : 1,
        "JobRole"                  : "Sales Representative",
        "JobSatisfaction"          : 1,
        "MaritalStatus"            : "Single",
        "MonthlyIncome"            : 2500,
        "MonthlyRate"              : 10000,
        "NumCompaniesWorked"       : 5,
        "OverTime"                 : "Yes",
        "PercentSalaryHike"        : 11,
        "PerformanceRating"        : 3,
        "RelationshipSatisfaction" : 2,
        "StockOptionLevel"         : 0,
        "TotalWorkingYears"        : 4,
        "TrainingTimesLastYear"    : 1,
        "WorkLifeBalance"          : 1,
        "YearsAtCompany"           : 2,
        "YearsInCurrentRole"       : 1,
        "YearsSinceLastPromotion"  : 1,
        "YearsWithCurrManager"     : 1,
    }

    model, scaler, label_enc, feature_names = load_artifacts()
    df_sample = pd.DataFrame([sample])
    df_proc   = preprocess(df_sample, label_enc, feature_names)
    X_scaled  = scaler.transform(df_proc)

    pred = model.predict(X_scaled)[0]
    prob = model.predict_proba(X_scaled)[0][1] * 100

    if prob >= 60:
        risk_cat = "HIGH RISK"
    elif prob >= 30:
        risk_cat = "MEDIUM RISK"
    else:
        risk_cat = "LOW RISK"

    print("  Profil Karyawan:")
    for k, v in sample.items():
        print(f"    {k:<30}: {v}")

    print(f"\n{'─'*55}")
    print(f"  HASIL PREDIKSI")
    print(f"{'─'*55}")
    print(f"  Prediksi   : {'ATTRITION' if pred == 1 else 'NO ATTRITION'}")
    print(f"  Risk Score : {prob:.2f}%")
    print(f"  Kategori   : {risk_cat}")
    print(f"{'='*55}\n")


#  Entry Point
if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Jika argumen CSV diberikan → prediksi batch
        csv_path = sys.argv[1]
        predict_from_csv(csv_path)
    else:
        # Tidak ada argumen → prediksi manual dengan data contoh
        predict_manual()