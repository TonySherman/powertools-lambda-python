from aws_lambda_powertools import Logger
from aws_lambda_powertools.utilities.typing import LambdaContext

logger = Logger()


def handler(event: dict, context: LambdaContext) -> str:
    fields = {"request_id": "1123"}
    logger.info("Collecting payment", extra=fields)

    return "hello world"
