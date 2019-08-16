#!/usr/bin/python3
"""test for db file storage"""
import unittest
import pep8
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


class TestDbFileStorage(unittest.TestCase):
    '''this will test the FileStorage'''


    def test_pep8_FileStorage(self):
        """Tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/db_storage.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_attr(self):
	"""Checking attributes"""
    self.assertTrue(hasattr(DBStorage, "_DBStorage_engine"))
    self.assertTrue(hasattr(DBStorage, "_DBStorage_session"))
    self.assertTrue(hasattr(DBStorage, "all"))
    self.assertTrue(hasattr(DBStorage, "new"))
    self.assertTrue(hasattr(DBStorage, "save"))
    self.assertTrue(hasattr(DBStorage, "delete"))
    self.assertTrue(hasattr(DBStorage, "reload"))
