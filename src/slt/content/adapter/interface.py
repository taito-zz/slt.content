from Products.CMFCore.utils import getToolByName
from collective.base.adapter import Adapter
from collective.cart.core.interfaces import IShoppingSiteRoot
from collective.cart.shopping.adapter.interface import ShoppingSite as BaseShoppingSite
from collective.cart.shopping.interfaces import ICustomerInfo
from collective.cart.shopping.interfaces import IShoppingSite
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
            order.registration_number = self.cart().get('registration_number')
        return order


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
