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

    @mock.patch('collective.cart.shopping.adapter.interface.ShoppingSite.update_address')
    def test_update_address(self, update_address):
        from zope.interface import alsoProvides
        alsoProvides(self.portal, IShoppingSiteRoot)

        adapter = IShoppingSite(self.portal)
        data = {}

        self.assertIsNone(adapter.update_address('billing', data))

        update_address.return_value = None
        self.assertEqual(adapter.update_address('billing', data), u'birth_date_warning')

        data = {'birth_date': 'BDATE'}
        self.assertEqual(adapter.update_address('billing', data), u'birth_date_warning')

        data = {'birth_date': '1990-01-31'}
        self.assertEqual(adapter.update_address('billing', data), u'birth_date_warning')

        data = {'birth_date': '31.01.1990'}
        self.assertIsNone(adapter.update_address('billing', data))

        data = {'birth_date': '31.01.1890'}
        self.assertEqual(adapter.update_address('billing', data), u'birth_date_warning_too_old')
