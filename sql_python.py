import sqlite3

conn = sqlite3.connect('sql_exam1.db')
conn.row_factory = sqlite3.Row
cursor = conn.cursor()


def execute_modify_query(_cursor, _conn, query, params) -> None:
    _cursor.execute(query, params)
    _conn.commit()


def execute_read_query(_cursor, query) -> list:
    _cursor.execute(query)
    _rows = _cursor.fetchall()
    _answer = []
    for _row in _rows:
        _answer.append(dict(_row))
    return _answer


# א:
print(execute_read_query(cursor, '''select * from movies;'''))

# ב I didn't understand if I needed to view all the information on found movies based on user input or just the title of those movies
movie_search: str = str(input("enter a movie:"))
result = (execute_read_query(cursor, f'''select movie_name from movies where movie_name like '%{movie_search}%' '''))
if result:
    print(result)
else:
    print("movies with that name are not in our library")

# ג:
movie_name = input("Enter movie name: ")
genre = input("Enter genre: ")
country = input("Enter country: ")
language = input("Enter language: ")
while True:
    year = int(input("Enter year: "))
    if year >= 2009:
        break
    print("Year must be 2009 or later.")

while True:
    revenue = float(input("Enter revenue: "))
    if revenue >= 0:
        break
    print("Revenue cannot be negative.")

execute_modify_query(cursor, conn, '''INSERT INTO movies (movie_name, genre, country, language,year,revenue) 
VALUES (?, ?, ?, ?, ? ,?);''', (movie_name, genre, country, language, year, revenue))

conn.close()
