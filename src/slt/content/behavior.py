from collective.behavior.discount.behavior import Discount
from plone.autoform.interfaces import IFormFieldProvider
from slt.content.interfaces import IDiscountBehavior
from zope.interface import alsoProvides
from zope.interface import implements


alsoProvides(IDiscountBehavior, IFormFieldProvider)


class DiscountBehavior(Discount):
    """Behavior to add price and discount field"""

    implements(IDiscountBehavior)

    @property
    def registered_member_discount_enabled(self):
        return getattr(self.context, 'registered_member_discount_enabled', False)

    @registered_member_discount_enabled.setter
    def registered_member_discount_enabled(self, value):
        """Set registered_member_discount_enabled as Boolean

        :param value: True or False
        :type value: bool
        """
        self._set_bool('registered_member_discount_enabled', value)

    @property
    def registered_member_discount_price(self):
        return getattr(self.context, 'registered_member_discount_price', None)

    @registered_member_discount_price.setter
    def registered_member_discount_price(self, value):
        """Setting registered_member_discount_price as Decimal and registered_member_discount_money as Money.

        :param value: Price value such as 5.00, 5,00 nor 1800.
        :type value: decimal.Decimal
        """
        self._set_price(value, name='registered_member_discount_')

    @property
    def registered_member_discount_money(self):
        return self._get_money('registered_member_discount_')

    @registered_member_discount_money.setter
    def registered_member_discount_money(self, value):
        """Setting registered_member_discount_money as Money.

        :param value: Money instance.
        :type value: moneyed.Money
        """
        self._set_money(value, name='registered_member_discount_')
