from Products.CMFCore import utils, permissions as CMFCorePermissions 
from Products.CMFCore.DirectoryView import registerDirectory
from Products.CMFCore.permissions import setDefaultRoles

import sys
this_module = sys.modules[ __name__ ]

product_globals = globals()

# Make the skins available as DirectoryViews
registerDirectory('skins', product_globals)

def initialize(context):
    pass
