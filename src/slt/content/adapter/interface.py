from Products.CMFCore.utils import getToolByName
from collective.base.adapter import Adapter
from collective.cart.core.interfaces import IShoppingSiteRoot
from collective.cart.shopping.adapter.interface import ShoppingSite as BaseShoppingSite
from collective.cart.shopping.interfaces import ICustomerInfo
from collective.cart.shopping.interfaces import IShoppingSite
from datetime import datetime
from slt.content import _
from slt.content.interfaces import IMember
from slt.content.interfaces import IOrder
from zope.component import adapts
from zope.interface import implements


class OrderShoppingSite(BaseShoppingSite):
    """Adapter for content type: collective.cart.core.Order"""
    adapts(IOrder)
    implements(IShoppingSite)

    def link_to_order(self, order_id):
        """Returns link to order

        :param order_id: Order ID
        :type order_id: str

        :rtype: str
        """
        membership = getToolByName(self.context, 'portal_membership')
        return '{}?order_number={}'.format(membership.getHomeUrl(), order_id)


class RootShoppingSite(BaseShoppingSite):
    """Adapter for content type providing interface: IShoppingSiteRoot"""
    adapts(IShoppingSiteRoot)

    def create_order(self, order_id=None):
        """Create order into order container from cart

        :rtype: collective.cart.core.Order
        """
        order = super(RootShoppingSite, self).create_order(order_id=order_id)
        if order is not None:
            cart = self.cart()
            for name in IOrder.names():
                default = getattr(order, name, None)
                setattr(order, name, cart.get(name, default))
            # order.registration_number = cart.get('registration_number')
            # order.birth_date = cart.get('birth_date')
        return order

    def update_address(self, name, data):
        """Update address of cart and return message if there are one

        :param name: Name of address, such as billing and shipping.
        :type name: str

        :param data: Form data.
        :type data: dict

        :rtype: unicode or None
        """
        message = super(RootShoppingSite, self).update_address(name, data)
        if message is None and name == 'billing' and data.get('billing_organization', '') == '':
            birth_date = data.get('birth_date', '')
            try:
                birth_date = datetime.strptime(birth_date.strip(), '%d.%m.%Y').date()
                if datetime.now().year - birth_date.year >= 110:
                    return _(u'birth_date_warning_too_old', default=u'The year of the birth date is too old.')
                else:
                    self.update_cart('birth_date', birth_date.isoformat())
            except ValueError:
                return _(u'birth_date_warning', default=u'Input birth date with format: YYYY-MM-DD like 1990-01-31')


class Member(Adapter):
    """Member related adapter"""
    implements(IMember)

    def area(self):
        """Returns content type: slt.content.MemberArea

        :rtype: slt.content.MemberArea
        """
        membership = getToolByName(self.context, 'portal_membership')
        return membership.getHomeFolder()

    def default_billing_info(self):
        """Returns brain of default billing info

        :rtype: brain
        """
        if self.area().default_billing_info:
            return self.get_brain(UID=self.area().default_billing_info)

    def default_shipping_info(self):
        """Returns brain of default shipping info

        :rtype: brain
        """
        if self.area().default_shipping_info:
            return self.get_brain(UID=self.area().default_shipping_info)

    def infos(self):
        """Returns brains of all the address infos

        :rtype: brains
        """
        if self.area():
            path = '/'.join(self.area().getPhysicalPath())
            return self.get_brains(ICustomerInfo, path=path, depth=1)

    def rest_of_infos(self, uuid):
        """Returns brains of all the address infos except for the info with the uuid

        :rtype: brains
        """
        return [info for info in self.infos() if info.UID != uuid]
