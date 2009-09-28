from Products.CMFCore import utils, CMFCorePermissions
from Products.CMFCore.DirectoryView import registerDirectory
from Products.CMFCore.CMFCorePermissions import setDefaultRoles

import sys
this_module = sys.modules[ __name__ ]

product_globals = globals()

# Make the skins available as DirectoryViews
registerDirectory('skins', product_globals)

def initialize(context):
    pass
