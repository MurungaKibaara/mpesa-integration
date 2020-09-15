'''Postgres Database connection model'''
import os
import psycopg2
from flask import jsonify

DB_URL = os.getenv('DATABASE')

def init_db():
    '''Connecting to the DB'''
    conn = psycopg2.connect(DB_URL)
    return conn

def create_tables():
    '''Function for creating tables in database'''
    conn = init_db()
    cur = conn.cursor()
    queries = tables()

    for query in queries:
        cur.execute(query)
        conn.commit()

def tables():
    '''Function to define the tables'''
    transactions = """CREATE TABLE IF NOT EXISTS transactions(
            transaction_id serial PRIMARY KEY NOT NULL,
            reciept_number character varying(1000) NOT NULL,
            amount character varying(1000) NOT NULL,
            phonenumber character varying(1000) NOT NULL,
            request_id character varying(1000) NOT NULL,
            """

    queries = [transactions]

    return queries