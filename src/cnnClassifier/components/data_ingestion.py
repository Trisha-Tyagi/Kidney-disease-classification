import os
import gdown
from cnnClassifier import logger
import zipfile
from cnnClassifier.utils.common import get_size
from cnnClassifier.entity.entity_data_ingestion import DataIngestionConfig


class  DataIngestion:
    def __init__ (self, config :DataIngestionConfig):
        self.config=config

    def download_data(self):
            
            '''
            fetch data using url
            '''
            try:  
                url=self.config.source_URL
                zip_folder_dir=self.config.local_data_file
                os.makedirs("artifacts/data_ingestion",exist_ok=True)
                logger.info(f"Downloading data from {url} to {zip_folder_dir}")

                gdown.download(
                    url=self.config.source_URL,
                    output=zip_folder_dir,
                    quiet=False,
                    fuzzy=True
                )
                logger.info(f"Downloading data from {url} to {zip_folder_dir}")

            except Exception as e:
                 raise e

    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
        
        