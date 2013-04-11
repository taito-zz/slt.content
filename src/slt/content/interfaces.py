from plone.dexterity.interfaces import IDexterityContainer
from zope.interface import Attribute
from zope.interface import Interface


class IFeedToShopTop(Interface):
    """A marker interface for feed to shop top page."""


class IMember(Interface):
    """Adapter interface for member related."""

    area = Attribute('MemberArea content type for member.')
    default_billing_info = Attribute('Default billing info.')
    default_shipping_info = Attribute('Default shipping info.')
    infos = Attribute('All the address infos.')

    def rest_of_infos(uuid):  # pragma: no cover
        """All the address infos except for the info with the uuid."""


class ICart(IDexterityContainer):
    """Interface for content type: collective.cart.core.Cart"""

    registration_number = Attribute('Registration number for the purchaser')
