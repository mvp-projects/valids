"""Run rust librabry."""
import _valids_rs

from valids.logging import logger

if __name__ == "__main__":
    sum_result = _valids_rs.sum_as_string(a=10, b=14)
    logger.info(sum_result)
    logger.info(type(sum_result))
