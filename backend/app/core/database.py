from neo4j import GraphDatabase
from backend.app.core.config import settings


class Database:
    def __init__(self):
        self.driver = None
        self.connect()

    def connect(self):
        """
        Create a new CognoDB / Neo4j driver connection.
        """

        try:
            self.driver = GraphDatabase.driver(
                settings.cognodb_uri,
                auth=(
                    settings.cognodb_username,
                    settings.cognodb_password
                ),
                max_connection_lifetime=300,
                connection_timeout=30,
                max_connection_pool_size=50,
            )

            print("CognoDB driver initialized successfully.")

        except Exception as e:
            print("Failed to initialize CognoDB driver.")
            print(f"Error: {repr(e)}")
            raise

    def get_session(self):
        """
        Return a fresh database session.
        """

        if self.driver is None:
            self.connect()

        return self.driver.session()

    def close(self):
        """
        Close the database driver.
        """

        if self.driver:
            self.driver.close()
            self.driver = None

    def verify_connection(self):
        """
        Verify that the database connection is active.
        """

        try:
            if self.driver is None:
                self.connect()

            self.driver.verify_connectivity()

            print(
                "CognoDB connectivity verified successfully."
            )

        except Exception as e:
            print(
                "CognoDB connectivity verification failed."
            )

            print(f"Error: {repr(e)}")

            raise


db = Database()