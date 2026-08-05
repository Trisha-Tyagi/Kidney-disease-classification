from cnnClassifier import logger
from cnnClassifier.pipeline.data_ingestion_pipeline import Data_Ingestion_Pipleline


STAGE_NAME = "Data Ingestion stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = Data_Ingestion_Pipleline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e