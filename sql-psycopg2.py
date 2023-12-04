import psycopg2

# connect to "chinook" database
connection = psycopg2.connect(database="chinook")

# build a cursor object of the database
cursor = connection.cursor()

# Query 1 - select all recoreds from the "Artist" table
cursor.execute('SELECT * FROM "Artist"')

# Query 2 - select "Name" column from "Artist" table
cursor.execute('SELECT "Name" FROM "Artist"')

# Query 3 - select only "Queen" from the "Artist" table
cursor.execute('SELECT * FROM "Artist" WHERE "Name"= %s', ["Queen"])

# Query 4 = select only by "ArtistId" #51 from the "Artist table"
cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', [51])

# Query 5 - select only the albums with "ArtistsId" #51 on the "Album" table
cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" =  %s', [51])

# Query 6 - select all tracks where the composer is "Queen" from the "Track" table
cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Queen"])

# Query 7 select all albums where the composer is "AC/DC"
cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["AC/DC"])

# Query 7 select all albums where the composer is "AC/DC"
cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["TEST"])

# fetch single result
# results = cursor.fetchone()

# fetch the results (multiple)
results = cursor.fetchall()

# close connection
connection.close()

for result in results:
    print(result)