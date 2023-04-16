from extractor import Extractor
#from loader import Loader
#from transformer import Transformer
from time import sleep

def run_etl():
    extractor = Extractor()
    extractor.extract_data()   
 
	#transformer = Transformer(extractor.extract_data())
	#loader = Loader(transformer.transform_data())

	#loader.load_data()

if __name__ == "__main__":
    while True:
        print('Waiting for the data generator...')
        sleep(40)
        print('ETL Starting...')
        run_etl()