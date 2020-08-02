"""
MainPackage.Test.TestPackageA
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

import unittest
import MainPackage

def setUpModule():
    """Set Up Module"""
    pass


def tearDownModule():
    """Tear Down Module"""
    pass

class TestPackageA(unittest.TestCase):
    """Test Package A."""

    @classmethod
    def setUpClass(cls):
        """Prepare test set up class."""
        pass

    def test_module_a_init(self):
        """Test Module A Init."""
        
        module_a = MainPackage.ModuleA()
        module_a.method_a()