import logging

# Create instance of logger
basic_logger = logging.getLogger("basic_logger")

# Create File handler
basic_handler = logging.FileHandler("info_logs.log")
basic_handler.setLevel(logging.INFO)

# Set porper format for file handler
basic_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# Add them to logger
basic_handler.setFormatter(basic_formatter)
basic_logger.addHandler(basic_handler)
