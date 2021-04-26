import psycopg2
from config import config

def create_tables():
    commands = """
        CREATE TABLE workers (
            worker_id serial PRIMARY KEY,
            name VARCHAR NOT NULL,
            salary INT NOT NULL,
            joined_date DATE NOT NULL,
            department TEXT
        );
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

create_tables()