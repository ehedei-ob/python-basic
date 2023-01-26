import sqlite3

conn = sqlite3.connect('db-alumnos.db')
cursor = conn.cursor()

cursor.execute('DROP TABLE IF EXISTS alumnos')
cursor.execute('CREATE TABLE alumnos(id INT primary key, nombre TEXT, apellido TEXT)')

students = []
for i in range(1, 10):
    students.append([i, f'Alumno {i}', f'Apellidos {i}'])

cursor.executemany('INSERT INTO alumnos VALUES(?, ?, ?)', students)
conn.commit()

cursor.execute('SELECT * FROM alumnos WHERE nombre = ?', ['Alumno 5'])
rows = cursor.fetchall()

print(rows)

cursor.close()
conn.close()