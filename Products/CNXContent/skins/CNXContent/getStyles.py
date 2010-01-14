## Script (Python) "getStyles"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=style=None
##title=
##

# FIXME: should get this from some kind of style registry
portal_url = context.portal_url()
styles = [
    {'id':'newlook','title':'New Look','path':portal_url+'/cnx-styles/newlook/document.css','active':1},
    ]
return styles
