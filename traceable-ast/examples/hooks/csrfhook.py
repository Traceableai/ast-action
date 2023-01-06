import os
import random
import string
import jwt
import urllib.parse

import requests
from traceable import ScanContext
from traceable.ast.testsuite import AttributeList
from traceable.ast.testsuite.assertion import Assertion
from traceable.config import logger


def remove_csrf_token_posthook(ctx: ScanContext, attributes: AttributeList) -> list[Assertion]:
    attributes.delete("mutated.http.request.header.crf_token")
    return [
        Assertion.create("MATCH_OPERATOR_EQUALS",
                         "original.http.response.code", "401"),
    ]


def set_csrf_token_prehook(ctx: ScanContext, attributes: AttributeList) -> list[Assertion]:
    if not ctx.get("csrf_token"):
        ctx.set("csrf_token", "".join(random.sample(string.ascii_lowercase, k=10)))
    attributes.set("mutated.http.request.header.crf_token", ctx.get("csrf_token"))
    return []
