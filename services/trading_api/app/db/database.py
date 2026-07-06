import os

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost:5432/tradingdb")


def get_database_url():
    return DATABASE_URL