from sqlalchemy import create_engine

engine = create_engine("postgresql://kay:postgres@127.0.0.1:5432/fabirlic")


with engine.connect() as con:
  print(con)

# # default
# engine = create_engine("postgresql://scott:tiger@localhost/mydatabase")

# # psycopg2
# engine = create_engine("postgresql+psycopg2://scott:tiger@localhost/mydatabase")

# # pg8000
# engine = create_engine("postgresql+pg8000://scott:tiger@localhost/mydatabase")