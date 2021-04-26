import psycopg2
from config import config

def insert_data():
    commands = """
        INSERT INTO workers (name, salary, joined_date, department) 
        VALUES
            ('Mark','5000', '2022-07-30', 'Human Resources'),
            ('Ben','12000', '2009-11-24', 'Marketing'),
            ('Elizabeth','9700', '2016-08-01', 'Sales'),
            ('Jack','7000', '2018-12-12', 'Finance');

        """

    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(commands)
        cur.close()
        conn.commit()
    except Exception as e:
        print(str(e))
    if conn is not None:
        conn.close()

insert_data()