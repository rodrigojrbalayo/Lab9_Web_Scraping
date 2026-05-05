cursor.execute("INSERT INTO students (name, course) VALUES (?, ?)", (name, course))

conn = sqlite3.connect("school.db")
cursor = conn.cursor()
try:
    cursor.execute("UPDATE students SET course = ? WHERE id = ?", ("BSCE", 2))
    conn.commit()
except:
    conn.rollback()

with sqlite3.connect("school.db") as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")

    return redirect(url_for('students'))

