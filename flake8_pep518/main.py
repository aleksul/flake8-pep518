from flake8.options.config import configparser as flake8_configparser

import flake8_pep518.mixins as mixins

flake8_configparser.RawConfigParser = mixins.PyprojectRawConfigParser


class PyprojectExtension:
    name = "flake8_pep518"
    version = "0.1.0"

    def __init__(self, tree):
        pass

    def run(self):
        yield from []
