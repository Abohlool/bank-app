"""
a lightweight banking database interface package. 
Providing models, queries, and connection utilities.
"""

version = "1.0.0"
__author__ = "Arvin Bohlool - https://github.com/Abohlool/"
__license__ = "GNU GENERAL PUBLIC LICENSE Version 3"
__all__ = ["connection", "queries", "models"]


from . import connection
from . import queries
from . import models
