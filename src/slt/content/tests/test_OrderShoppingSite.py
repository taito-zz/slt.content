from collective.cart.shopping.interfaces import IShoppingSite
from slt.content.adapter.interface import OrderShoppingSite
from slt.content.tests.base import IntegrationTestCase

import mock


class OrderShoppingSiteTestCase(IntegrationTestCase):
    """TestCas for OrderShoppingSite"""

    def test_subclass(self):
        from collective.cart.shopping.adapter.interface import ShoppingSite as BaseShoppingSite
        self.assertTrue(issubclass(OrderShoppingSite, BaseShoppingSite))

    def test_verifyObject(self):
        from zope.interface.verify import verifyObject
        context = self.create_content('collective.cart.core.Order')
        self.assertTrue(verifyObject(IShoppingSite, IShoppingSite(context)))

    @mock.patch('slt.content.adapter.interface.getToolByName')
    def test_link_to_order(self, getToolByName):
        context = self.create_content('collective.cart.core.Order', id='2')
        getToolByName().getHomeUrl.return_value = 'home_url'
        self.assertEqual(IShoppingSite(context).link_to_order(2), 'home_url?order_number=2')
