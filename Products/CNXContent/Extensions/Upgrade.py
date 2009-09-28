def addCustomStylesheetExternalMethods(self):  
    addLocation=self.portal_skins.custom
    for p in ['TIMEA','RUP']:
        methodName='special'+p
        if not hasattr(addLocation,methodName):  
            addLocation.manage_addProduct['ExternalMethod'].manage_addExternalMethod(methodName, 'Property-setting method for %s content', 'CNXPloneSite.specialBranding', methodName)


def removeCustomStylesFolder(self):
    skinstool=self.portal_skins
    skins = skinstool.getSkinSelections()
    if hasattr(skinstool,'styles'):
        skinstool.manage_delObjects(['styles'])
    for skin in skins:
        pathlist = skinstool.getSkinPath(skin).split(',')
        if 'styles' in pathlist:
            pathlist.remove('styles')
            path = ','.join(pathlist)
            skinstool.addSkinSelection(skin, path)
