import sqlite3

connection = sqlite3.connect("tech_database.db")

cursor = connection.cursor()

#cursor.execute("""CREATE TABLE techs
#                    (name text, nation text, year int, description text)""")
#
#cursor.execute("INSERT INTO techs VALUES ('Short Magazine Lee Enfield Rifle Mk. III', 'england', 1907, 'Short Magazine Lee Enfield Rifle description')")
#
## save data to database
#connection.commit()
#
## insert multiple records using the more secure "?" method
#techs = [('Vickers Machine Gun', 'england', 1912, 'Vickers Machine Gun description'),
#          ('M1917 Enfield Rifle', 'england', 1914, 'M1917 Enfield Rifle description'),
#          ('Bren Light Machine Gun', 'england', 1935, 'Bren Light Machine Gun description'),
#          ('No. 4 Mk I Rifle', 'england', 1939, 'No. 4 Mk I Rifle description'),
#          ('Gewehr 98', 'germany', 1898, 'Gewehr 98 description'),
#          ('Karabiner 98k', 'germany', 1935, 'Karabiner 98k description'),
#          ('Maschinengewehr 08', 'germany', 1908, 'Maschinengewehr 08 description')]
#cursor.executemany("INSERT INTO techs VALUES (?,?,?,?)", techs)
#connection.commit()

print "\nGerman Techs:"
sql = "SELECT name FROM techs WHERE nation=?"
for row in cursor.execute(sql, [("germany")]):
    print row  # or use fetchone()

print "\nGerman Techs by date:"
sql = "SELECT name FROM techs WHERE nation=? ORDER BY year"
for row in cursor.execute(sql, [("germany")]):
    print row  # or use fetchone()

print "\nTechs by nation:"
for row in cursor.execute("SELECT rowid, * FROM techs ORDER BY nation"):
    print row

print "\nResults from a LIKE query on Rifles:"
sql = """
SELECT * FROM techs
WHERE name LIKE '%Rifle'"""
cursor.execute(sql)
print cursor.fetchall()