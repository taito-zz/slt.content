from collective.cart.shopping.interfaces import IShoppingSite
from slt.content.adapter.interface import ShoppingSite
from slt.content.tests.base import IntegrationTestCase

import mock


class ShoppingSiteTestCase(IntegrationTestCase):
    """TestCas for ShoppingSite"""

    def test_subclass(self):
        from collective.cart.shopping.adapter.interface import ShoppingSite as BaseShoppingSite
        self.assertTrue(issubclass(ShoppingSite, BaseShoppingSite))

    def test_instance(self):
        self.assertIsInstance(IShoppingSite(self.portal), ShoppingSite)

    @mock.patch('slt.content.adapter.interface.getToolByName')
    def test_link_to_order_for_customer(self, getToolByName):
        getToolByName().getHomeUrl.return_value = 'home_url'
        self.assertEqual(IShoppingSite(self.portal).link_to_order_for_customer(2), 'home_url?order_number=2')
