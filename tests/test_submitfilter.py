# -*- coding: utf-8 -*-
"""
Test suite for the submit filter library
"""

import glob
import unittest

import submitfilter as sf

DATA_DIR = "pbs"
DATA_RES = "ok"

TEST_TAG = "@TEST@"

class TestSubmitFilter(unittest.TestCase):

    def test_add_pbs_tag(self):

        cases = glob.glob("{0}/*_{1}.pbs".format(DATA_DIR, DATA_RES))

        self.assertNotEqual(cases, [], "Can't find example PBS jobs")
        
        for case in cases:

            file_good = case
            file_orig = case.replace("_{0}.pbs".format(DATA_RES), ".pbs")

            with open(file_good, "r") as fp:
                data_good = fp.readlines()

            with open(file_orig, "r") as fp:
                data_orig = fp.readlines()

            data_test = sf.add_pbs_tag(data_orig, TEST_TAG)

            self.assertEqual(data_test, data_good)

