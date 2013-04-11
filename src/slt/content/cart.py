from plone.dexterity.content import Container
from slt.content.interfaces import ICart
from zope.interface import implements


class Cart(Container):
    """Content type: collective.cart.core.Cart"""
    implements(ICart)

    registration_number = None
