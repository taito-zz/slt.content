from collective.cart.shopping.content import Article
from collective.cart.shopping.interfaces import IArticle
from plone.dexterity.content import Container
from slt.content.content import MemberArea
from slt.content.content import Order
from slt.content.interfaces import IMemberArea
from slt.content.interfaces import IOrder
from zope.interface.verify import verifyObject

import unittest


class MemberAreaTestCase(unittest.TestCase):
    """TestCase for content type: slt.content.MemberArea"""

    def test_subclass(self):
        self.assertTrue(issubclass(MemberArea, Container))
        from slt.content.schema import MemberAreaSchema
        self.assertTrue(issubclass(IMemberArea, MemberAreaSchema))

    def test_verifyObject(self):
        self.assertTrue(verifyObject(IMemberArea, MemberArea()))


class ArticleTestCase(unittest.TestCase):
    """TestCase for content type: collective.cart.core.Article"""

    def test_subclass(self):
        from collective.cart.shopping.content import Article as BaseArticle
        self.assertTrue(issubclass(Article, BaseArticle))
        from slt.content.schema import ArticleSchema
        from collective.cart.shopping.interfaces import IArticle as IBaseArticle
        self.assertTrue(issubclass(IArticle, (ArticleSchema, IBaseArticle)))

    def test_verifyObject(self):
        self.assertTrue(verifyObject(IArticle, Article()))


class OrderTestCase(unittest.TestCase):
    """TestCase for content type: collective.cart.core.Order"""

    def test_subclass(self):
        from collective.cart.shopping.content import Order as BaseOrder
        self.assertTrue(issubclass(Order, BaseOrder))
        from collective.cart.shopping.interfaces import IOrder as IBaseOrder
        self.assertTrue(issubclass(IOrder, IBaseOrder))

    def test_verifyObject(self):
        self.assertTrue(verifyObject(IOrder, Order()))
