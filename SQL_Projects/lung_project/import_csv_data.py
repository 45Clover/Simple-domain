import sqlite3
import csv

def import_csv_to_db(db_name, table_name, csv_file, columns):
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()

    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        data = [tuple(row[col] for col in columns) for row in reader]

    placeholders = ','.join(['?'] * len(columns))
    query = f"INSERT INTO {table_name} ({','.join(columns)}) VALUES ({placeholders})"

    cur.executemany(query, data)
    conn.commit()
    conn.close()
    print(f"✅ Imported {len(data)} rows into {table_name}")

# --- Import everything ---
import_csv_to_db("lung_project.db", "patients",
    "patients.csv", ["full_name", "age", "gender", "region", "smoking_status"])

import_csv_to_db("lung_project.db", "lung_tests",
    "lung_tests.csv", ["patient_id", "test_date", "fev1", "fvc", "pef", "spo2", "diagnosis"])

import_csv_to_db("lung_project.db", "symptoms",
    "symptoms.csv", ["name"])

import_csv_to_db("lung_project.db", "patient_symptoms",
    "patient_symptoms.csv", ["patient_id", "symptom_id", "symptom_date"])

