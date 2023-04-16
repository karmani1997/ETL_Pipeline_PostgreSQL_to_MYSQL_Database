from os import environ
from time import sleep
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
import pandas as pd


def connect():
	try:

		psql_engine = create_engine(environ["POSTGRESQL_CS"], pool_pre_ping=True, pool_size=10)
		print('Connection to PostgresSQL successful.')
	
		return psql_engine
	
	except OperationalError:
		sleep(0.1)


class Extractor:
	"""
	This class loads data from the PostgreSQL database into the dataframe
	"""
	psql_engine = None
	data = None
	def __init__(self):

		self.psql_engine = create_engine(environ["POSTGRESQL_CS"], pool_pre_ping=True, pool_size=10)

	def extract_data(self):
		"""
		Load the data into the dataframe
		"""
		# write a SQL query to fetch the data
		query = "select * from devices"
		conn = self.psql_engine.connect()
		# use the read_sql function to read the data into a DataFrame
		try:
			data = pd.read_sql_query(query,conn)
		except:
			print ("Data is not extracted")

		conn.close()
		return data
	