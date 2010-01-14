import unittest

from zope.testing import doctestunit
from zope.component import testing
from Testing import ZopeTestCase as ztc

from Products.Five import zcml
from Products.Five import fiveconfigure
from Products.PloneTestCase import PloneTestCase as ptc
from Products.PloneTestCase.layer import PloneSite

# Set up a Plone site, and apply our custom extension profile
PROFILES = ('Products.CNXContent:default',)
ptc.setupPloneSite(extension_profiles=PROFILES)

import Products.CNXContent

class TestCase(ptc.PloneTestCase):
    class layer(PloneSite):
        @classmethod
        def setUp(cls):
            fiveconfigure.debug_mode = True
            zcml.load_config('configure.zcml', Products.CNXContent)
            ztc.installPackage('Products.CNXContent')
            fiveconfigure.debug_mode = False

        @classmethod
        def tearDown(cls):
            pass


def test_suite():
    return unittest.TestSuite([

        # Unit tests
        doctestunit.DocFileSuite(
            'static.txt', package='Products.CNXContent.tests',
            setUp=testing.setUp, tearDown=testing.tearDown),

        ])

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')

