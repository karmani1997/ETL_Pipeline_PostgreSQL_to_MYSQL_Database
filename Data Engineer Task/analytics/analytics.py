from time import sleep
from extractor import Extractor
from transformer import Transformer
from loader import Loader

#from .loader import Loader


def run_etl():

    print('Waiting for the data generator... Mehtab')
    sleep(50)
    print('ETL Starting...')

    extractor = Extractor()
    transformer = Transformer(extractor.extract_data())
    max_temperatures, data_points, distance_moved = transformer.transform_data()
    loader = Loader()
    loader.load_data(max_temperatures, data_points, distance_moved)

if __name__ == "__main__":
	run_etl()
