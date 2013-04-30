from collective.cart.shopping.content import Article as BaseArticle
from collective.cart.shopping.content import Order as BaseOrder
from plone.dexterity.content import Container
from slt.content.interfaces import IArticle
from slt.content.interfaces import IMemberArea
from slt.content.interfaces import IOrder
from zope.interface import implements


class MemberArea(Container):
    """Content type: slt.content.MemberArea"""
    implements(IMemberArea)

    default_billing_info = None
    default_shipping_info = None


class Article(BaseArticle):
    """Content type: collective.cart.core.Article"""
    implements(IArticle)


class Order(BaseOrder):
    """Content type: collective.cart.core.Order"""
    implements(IOrder)

    registration_number = None
