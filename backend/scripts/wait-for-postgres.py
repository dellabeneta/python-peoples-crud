#!/usr/bin/env python3
import psycopg2
import time
import os
import sys
from urllib.parse import urlparse

def wait_for_postgres():
    # Get database URL from environment
    db_url = os.getenv('DATABASE_URL')
    if not db_url:
        print("ERROR: DATABASE_URL environment variable is not set")
        return False

    print(f"Connecting to database URL: {db_url}")

    # Parse the URL to get connection parameters
    parsed = urlparse(db_url)
    dbname = parsed.path[1:]  # Remove leading slash
    user = parsed.username
    password = parsed.password
    host = parsed.hostname
    port = parsed.port

    print(f"Parsed connection parameters:")
    print(f"- Host: {host}")
    print(f"- Port: {port}")
    print(f"- Database: {dbname}")
    print(f"- User: {user}")

    max_retries = 30  # Maximum number of retries
    retry_interval = 2  # Seconds between retries

    for i in range(max_retries):
        try:
            print(f"\nAttempt {i + 1}/{max_retries} to connect to PostgreSQL...")
            conn = psycopg2.connect(
                dbname=dbname,
                user=user,
                password=password,
                host=host,
                port=port
            )
            conn.close()
            print("Successfully connected to PostgreSQL!")
            return True
        except psycopg2.OperationalError as e:
            print(f"Failed to connect: {e}")
            if i < max_retries - 1:
                print(f"Waiting {retry_interval} seconds before next attempt...")
                time.sleep(retry_interval)
            else:
                print("ERROR: Max retries reached. Could not connect to PostgreSQL.")
                return False

if __name__ == "__main__":
    success = wait_for_postgres()
    if not success:
        sys.exit(1)  # Exit with error code if connection failed
    sys.exit(0)  # Exit with success code if connection succeeded
