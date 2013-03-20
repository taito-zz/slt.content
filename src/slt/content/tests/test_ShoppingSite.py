from collective.cart.shopping.interfaces import IShoppingSite
from slt.content.adapter.interface import ShoppingSite
from slt.content.tests.base import IntegrationTestCase

import mock


class ShoppingSiteTestCase(IntegrationTestCase):
    """TestCas for ShoppingSite"""

    def test_subclass(self):
        from collective.cart.shopping.adapter.interface import ShoppingSite as BaseShoppingSite
        self.assertTrue(issubclass(ShoppingSite, BaseShoppingSite))

    def test_context(self):
        from collective.cart.shopping.interfaces import ICart
        self.assertEqual(getattr(ShoppingSite, 'grokcore.component.directive.context'), ICart)

    def test_instance(self):
        cart = self.create_content('collective.cart.core.Cart')
        self.assertIsInstance(IShoppingSite(cart), ShoppingSite)

    @mock.patch('slt.content.adapter.interface.getToolByName')
    def test_link_to_order_for_customer(self, getToolByName):
        cart = self.create_content('collective.cart.core.Cart', id='2')
        getToolByName().getHomeUrl.return_value = 'home_url'
        self.assertEqual(IShoppingSite(cart).link_to_order_for_customer(2), 'home_url?order_number=2')
