import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS schemes")

cursor.execute("""
CREATE TABLE schemes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    description TEXT,
    type TEXT,
    min_age INTEGER,
    max_age INTEGER,
    income REAL,
    occupation TEXT,
    state TEXT,
    qualification TEXT,
    apply_link TEXT
)
""")

cursor.executemany("""
INSERT INTO schemes 
(name, description, type, min_age, max_age, income, occupation, state, qualification, apply_link)
VALUES (?,?,?,?,?,?,?,?,?,?)
""", [

# ===== SCHEMES =====
('PM Kisan', 'Farmer income support', 'scheme', 18, 60, None, 'farmer', 'all states', 'any', 'https://pmkisan.gov.in'),
('Ayushman Bharat', 'Health scheme', 'scheme', 0, 100, 300000, 'any', 'all states', 'any', 'https://pmjay.gov.in'),
('NSP Scholarship', 'Student scholarship', 'scheme', 15, 30, 250000, 'student', 'all states', '12th pass', 'https://scholarships.gov.in'),
('PM Awas Yojana', 'Housing scheme', 'scheme', 18, 60, 300000, 'any', 'all states', 'any', 'https://pmaymis.gov.in'),
('Skill India', 'Skill development', 'scheme', 18, 35, None, 'any', 'all states', 'any', 'https://skillindia.gov.in'),

('YSR Rythu Bharosa', 'AP farmer scheme', 'scheme', 18, 60, 500000, 'farmer', 'andhra pradesh', 'any', 'https://ysrrythubharosa.ap.gov.in'),
('Rythu Bandhu', 'Telangana farmer scheme', 'scheme', 18, 60, None, 'farmer', 'telangana', 'any', 'https://rythubandhu.telangana.gov.in'),
('UP Scholarship', 'UP scholarship', 'scheme', 15, 30, 200000, 'student', 'uttar pradesh', '12th pass', 'https://scholarship.up.gov.in'),

# ===== EXAMS =====
('UPSC Civil Services', 'IAS IPS exam', 'exam', 21, 32, None, 'any', 'all states', 'graduate', 'https://upsc.gov.in'),
('UPSC NDA', 'Defence exam', 'exam', 16, 19, None, 'student', 'all states', '12th pass', 'https://upsc.gov.in'),
('SSC CGL', 'Graduate exam', 'exam', 18, 32, None, 'any', 'all states', 'graduate', 'https://ssc.nic.in'),
('SSC CHSL', '12th exam', 'exam', 18, 27, None, 'student', 'all states', '12th pass', 'https://ssc.nic.in'),
('SSC GD', 'Constable exam', 'exam', 18, 23, None, 'any', 'all states', '10th pass', 'https://ssc.nic.in'),

('RRB NTPC', 'Railway exam', 'exam', 18, 33, None, 'any', 'all states', '12th pass', 'https://rrbcdg.gov.in'),
('RRB Group D', 'Railway jobs', 'exam', 18, 33, None, 'any', 'all states', '10th pass', 'https://rrbcdg.gov.in'),

('IBPS PO', 'Bank PO exam', 'exam', 20, 30, None, 'graduate', 'all states', 'graduate', 'https://ibps.in'),
('IBPS Clerk', 'Bank clerk', 'exam', 20, 28, None, 'graduate', 'all states', 'graduate', 'https://ibps.in'),
('SBI PO', 'SBI officer', 'exam', 21, 30, None, 'graduate', 'all states', 'graduate', 'https://sbi.co.in'),

('AFCAT', 'Air Force exam', 'exam', 20, 24, None, 'graduate', 'all states', 'graduate', 'https://afcat.cdac.in'),
('Indian Army Agniveer', 'Army recruitment', 'exam', 17, 23, None, 'any', 'all states', '10th pass', 'https://joinindianarmy.nic.in'),

('CTET', 'Teacher exam', 'exam', 18, 35, None, 'graduate', 'all states', 'graduate', 'https://ctet.nic.in'),
('State Police SI', 'Police exam', 'exam', 20, 28, None, 'graduate', 'all states', 'graduate', 'https://police.gov.in')

])

conn.commit()
conn.close()

print("✅ Database with 24+ records created")