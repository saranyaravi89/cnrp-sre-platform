import logging
from pythonjsonlogger import jsonlogger
from pathlib import Path


def get_logger():
    logger = logging.getLogger("trading-api")
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        log_dir = Path("/app/app/logs")
        log_dir.mkdir(parents=True, exist_ok=True)

        formatter = jsonlogger.JsonFormatter(
            "%(asctime)s %(levelname)s %(name)s %(message)s"
        )

        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)

        file_handler = logging.FileHandler("/app/app/logs/trading-api.log")
        file_handler.setFormatter(formatter)

        logger.addHandler(stream_handler)
        logger.addHandler(file_handler)

    return logger
