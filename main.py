from cnnClassifier import logger
from cnnClassifier.pipeline.data_ingestion_pipeline import Data_Ingestion_Pipleline
from cnnClassifier.pipeline.prepare_base_model import prepare_base_model_Pipleline
from cnnClassifier.pipeline.train_model import train_model_Pipleline
from cnnClassifier.pipeline.model_evaluate import Model_evaluation_pipeline


STAGE_NAME = "Data Ingestion stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = Data_Ingestion_Pipleline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = "Prepare Base Model"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = prepare_base_model_Pipleline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = "Training Model"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = train_model_Pipleline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME="Evaluate Model"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   obj=Model_evaluation_pipeline()
   obj.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
   logger.exception(e)
   raise e


