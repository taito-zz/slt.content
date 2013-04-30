from collective.cart.core.interfaces import IShoppingSiteRoot
from collective.cart.shopping.interfaces import IShoppingSite
from slt.content.adapter.interface import RootShoppingSite
from slt.content.tests.base import IntegrationTestCase

import mock


class RootShoppingSiteTestCase(IntegrationTestCase):
    """TestCas for RootShoppingSite"""

    def test_subclass(self):
        from collective.cart.shopping.adapter.interface import ShoppingSite as BaseShoppingSite
        self.assertTrue(issubclass(RootShoppingSite, BaseShoppingSite))

    def test_verifyObject(self):
        from zope.interface.verify import verifyObject
        self.assertTrue(verifyObject(IShoppingSite, IShoppingSite(self.portal)))

    @mock.patch('collective.cart.shopping.adapter.interface.ShoppingSite.cart')
    def test_create_order(self, cart):
        from zope.interface import alsoProvides
        alsoProvides(self.portal, IShoppingSiteRoot)

        with self.assertRaises(AttributeError):
            IShoppingSite(self.portal).create_order(order_id='2').registration_number

        self.create_content('collective.cart.core.OrderContainer')
        cart.return_value = {'articles': {'UUID1': mock.MagicMock()}, 'registration_number': '3'}
        self.assertEqual(IShoppingSite(self.portal).create_order(order_id='3').registration_number, '3')
