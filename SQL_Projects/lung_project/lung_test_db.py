import sqlite3
from datetime import date

# Connect to the SQLite database (creates it if it doesn't exist)
conn = sqlite3.connect("lung_project.db")
cur = conn.cursor()

# Create Patients Table
cur.execute("""
CREATE TABLE IF NOT EXISTS patients (
    patient_id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT,
    age INTEGER,
    gender TEXT,
    region TEXT,
    smoking_status TEXT
)
""")

# Create Lung Tests Table
cur.execute("""
CREATE TABLE IF NOT EXISTS lung_tests (
    test_id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id INTEGER,
    test_date DATE,
    fev1 REAL,
    fvc REAL,
    pef REAL,
    spo2 REAL,
    diagnosis TEXT,
    FOREIGN KEY(patient_id) REFERENCES patients(patient_id)
)
""")

# Create Symptoms Table
cur.execute("""
CREATE TABLE IF NOT EXISTS symptoms (
    symptom_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE
)
""")

# Create Patient Symptoms Table
cur.execute("""
CREATE TABLE IF NOT EXISTS patient_symptoms (
    patient_id INTEGER,
    symptom_id INTEGER,
    symptom_date DATE,
    FOREIGN KEY(patient_id) REFERENCES patients(patient_id),
    FOREIGN KEY(symptom_id) REFERENCES symptoms(symptom_id)
)
""")

# --- Insert Sample Data ---
# Patients
patients_data = [
    ("Lebo Tangu", 19, "Male", "Calgary", "No"),
    ("Janet Mokoena", 22, "Female", "Calgary", "Past"),
    ("Sizwe Dlamini", 25, "Male", "Edmonton", "Yes")
]

cur.executemany("""
INSERT INTO patients (full_name, age, gender, region, smoking_status)
VALUES (?, ?, ?, ?, ?)
""", patients_data)

# Symptoms
symptom_list = ["cough", "shortness of breath", "chest tightness", "fatigue"]
for symptom in symptom_list:
    cur.execute("INSERT OR IGNORE INTO symptoms (name) VALUES (?)", (symptom,))

# Patient Symptoms
patient_symptoms_data = [
    (1, 1, "2025-07-20"),  # Lebo - cough
    (1, 2, "2025-07-20"),  # Lebo - shortness of breath
    (2, 3, "2025-07-18"),  # Janet - chest tightness
    (3, 1, "2025-07-15")   # Sizwe - cough
]
cur.executemany("""
INSERT INTO patient_symptoms (patient_id, symptom_id, symptom_date)
VALUES (?, ?, ?)
""", patient_symptoms_data)

# Lung Test Results
lung_tests_data = [
    (1, "2025-07-21", 2.8, 3.4, 400, 95, "Asthma"),
    (2, "2025-07-20", 3.1, 3.6, 420, 96, "Healthy"),
    (3, "2025-07-19", 1.9, 2.5, 300, 90, "COPD")
]
cur.executemany("""
INSERT INTO lung_tests (patient_id, test_date, fev1, fvc, pef, spo2, diagnosis)
VALUES (?, ?, ?, ?, ?, ?, ?)
""", lung_tests_data)

conn.commit()

# --- Example Queries ---
print("\n🔍 Patients with shortness of breath:")
cur.execute("""
SELECT p.full_name, ps.symptom_date
FROM patients p
JOIN patient_symptoms ps ON p.patient_id = ps.patient_id
JOIN symptoms s ON ps.symptom_id = s.symptom_id
WHERE s.name = 'shortness of breath'
""")
for row in cur.fetchall():
    print(row)

print("\n📊 Average FEV1 by smoking status:")
cur.execute("""
SELECT p.smoking_status, ROUND(AVG(l.fev1), 2) as avg_fev1
FROM patients p
JOIN lung_tests l ON p.patient_id = l.patient_id
GROUP BY p.smoking_status
""")
for row in cur.fetchall():
    print(row)

print("\n🫁 Patients with SPO2 under 92%:")
cur.execute("""
SELECT p.full_name, l.test_date, l.spo2
FROM patients p
JOIN lung_tests l ON p.patient_id = l.patient_id
WHERE l.spo2 < 92
""")
for row in cur.fetchall():
    print(row)

conn.close()



