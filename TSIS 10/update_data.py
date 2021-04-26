import psycopg2
from config import config

def insert_data():
    commands = """
        UPDATE workers
        SET joined_date = '2020-07-02'
        WHERE worker_id = 2
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