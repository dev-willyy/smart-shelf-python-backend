import logging

logger = logging.getLogger("smart_shelf")
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
formatter = logging.Formatter("[%(levelname)s] %(asctime)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)
