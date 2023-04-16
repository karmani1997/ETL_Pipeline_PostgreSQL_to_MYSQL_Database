import pandas as pd
import json
import math

class Transformer:
	data = None
	def __init__(self, data: pd.DataFrame):
		"""
		This class transforms extracted data according to the desired model

		Args:
		    raw_data: extracted data
		"""
		self.data = data



	# Calculate the distance between two locations using the provided formula
	def distance(self, lat1, lon1, lat2, lon2):
		return math.acos(math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * math.cos(lon1 - lon2)) * 6371

	def calculate_distance(self, x):
		x['latitude2'] = x['latitude1'].shift(1)
		x['longitude2'] = x['longitude1'].shift(1)
		x = x.fillna(0)
		return x.apply(lambda x: self.distance(x['latitude1'], x['longitude1'], x['latitude2'], x['longitude2']), axis = 1 ).sum()



	def transform_data(self):
		"""
		Transforms data

		Returns:
		    return the transformed data
		"""
		
		self.data['location'] = self.data['location'].apply(lambda x: json.loads(x))
		self.data[['latitude1', 'longitude1']] = self.data['location'].apply(lambda x: pd.Series([float(x['latitude']), float(x['longitude'])]))
		self.data = self.data.rename(columns={'latitude': 'latitude1', 'longitude': 'longitude1'})

		## convert the time into timestamp
		self.data['time'] = pd.to_datetime(self.data['time'], unit='s')
		self.data = self.data.sort_values(['device_id', 'time'], ascending=[True, True])

		# Group the data by device_id and hour
		df_grouped = self.data.groupby([self.data["device_id"], self.data["time"].dt.floor("H")])

		# Calculate the maximum temperature for each device per hour
		max_temperatures = df_grouped["temperature"].max().reset_index()
		max_temperatures = max_temperatures.rename(columns={'temperature': 'max_temperature'})
		# Calculate the number of data points for each device per hour
		data_points = df_grouped["location"].count().reset_index()
		data_points = data_points.rename(columns={'location': 'covered_data_points'})

		# Calculate the total distance of device movement for each device per hour
		distance_moved = df_grouped.apply(lambda x: self.calculate_distance(x)).reset_index()
		distance_moved = distance_moved.rename(columns={0: 'distance_moved'})
		
		return (max_temperatures, data_points, distance_moved)
