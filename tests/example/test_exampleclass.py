#!/usr/bin/env python3

### IMPORTS ###
import logging
import unittest

import example

### GLOBALS ###

### FUNCTIONS ###

### CLASSES ###
class TestExampleClass(unittest.TestCase):
    def setUp(self):
        # Setup logging for the class
        self.logger = logging.getLogger(type(self).__name__)
        self.logger.debug("setUp")

    def test_get_value_one(self):
        self.logger.debug("test_get_value_one")
        dut_ec = example.ExampleClass(value_one = "abcde")
        dut_vo = dut_ec.get_value_one()
        self.assertEqual(dut_vo, "abcde")
