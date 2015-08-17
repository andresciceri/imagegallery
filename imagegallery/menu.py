from menus.base import Menu, NavigationNode
from menus.menu_pool import menu_pool
from django.utils.translation import ugettext_lazy as_
from cms.menu_bases import CMSAttachMenu

class MainMenu (CMSAttachMenu):

	name = _("Main Menu")

	def get_nodes(self, request):
		nodes 	= []
		n 		= NavigationNode(_('Home'),"/",1)
		n2 		= NavigationNode(_('Add Image'),"/create",2)
		n3 		= NavigationNode(_('About'),"/about",3)
		n4 		= NavigationNode(_('Contact us'),"/contact",4)

		nodes.append(n)
		nodes.append(n2)
		nodes.append(n3)
		nodes.append(n4)
		return nodes

menu_pool.register_menu(MainMenu)