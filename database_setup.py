"""MySQL database bootstrap for the Face Recognition System.

Keeps the original MySQL credentials and register_page/register schema used by
this project. If the database/table already exists, nothing is changed.
"""
import mysql.connector
from mysql.connector import Error

DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "Maneesh@2006"
DB_NAME = "register_page"


def ensure_database():
    """Create the login database/table if they do not already exist."""
    conn = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
    )
    cur = conn.cursor()
    cur.execute(f"CREATE DATABASE IF NOT EXISTS `{DB_NAME}`")
    cur.close()
    conn.close()

    conn = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
    )
    cur = conn.cursor()
    cur.execute(
        """CREATE TABLE IF NOT EXISTS register (
            id INT AUTO_INCREMENT PRIMARY KEY,
            fname VARCHAR(100) NOT NULL,
            lname VARCHAR(100) NOT NULL,
            contact VARCHAR(30),
            email VARCHAR(150) NOT NULL UNIQUE,
            securityQ VARCHAR(255),
            securityA VARCHAR(255),
            password VARCHAR(255) NOT NULL
        )"""
    )
    conn.commit()
    cur.close()
    conn.close()


def get_connection():
    """Return a connection to the existing project database."""
    ensure_database()
    return mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
    )
