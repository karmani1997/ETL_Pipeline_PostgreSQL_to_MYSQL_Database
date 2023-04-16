from os import environ
from time import sleep
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
import pandas as pd


def connect():
	try:

		mysql_engine = create_engine(environ["MYSQL_CS"], pool_pre_ping=True, pool_size=10)
		print('Connection to MySQL successful.')
	
		return mysql_engine
	
	except OperationalError:
		sleep(0.1)


class Loader:
	"""
	This class loads data into the MySQL database from the dataframe
	"""
	mysql_engine = None

	def __init__(self):

		self.mysql_engine = connect()

	def load_data(self, max_temperatures, data_points, distance_moved):
		"""
		Load the data into the MySQL Database
		"""
		max_temperatures.to_sql(name='device_max_temperatures_hourly', con=self.mysql_engine, if_exists='append', index=False)
		data_points.to_sql(name='device_data_points_hourly', con=self.mysql_engine, if_exists='append', index=False)
		distance_moved.to_sql(name='device_distance_moved_hourly', con=self.mysql_engine, if_exists='append', index=False)
		
		print ("Data dumped successfully.....")