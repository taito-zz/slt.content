from Products.CMFCore.utils import getToolByName
from collective.base.adapter import Adapter
from collective.cart.shopping.interfaces import ICustomerInfo
from five import grok
from slt.content.interfaces import IMember
# from zope.interface import Interface


class Member(Adapter):
    """Member related adapter"""

    grok.provides(IMember)

    @property
    def area(self):
        """MemberArea content type for member."""
        membership = getToolByName(self.context, 'portal_membership')
        return membership.getHomeFolder()

    @property
    def default_billing_info(self):
        """Default billing info."""
        if self.area.default_billing_info:
            return self.get_brain(UID=self.area.default_billing_info)

    @property
    def default_shipping_info(self):
        """Default shipping info."""
        if self.area.default_shipping_info:
            return self.get_brain(UID=self.area.default_shipping_info)

    @property
    def infos(self):
        """All the address infos."""
        if self.area:
            path = '/'.join(self.area.getPhysicalPath())
            return self.get_brains(ICustomerInfo, path=path, depth=1)

    def rest_of_infos(self, uuid):
        """All the address infos except for the info with the uuid."""
        return [info for info in self.infos if info.UID != uuid]
