from collective.cart import shopping
from collective.cart.shopping.interfaces import IShoppingSite
from five import grok
from plone.dexterity.utils import createContentInContainer
from slt.content.interfaces import ICartAdapter
from slt.content.interfaces import IMember
from zope.lifecycleevent import modified


class CartAdapter(shopping.adapter.cart.CartAdapter):

    grok.provides(ICartAdapter)

    def add_address(self, name):
        info = '{}_info'
        if not getattr(self, info, None):
            member = IMember(self.context)
            default_attr = 'default_{}_info'.format(name)
            address = getattr(member, default_attr, None)
            if not address and member.infos:
                address = member.infos[0]
            if address:
                attrs = ['first_name', 'last_name', 'organization', 'vat', 'email',
                    'street', 'post', 'city', 'phone']
                data = {}
                for attr in attrs:
                    data[attr] = getattr(address, attr)
                data['orig_uuid'] = address.UID
                info = createContentInContainer(
                    IShoppingSite(self.context).cart, 'collective.cart.shopping.CustomerInfo', id=name,
                    checkConstraints=False, **data)
                modified(info)

    def add_addresses(self):
        self.add_address('billing')
        self.add_address('shipping')
