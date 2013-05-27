from slt.content.behavior import DiscountBehavior
from slt.content.interfaces import IDiscountBehavior

import mock
import unittest


class TestDiscountBehavior(unittest.TestCase):
    """TestCase for DiscountBehavior"""

    def test_subclass(self):
        from collective.behavior.discount.behavior import Discount as Base
        self.assertTrue(issubclass(DiscountBehavior, Base))
        from collective.behavior.discount.interfaces import IDiscount as Base
        self.assertTrue(issubclass(IDiscountBehavior, Base))

    def create_instance(self, context=mock.Mock()):
        return DiscountBehavior(context)

    @mock.patch('collective.behavior.price.behavior.getUtility')
    def test_verifyObject(self, getUtility):
        from zope.interface.verify import verifyObject
        instance = self.create_instance()
        self.assertTrue(verifyObject(IDiscountBehavior, instance))

    def test_registered_member_discount_enabled(self):
        context = object()
        instance = self.create_instance(context=context)
        self.assertFalse(instance.registered_member_discount_enabled)

        context = mock.Mock()
        instance = self.create_instance(context=context)
        instance.registered_member_discount_enabled = False
        self.assertFalse(instance.registered_member_discount_enabled)
        self.assertFalse(instance.context.registered_member_discount_enabled)

        instance.registered_member_discount_enabled = True
        self.assertTrue(instance.registered_member_discount_enabled)
        self.assertTrue(instance.context.registered_member_discount_enabled)

    @mock.patch('collective.behavior.price.behavior.getUtility')
    def test_registered_member_discount_price_money(self, getUtility):
        context = object()
        instance = self.create_instance(context=context)
        self.assertIsNone(instance.registered_member_discount_price)
        self.assertIsNone(instance.registered_member_discount_money)

        from decimal import Decimal
        from moneyed import Money
        context = mock.Mock()
        instance = self.create_instance(context=context)
        getUtility().forInterface().default_currency = 'EUR'
        price = Decimal('5.00')
        context.registered_member_discount_price = price
        context.registered_member_discount_money = None
        self.assertEqual(instance.context.registered_member_discount_price, price)
        self.assertEqual(instance.registered_member_discount_price, price)
        money = Money(price, currency='EUR')
        self.assertIsNone(instance.context.registered_member_discount_money)
        self.assertEqual(instance.registered_member_discount_money, money)

        price = Decimal('10.00')
        instance.registered_member_discount_price = price
        self.assertEqual(instance.context.registered_member_discount_price, price)
        self.assertEqual(instance.registered_member_discount_price, price)
        money = Money(price, currency='EUR')
        self.assertEqual(instance.context.registered_member_discount_money, money)
        self.assertEqual(instance.registered_member_discount_money, money)

        money = Money(Decimal('20.00'), currency='EUR')
        instance.registered_member_discount_money = money
        self.assertEqual(instance.context.registered_member_discount_price, price)
        self.assertEqual(instance.registered_member_discount_price, price)
        self.assertEqual(instance.context.registered_member_discount_money, money)
        self.assertEqual(instance.registered_member_discount_money, money)
