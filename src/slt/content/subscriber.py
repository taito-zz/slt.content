from collective.cart.shopping.interfaces import IBillingAddressConfirmedEvent
from collective.cart.shopping.interfaces import IShippingAddressConfirmedEvent
from collective.cart.shopping.interfaces import IShoppingSite
from plone.dexterity.utils import createContentInContainer
from slt.content.interfaces import IMember
from zope.component import adapter
from zope.lifecycleevent import modified


@adapter(IBillingAddressConfirmedEvent)
def add_billing_info_to_address_book_for_the_first_time(event):
    member = IMember(event.context)
    if member.area and not member.infos:
        data = IShoppingSite(event.context).get_address('billing')
        oid = u'{}1'.format('billing')
        info = createContentInContainer(
            member.area, 'collective.cart.shopping.CustomerInfo', id=oid, checkConstraints=False, **data)

        if not IShoppingSite(event.context).billing_same_as_shipping:
            info.info_type = u'billing'

        modified(info)


@adapter(IShippingAddressConfirmedEvent)
def add_shipping_info_to_address_book_for_the_first_time(event):
    member = IMember(event.context)
    if member.area and not member.default_shipping_info:
        data = IShoppingSite(event.context).get_address('shipping')
        oid = u'{}1'.format('shipping')
        info = createContentInContainer(
            member.area, 'collective.cart.shopping.CustomerInfo', id=oid, checkConstraints=False, **data)

        if not IShoppingSite(event.context).billing_same_as_shipping:
            info.info_type = u'shipping'

        modified(info)
