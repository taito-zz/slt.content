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

    def test_context(self):
        self.assertEqual(getattr(RootShoppingSite, 'grokcore.component.directive.context'), IShoppingSiteRoot)

    @mock.patch('collective.cart.shopping.adapter.interface.ShoppingSite.cart', new_callable=mock.PropertyMock)
    def test_create_cart(self, cart):
        from zope.interface import alsoProvides
        alsoProvides(self.portal, IShoppingSiteRoot)

        with self.assertRaises(AttributeError):
            IShoppingSite(self.portal).create_cart(cart_id='2').registration_number

        self.create_content('collective.cart.core.CartContainer', id='cart-container')
        cart.return_value = {'articles': {'UUID1': mock.MagicMock()}, 'registration_number': '3'}
        self.assertEqual(IShoppingSite(self.portal).create_cart(cart_id='3').registration_number, '3')
