from collective.cart.shopping.interfaces import IArticleAdapter
from decimal import Decimal
from moneyed import Money
from slt.content.adapter.article import ArticleAdapter
from slt.content.tests.base import IntegrationTestCase

import mock


class ArticleAdapterTestCase(IntegrationTestCase):
    """TestCase for ArticleAdapter"""

    def test_subclass(self):
        from collective.cart.shopping.adapter.article import ArticleAdapter as Base
        self.assertTrue(issubclass(ArticleAdapter, Base))

    def test_instance(self):
        context = self.create_content('collective.cart.core.Article')
        self.assertIsInstance(IArticleAdapter(context), ArticleAdapter)

    def test_verifyObject(self):
        from zope.interface.verify import verifyObject
        context = self.create_content('collective.cart.core.Article')
        self.assertTrue(verifyObject(IArticleAdapter, IArticleAdapter(context)))

    @mock.patch('plone.app.layout.globals.portal.PortalState.member')
    def test__registered_member_discount_available(self, member):
        context = self.create_content('collective.cart.core.Article')
        instance = IArticleAdapter(context)
        member().getProperty.return_value = ''
        self.assertFalse(instance._registered_member_discount_available())

        member().getProperty.return_value = 'RN'
        self.assertFalse(instance._registered_member_discount_available())

        context.registered_member_discount_enabled = True
        self.assertFalse(instance._registered_member_discount_available())

        context.registered_member_discount_price = 'PRICE'
        self.assertTrue(instance._registered_member_discount_available())

    def test_discount_available(self):
        context = self.create_content('collective.cart.core.Article')
        instance = IArticleAdapter(context)
        self.assertFalse(instance.discount_available())

        context.discount_enabled = True
        self.assertFalse(instance.discount_available())

        from datetime import date
        context.discount_end = date.today()
        self.assertTrue(instance.discount_available())

        context.discount_enabled = False
        self.assertFalse(instance.discount_available())

        instance._registered_member_discount_available = mock.Mock(return_value=True)
        self.assertTrue(instance.discount_available())

        instance._registered_member_discount_available = mock.Mock(return_value=False)
        self.assertFalse(instance.discount_available())

    def test_discount_end(self):
        context = self.create_content('collective.cart.core.Article')
        instance = IArticleAdapter(context)
        self.assertIsNone(instance.discount_end())

        context.discount_enabled = True
        from datetime import date
        context.discount_end = date.today()
        self.assertIsNotNone(instance.discount_end())

        context.discount_enabled = False
        context.registered_member_discount_enabled = True
        context.registered_member_discount_price = 'PRICE'
        self.assertIsNone(instance.discount_end())

    @mock.patch('collective.cart.shopping.adapter.article.ArticleAdapter.gross', mock.Mock(return_value=Money(Decimal('10.00'), currency='EUR')))
    def test_gross(self):
        context = self.create_content('collective.cart.core.Article')
        instance = IArticleAdapter(context)
        self.assertEqual(instance.gross(), self.money('10.00'))

        instance._registered_member_discount_available = mock.Mock(return_value=True)
        context.registered_member_discount_money = self.money('11.00')
        self.assertEqual(instance.gross(), self.money('10.00'))

        context.registered_member_discount_money = self.money('10.00')
        self.assertEqual(instance.gross(), self.money('10.00'))

        context.registered_member_discount_money = self.money('9.00')
        self.assertEqual(instance.gross(), self.money('9.00'))
