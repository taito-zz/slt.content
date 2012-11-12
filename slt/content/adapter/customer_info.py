from five import grok
from slt.content.interfaces import ICustomerInfoBrain
from zope.interface import Interface


class CustomerInfoBrain(grok.Adapter):
    """Adapter interface for brain of CustomerInfo."""

    grok.context(Interface)
    grok.provides(ICustomerInfoBrain)

    def __call__(self):
        """Returns dictionary of easily accessible keys and values."""
        return {
            'name': self._name(self.context),
            'organization': self._organization(self.context),
            'street': self.context.street,
            'city': self._city(self.context),
            'email': self.context.email,
            'phone': self.context.phone,
            'edit_url': '{}/edit'.format(self.context.getURL()),
            'uuid': self.context.UID,
            'orig_uuid': self.context.orig_uuid,
        }

    def _name(self, item):
        return u'{} {}'.format(item.first_name, item.last_name)

    def _organization(self, item):
        org = item.organization
        if org:
            if item.vat:
                org = u'{} {}'.format(item.organization, item.vat)
            return org.strip()

    def _city(self, item):
        if item.post:
            city = u'{} {}'.format(item.city, item.post)
            return city.strip()
