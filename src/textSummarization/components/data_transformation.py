import os
from textSummarization.logging import logger
from transformers import AutoTokenizer
from datasets import load_dataset, load_from_disk
from textSummarization.entity import DataTransformationConfig

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
        self.tokenizer = AutoTokenizer.from_pretrained(config.tokenizer_name)

    def convert_examples_to_features(self, example_batch):
        input_encodings = self.tokenizer(example_batch['dialogue'], max_length=1024, truncation=True)
        
        with self.tokenizer.as_target_tokenizer():
            target_encodings = self.tokenizer(example_batch['summary'], max_length=128, truncation=True)
            
        return {
            'input_ids': input_encodings['input_ids'],
            'attention_mask': input_encodings['attention_mask'],
            'labels': target_encodings['input_ids']
        }

    def convert(self):
        logger.info(f"Checking if the data path {self.config.data_path} exists.")
        # Check if the data path exists
        if not os.path.exists(self.config.data_path):
            raise FileNotFoundError(f"The data path {self.config.data_path} does not exist.")
        
        logger.info(f"Loading dataset from {self.config.data_path}.")
        dataset_samsum = load_from_disk(self.config.data_path)
        
        logger.info("Mapping dataset to features.")
        dataset_samsum_pt = dataset_samsum.map(self.convert_examples_to_features, batched=True)
        
        save_path = os.path.join(self.config.root_dir, "samsum_dataset")
        logger.info(f"Ensuring the save path directory {save_path} exists.")
        # Ensure the save path directory exists
        os.makedirs(save_path, exist_ok=True)
        
        logger.info(f"Saving processed dataset to {save_path}.")
        try:
            dataset_samsum_pt.save_to_disk(save_path)
            logger.info("Dataset saved successfully.")
        except OSError as e:
            logger.error(f"Failed to save dataset to {save_path}: {e}")
            raise