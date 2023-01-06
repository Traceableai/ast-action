import base64
import html
import json
import os
import random
import re
import string
import time
import jwt
import urllib.parse
import requests
from traceable.ast.context import ScanContext, PluginContext
from traceable.ast.testsuite import AttributeList
from traceable.ast.testsuite.assertion import Assertion
from traceable.config import logger


def sample_using_plugin_ctx(scanctx: ScanContext, pluginctx: PluginContext, attributes: AttributeList) -> list[Assertion]:
    plugin_name = pluginctx.get_plugin()
    logger.info("Plugin name: %s" % plugin_name)
    category = pluginctx.get_category()
    logger.info("Category: %s" % category)
    api_name = pluginctx.get_api_name()
    logger.info("API name: %s" % api_name)
    api_id = pluginctx.get_api_id()
    logger.info("API id: %s" % api_id)
    service_name = pluginctx.get_service_name()
    logger.info("Service name: %s" % service_name)
    service_id = pluginctx.get_service_id()
    logger.info("Service id: %s" % service_id)
    enviroment_name = pluginctx.get_environment_name()
    logger.info("Environment name: %s" % enviroment_name)


def sample_crapi_login_posthook(scanctx: ScanContext, pluginctx: PluginContext, attributes: AttributeList) -> list[Assertion]:
    res_code = int(attributes.get_one("mutated.http.response.code", 0))
    # err_code = attributes.get_one("mutated.http.response.json.error", "")
    if res_code == 401 and scanctx["crapi_token"]:
        del scanctx["crapi_token"]
    return []


def sample_crapi_login_prehook(scanctx: ScanContext, pluginctx: PluginContext, attributes: AttributeList) -> list[Assertion]:
    url = urllib.parse.urlparse(
        attributes.get_one("original.http.request.url", ""))
    logger.info("Attempting login to CRAPI")
    if scanctx.get("crapi_user", None) is None and scanctx.get("crapi_token", None) is None:
        # Register:
        u = urllib.parse.urlunparse(
            url._replace(path="/identity/api/auth/signup"))
        email = "".join(random.sample(
            string.ascii_lowercase, k=10)) + "@not-traceable.ai"
        phone = "".join(random.sample(string.digits, k=10))
        res = requests.post(u, json={
            "name": "John Doe",
            "email": email,
            "number": phone,
            "password": "Traceable1!"
        }, headers={
            "content-type": "application/json"
        })
        if res.status_code == 200:
            scanctx["crapi_user"] = email
            logger.info("CRAPI user successfully created, email %s" % email)
        else:
            logger.error("Failed to create crapi user, got status %d and body: %s" % (
                res.status_code, res.json()))
        # if error, probably used already registered
    if scanctx.get("crapi_token", None) is None:
        # Login:
        u = urllib.parse.urlunparse(
            url._replace(path="/identity/api/auth/login"))
        res = requests.post(u, json={
            "email": scanctx.get("crapi_user", "juan@not-traceable.ai"),
            "password": "Traceable1!"
        }, headers={
            "content-type": "application/json"
        })
        if res.status_code != 200:
            logger.error("Failed to login to crapi, got status %d" %
                         res.status_code)
            return []

        res = res.json()
        scanctx["crapi_token"] = res["token"]
        logger.info("got crapi_token: %s" % scanctx["crapi_token"])
    else:
        logger.info("Already logged in to CRAPI")
    attributes.set("mutated.http.request.header.authorization",
                   "Bearer %s" % scanctx["crapi_token"])
    return []


def sample_traceable_refresh_login_prehook(scanctx: ScanContext, pluginctx: PluginContext, attributes: AttributeList) -> list[Assertion]:
    session = scanctx.get("traceable_session", None)
    token = attributes.get_one(
        "mutated.http.request.cookies.jwt", "")
    if len(token) > 0:
        payload = token.split(".")[1]
        b64decoded = str(base64.decodebytes(payload.encode("utf-8")))
        logger.debug("Got payload: %s" % b64decoded)
        jsdecoded = json.loads(b64decoded)
        logger.debug("Got json: %s" % jsdecoded)
        exp = jsdecoded["exp"]
        # if exp is in the past, we need to login again
        if exp < int(time.time()):
            logger.info("Token expired, refresh token")
        return []


def sample_traceable_login_prehook(scanctx: ScanContext, pluginctx: PluginContext, attributes: AttributeList) -> list[Assertion]:
    session = scanctx.get("traceable_session", None)
    if session is not None:
        logger.info("Already logged in to Traceable")
        for cookie in session.cookies:
            attributes.set("mutated.http.request.cookies.%s" % (cookie.name), cookie.value)
        return []
    session = scanctx["traceable_session"] = requests.Session()
    USERNAME = os.environ.get("TRACEABLE_EMAIL", "")
    PASSWORD = os.environ.get("TRACEABLE_PASSWORD", "")
    if USERNAME == "" or PASSWORD == "":
        logger.error("Missing TRACEABLE_EMAIL or TRACEABLE_PASSWORD. Cannot login")
        return []
    # First we get the cookies:
    res = session.get('https://app.traceable.ai/login?redirect=https%3A%2F%2Fapp%2Etraceable%2Eai%2F', allow_redirects=True)
    if not res.status_code == 200:
        logger.error("Failed to get cookies, got status %d" %
                     res.status_code)
        return []
    # we login
    logger.info("Attempting Traceable.ai login with username %s" % USERNAME)
    body = res.text
    rx = re.compile(r'escape\(window\.atob\(\'(.*?)\'\)')
    config = rx.search(body)
    if config is None:
        logger.error("Failed to get config, got body: %s" % body)
        return []
    try:
        config = config.group(1)
        # base64 decode config
        # FROM https://auth.traceable.ai/login?state=...
        config = base64.b64decode(config).decode("utf-8")
        config = json.loads(config)
    except BaseException:
        logger.error("Failed to decode config, got body: %s" % config.group(1))
        return []
    client_id = config["clientID"]
    state = config["extraParams"]["state"]
    csrf_token = config["extraParams"]["_csrf"]

    # res = session.post("https://auth.traceable.ai/usernamepassword/challenge", json={
    #     "state": state
    # })
    # res = session.get("https://auth.traceable.ai/user/ssodata")

    res = session.post("https://auth.traceable.ai/usernamepassword/login", json={
        "client_id": client_id,
        "redirect_uri": "https://app.traceable.ai/callback",
        "tenant": "traceable",
        "response_type": "code",
        "scope": "openid profile email",
        "state": state,
        "connection": "Username-Password-Authentication",
        "username": USERNAME,
        "password": PASSWORD,
        "popup_options": {},
        "sso": True,
        "_intstate": "deprecated",
        "_csrf": csrf_token,
        "email_hint": "",
        "organization_hint": "",
        "action": "",
        "protocol": "oauth2"
    }, headers={
        "content-type": "application/json"
    }
    )
    if res.status_code != 200:
        logger.error("Failed to login to traceable, got status %d" %
                     res.status_code)
        return []
    callbackdata = res.text
    rx = re.compile(r'value="(.*?)"', re.MULTILINE)
    fields = rx.findall(callbackdata)
    cookies = ";".join(["%s=%s" % (cookie.name, cookie.value) for cookie in session.cookies])

    res = session.post("https://auth.traceable.ai/login/callback", headers={
        "content-type": "application/x-www-form-urlencoded",
        "origin": "https://auth.traceable.ai",
        "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:101.0) Gecko/20100101 Firefox/101.0',
        "Accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        "Cookie": cookies
    }, data={
        "wa": "wsignin1.0",
        "wresult": fields[1],
        "wctx": html.unescape(fields[2]),
    },
        allow_redirects=True
    )
    for cookie in session.cookies:
        attributes.set("mutated.http.request.cookies.%s" % (cookie.name), cookie.value)
    scanctx["traceable_session"] = session
    return []
