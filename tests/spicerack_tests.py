#!/usr/bin/env python

import unittest

# These three lines allow me to run this from within Sublime Text
import os
import sys
sys.path.append(os.path.abspath('..'))

# From folder.filename import *
# from spicerack.spicerack import *
# OR:
# import folder.filename as filename
import spicerack.spicerack as srack

import json

# You can run all tests in this directory with:
# python -m unittest discover -p '*tests.py'

class test_database(unittest.TestCase):
    """ Test database functions """

    spiceName = "Tumeric"
    spiceRow = "2"
    spiceColumn = "5"

    def test_table_exists(self):
        srack.get_table()

    @unittest.skip("Not written")
    def test_store_spice(self):
        spiceName = "Tumeric"
        spiceLocation = ""
        spiceRow = "2"
        spiceColumn = "5"
        srack.store_spice(spiceName, spiceLocation, spiceRow, spiceColumn)

    @unittest.skip("Not written")
    def test_recall_spice(self):
        spiceName = "Tumeric"
        result = srack.recall_spice(spiceName)
        print res



class test_lambda(unittest.TestCase):
    """ Test lamda handler and basic overhead """

    def test_lambda_handler(self):
        json_data = open('launch.json').read()
        event = json.loads(json_data)
        response = srack.lambda_handler(event, "")
        pass

    #def test_on_session_started(self):
    #def test_on_session_ended(self):
    #def test_on_launch(self):
    #def test_on_intent(self):

class test_spicerack(unittest.TestCase):
    """ Test functions specific to spicerack """

    def test_launch_response(self):
        response = srack.launch_response()
        pass

    def test_get_spice_location(self):
        json_data = open('intent-getSpiceLocation.json').read()
        intent = json.loads(json_data)["request"]["intent"]
        response = srack.get_spice_location(intent)
        pass

    def test_set_spice_location(self):
        json_data = open('intent-setSpiceLocation.json').read()
        intent = json.loads(json_data)["request"]["intent"]
        response = srack.set_spice_location(intent)
        pass


if __name__ == '__main__':
    unittest.main()
