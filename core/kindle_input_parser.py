import sqlite3
import sys
import os
import config

DB_FILE_PATH = config.Constants.DB_FILE_PATH


class Kindle:
    def __init__(self):
        """
        Attempt to connect to the given SQLite database file.

        Raises:
            SystemExit: If the SQLite database file does not exist at the specified path.
        """
        if not os.path.exists(DB_FILE_PATH):
            print(f"Required Kindle DB file not found at location: {DB_FILE_PATH}")
            sys.exit(0)

        try:
            self.conn = sqlite3.connect(DB_FILE_PATH)
            print("Connection successful.")
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")
            print(f"Location: {DB_FILE_PATH}")
            sys.exit(0)

    def init_cursor(self):
        """
        Create and return the cursor for the relevant SQLite database file.

        Returns:
            sqlite3.Cursor: A cursor for interacting with the SQLite database.
        """
        return self.conn.cursor()

    def query(self):
        """
        Extract and return a list of word and usage pairs from the Kindle DB.

        Raises:
            SystemExit: If there is an error executing the database query.

        Returns:
            list: A list containing pairs of words and their usage extracted from the database.
        """
        cursor = self.init_cursor()
        kindle_export = []

        try:
            for row in cursor.execute(
                'SELECT word_key, usage FROM "main"."LOOKUPS" LIMIT 5;'
            ):
                word = row[0].replace("en:", "")
                usage = row[1]
                kindle_export.append([word, usage])
        except Exception as e:
            print(f"Error querying database: {e}")
            print(f"Location: {DB_FILE_PATH}")
            sys.exit(0)

        cursor.close()
        self.close_connection()
        return kindle_export

    def close_connection(self):
        """
        Close the connection to the database.

        Returns:
            None
        """
        if self.conn:
            self.conn.close()
            print("DB connection closed.")
