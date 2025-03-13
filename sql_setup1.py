from llama_index.core import SQLDatabase, Settings
from llama_index.llms.openai import OpenAI
from llama_index.core.query_engine import NLSQLTableQueryEngine
from sqlalchemy import insert
from sqlalchemy import inspect
from sqlalchemy import (
    create_engine,
    MetaData,
    Table,
    Column,
    String,
    Integer,
)

import os
from dotenv import load_dotenv
load_dotenv()

os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')
#os.environ['LANGSMITH_API_KEY'] = os.getenv('LANGSMITH_API_KEY')

Settings.llm = OpenAI(model="gpt-3.5-turbo")


#engine = create_engine("sqlite:///:memory:", future=True)
engine = create_engine("sqlite:///city_stats.db", future=True)
metadata_obj = MetaData()

# create city SQL table
table_name = "city_stats"
city_stats_table = Table(
    table_name,
    metadata_obj,
    Column("city_name", String(16), primary_key=True),
    Column("population", Integer),
    Column("state", String(16), nullable=False),
)

# Check if the table already exists
inspector = inspect(engine)
table_exists = inspector.has_table(table_name)

if not table_exists:
    # Create the table only if it doesn't exist
    metadata_obj.create_all(engine)

    # Insert initial data
    rows = [
        {"city_name": "New York City", "population": 8336000, "state": "New York"},
        {"city_name": "Los Angeles", "population": 3822000, "state": "California"},
        {"city_name": "Chicago", "population": 2665000, "state": "Illinois"},
        {"city_name": "Houston", "population": 2303000, "state": "Texas"},
        {"city_name": "Miami", "population": 449514, "state": "Florida"},
        {"city_name": "Seattle", "population": 749256, "state": "Washington"},
    ]
    for row in rows:
        stmt = insert(city_stats_table).values(**row)
        with engine.begin() as connection:
            connection.execute(stmt)
    print("Database and table created with initial data.")
else:
    print("Database and table already exist. Skipping creation.")


sql_database = SQLDatabase(engine, include_tables=["city_stats"])
sql_query_engine = NLSQLTableQueryEngine(
    sql_database=sql_database,
    tables=["city_stats"]
)