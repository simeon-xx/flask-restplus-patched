
__version__ = '0.1.4.2018120601'

from flask_restplus import *
from .api import Api
from .model import Schema, DocumentSchema, DefaultHTTPErrorSchema
from .namespace import Namespace
from .parameters import Parameters, PostFormParameters, PostJSONParameters, PatchJSONParameters
from .swagger import Swagger
from .resource import Resource

try:
    from .model import ModelSchema
except ImportError:
    pass
