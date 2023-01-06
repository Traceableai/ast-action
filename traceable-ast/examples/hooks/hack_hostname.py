from traceable.ast.context import ScanContext
from traceable.ast.testsuite import AttributeList
from traceable.ast.testsuite.assertion import Assertion
from traceable.config import logger


def hack_hostname(ctx: ScanContext, attributes: AttributeList) -> list[Assertion]:
    logger.info("Hacking hostname through hook")
    attributes.set("mutated.net.host.name", "expired.badssl.com")
    return []
