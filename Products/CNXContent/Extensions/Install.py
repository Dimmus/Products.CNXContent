__version__ = "0.1"

from Products.CMFCore.TypesTool import FactoryTypeInformation
from Products.CMFCore.DirectoryView import addDirectoryViews
from Products.CMFCore.utils import getToolByName
from Products.CNXContent import product_globals as GLOBALS
from Products.Archetypes.Extensions.utils import install_subskin
from cStringIO import StringIO
import string

def install(self):
    """Register CNXContent with the necessary tools"""
    out = StringIO()

    # Setup the skins
    print >> out, "Installing skin layers"
    install_subskin(self, out, GLOBALS)


    return out.getvalue()

