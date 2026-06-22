from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.Exception_handling.exception import CustomException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig
import sys

if __name__=="__main__":
    try:
        training_config=TrainingPipelineConfig()
        data_ingestion_config=DataIngestionConfig(training_config)
        data_ingestion=DataIngestion(data_ingestion_config)
        logging.info("Initiate data inegstion")
        dataingestionartifact=data_ingestion.initiate_data_ingestion()
        print(dataingestionartifact)

    except Exception as e:
        raise CustomException(e,sys)

