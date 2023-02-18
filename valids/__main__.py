from valids.calculations import get_value_of_pi
from valids.logging import logger
import _valids_rs


if __name__ == "__main__":
    logger.info(_valids_rs.get_value_of_pi(n=10_000_000))
