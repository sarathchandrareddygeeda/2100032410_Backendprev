import mysql.connector

dbname = 'safertek'
user = 'root' 
password = 'Sarath@138'  
host = 'localhost'
port = 3306

try:
    conn = mysql.connector.connect(
        database=dbname,
        user=user,
        password=password,
        host=host,
        port=port
    )

    cur = conn.cursor()

    query_with_join = """
    SELECT l.location_id, l.street_address, l.city, l.state_province, c.country_name
    FROM locations l
    JOIN countries c ON l.country_id = c.country_id
    WHERE c.country_name = 'Canada'
    """

    cur.execute(query_with_join)
    print("Query with JOIN:")
    for row in cur.fetchall():
        print(row)

    query_without_join = """
    SELECT location_id, street_address, city, state_province,
        (SELECT country_name FROM countries WHERE countries.country_id = locations.country_id) AS country_name
    FROM locations
    WHERE country_id = 'CA';
    """

    cur.execute(query_without_join)
    print("\nQuery without JOIN:")
    for row in cur.fetchall():
        print(row)

except mysql.connector.Error as e:
    print(f"Error: {e}")
