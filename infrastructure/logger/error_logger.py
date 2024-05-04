import logging

error_logger = logging.getLogger("error_logger")

# Create File handler
error_handler = logging.FileHandler("error_logs.log")
error_handler.setLevel(logging.INFO)

# Set porper format for file handler
error_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# Add them to logger
error_handler.setFormatter(error_formatter)
error_logger.addHandler(error_handler)
