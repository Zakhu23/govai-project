import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Zakhu@123",
    database="gov_ai_system"
)

cursor = conn.cursor()

print("===== Government AI System =====")

# User Inputs
age = int(input("Enter your age: "))
income = float(input("Enter your annual income: "))
occupation = input("Enter your occupation: ").lower()
state = input("Enter your state: ").lower()
qualification = input("Enter your qualification (12th Pass / Graduate): ").lower()

print("\n===== Eligible Schemes =====\n")

# SQL Query (IMPORTANT FIXED VERSION)
query = """
SELECT scheme_name, description, apply_link 
FROM schemes
WHERE 
    %s BETWEEN min_age AND max_age
    AND (%s <= max_income OR max_income IS NULL)
    AND (LOWER(occupation) = %s OR occupation = 'Any')
    AND (LOWER(state) = %s OR state = 'All States')
"""

cursor.execute(query, (age, income, occupation, state))

results = cursor.fetchall()

# Output
if results:
    for row in results:
        print("Scheme:", row[0])
        print("Description:", row[1])
        print("Apply Link:", row[2])
        print("---------------------------")
else:
    print("No schemes found for your eligibility.")

# Close connection
conn.close()