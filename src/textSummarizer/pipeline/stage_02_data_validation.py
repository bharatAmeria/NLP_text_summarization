from src.textSummarizer.components.data_validation import DataValidation
from src.textSummarizer.config.configuration import ConfigurationManager


class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    @staticmethod
    def main():
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_all_files_exist()
