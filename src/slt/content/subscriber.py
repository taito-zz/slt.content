from collective.cart.shopping.interfaces import IBillingAddressConfirmedEvent
from collective.cart.shopping.interfaces import ICartAdapter
from collective.cart.shopping.interfaces import IShippingAddressConfirmedEvent
from five import grok
from plone.dexterity.utils import createContentInContainer
from slt.content.interfaces import IMember
from zope.lifecycleevent import modified


@grok.subscribe(IBillingAddressConfirmedEvent)
def add_billing_info_to_address_book_for_the_first_time(event):
    cart = event.cart
    member = IMember(cart)
    if member.area and not member.infos:
        data = ICartAdapter(cart).get_info('billing')
        oid = u'{}1'.format('billing')
        info = createContentInContainer(
            member.area, 'collective.cart.shopping.CustomerInfo', id=oid, checkConstraints=False, **data)

        if not cart.billing_same_as_shipping:
            info.info_type = u'billing'

        modified(info)


@grok.subscribe(IShippingAddressConfirmedEvent)
def add_shipping_info_to_address_book_for_the_first_time(event):
    cart = event.cart
    member = IMember(cart)
    if member.area and not member.default_shipping_info:
        data = ICartAdapter(cart).get_info('shipping')
        oid = u'{}1'.format('shipping')
        info = createContentInContainer(
            member.area, 'collective.cart.shopping.CustomerInfo', id=oid, checkConstraints=False, **data)

        if not cart.billing_same_as_shipping:
            info.info_type = u'shipping'

        modified(info)
