"""
Collection of useful utility functions not necessarily related to any specific
object.
"""
# Standard
import logging
# Django
from django.conf import settings

from joplin.backends.gopher_backend import GopherBackend
from joplin.backends.jupiter_backend import JupiterRequestsBackend
from gopher import Gopher
import requests as res


def create_pub_rep_backend(via_jupiter=True):
    internal = settings.TPOZ_URL
    pubrep = settings.REP_TO_PUBREP_MAP.get(internal)
    logging.info("Internal: %s" % internal)
    logging.info("Pub: %s" % pubrep)
    if pubrep:
        return create_backend(use_jupiter=via_jupiter, url=pubrep, user=settings.TPOZ_ADMIN_USERNAME, passwd=settings.TPOZ_ADMIN_PASSWORD)
    logging.error(
        "Error Creating corresponding pubrep backend for -- %s" % internal)
    return False


def create_admin_backend(use_jupiter=True, url=settings.TPOZ_URL, user=settings.TPOZ_ADMIN_USERNAME, passwd=settings.TPOZ_ADMIN_PASSWORD):
    return create_backend(use_jupiter, url, user, passwd)


def create_backend(use_jupiter=True, url=settings.TPOZ_URL, user=settings.TPOZ_USERNAME, passwd=settings.TPOZ_PASSWORD):
    """Creates gopher or jupiter backend instance

    :return: gopher or jupiter backend
    """
    if use_jupiter:
        return create_jupiter_backend(url, user, passwd)
    gopher = Gopher(url)
    gopher.login(
        user,
        passwd
    )
    return GopherBackend(gopher)


def create_jupiter_backend(url=settings.TPOZ_URL, username=settings.TPOZ_USERNAME, passwd=settings.TPOZ_PASSWORD):
    s = res.Session()
    s.post("%s/system/login" % url,
           data={"username": username, "password": passwd})
    try:
        return JupiterRequestsBackend(s, settings.TPOZ_URL)
    except Exception as e:
        return None


def create_jupiter_user(user_to_check, role, backend, passwd='letmein'):
    logging.info("Backend: %s" % backend)
    try:
        repo_users = backend.list_user_info()
        if user_to_check not in repo_users and user_to_check.lower() not in repo_users:
            backend.create_user(user_to_check, role, password=passwd)
            return backend.get_user_info(user_to_check)
    except Exception as e:
        logging.error("Error creating Jupiter User: %s" % e)
        return False
