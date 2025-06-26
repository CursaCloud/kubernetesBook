import os
import psycopg2
from flask import Flask, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Configuración de la base de datos
DB_HOST = os.getenv("POSTGRES_HOST", "postgres-service")
DB_NAME = os.getenv("POSTGRES_DB")
DB_USER = os.getenv("POSTGRES_USER")
DB_PASS = os.getenv("POSTGRES_PASSWORD")

def get_db_connection():
    return psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASS,
        host=DB_HOST
    )

@app.route('/')
def home():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, nombre, apellidos, email, telefono, fecha_registro FROM clientes;")
        clientes = cursor.fetchall()
        cursor.close()
        conn.close()
        return render_template("index.html", clientes=clientes)
    except Exception as e:
        return f"Error al conectar con la base de datos: {str(e)}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
