import sqlite3

c = sqlite3.connect("db.sqlite3")
cursor = c.cursor()

Speciality = {
    'Anesthesiology',
    'Allergy and Immunology',
    'Cardiovascular Disease',
    'Dermatology',
    'Emergency Medicine',
    'Family Medicine',
    'Gastroenterology',
    'Geriatrics',
    'Hematology',
    'Infectious Disease',
    'Internal Medicine',
    'Medical Genetics',
    'Nephrology',
    'Neurology',
    'Nuclear Medicine',
    'Obstetrics and Gynecology',
    'Oncology',
    'Ophthalmology',
    'Orthopedic Surgery',
    'Otolaryngology (ENT)',
    'Pain Medicine',
    'Pathology',
    'Pediatrics',
    'Physical Medicine and Rehabilitation',
    'Plastic Surgery',
    'Preventive Medicine',
    'Psychiatry',
    'Pulmonology',
    'Radiology',
    'Rheumatology',
    'Sleep Medicine',
    'Sports Medicine',
    'Surgery',
    'Thoracic Surgery',
    'Urology',
    'Vascular Surgery',
    'Other',
}

# Verifica se cada especialidade já existe na tabela antes de inseri-la
for sp in Speciality:
    cursor.execute("SELECT * FROM recipes_speciality WHERE name = ?", (sp,))
    existing_specialty = cursor.fetchone()
    if not existing_specialty:
        cursor.execute("INSERT INTO recipes_speciality(name) VALUES(?)", (sp,))

c.commit()
c.close()