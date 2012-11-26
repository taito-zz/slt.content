from Products.CMFCore.utils import getToolByName
from collective.cart.shopping.interfaces import ICustomerInfo
from five import grok
from slt.content.interfaces import IMember
from zope.interface import Interface


class Member(grok.Adapter):
    """Adapter interface for member related."""

    grok.context(Interface)
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
            catalog = getToolByName(self.context, 'portal_catalog')
            brains = catalog(UID=self.area.default_billing_info)
            if brains:
                return brains[0]

    @property
    def default_shipping_info(self):
        """Default shipping info."""
        if self.area.default_shipping_info:
            catalog = getToolByName(self.context, 'portal_catalog')
            brains = catalog(UID=self.area.default_shipping_info)
            if brains:
                return brains[0]

    @property
    def infos(self):
        """All the address infos."""
        catalog = getToolByName(self.context, 'portal_catalog')
        query = {
            'object_provides': ICustomerInfo.__identifier__,
            'path': {
                'query': '/'.join(self.area.getPhysicalPath()),
                'depth': 1,
            }
        }
        return catalog(query)

    def rest_of_infos(self, uuid):
        """All the address infos except for the info with the uuid."""
        return [info for info in self.infos if info.UID != uuid]
