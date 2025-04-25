import psycopg2
import json

# Connection string
conn = psycopg2.connect("postgresql://postgres:Madhu#1269@db.hgaedxjvwwopsrhjzoqd.supabase.co:5432/postgres")

# Create cursor
cur = conn.cursor()

# SQL insert
cur.execute("""
    INSERT INTO card (sap, data)
    VALUES (%s, %s);
""", ('1234', json.dumps({})))

# Commit and close
conn.commit()
cur.close()
conn.close()
