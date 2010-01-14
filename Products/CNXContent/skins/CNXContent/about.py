## Script (Python) "about"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title= Backward compatibility redirect
##

return context.REQUEST.RESPONSE.redirect('content_info', 301)


