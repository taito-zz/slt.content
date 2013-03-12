# from collective.cart import shopping
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


# class ICustomerInfoBrain(Interface):
#     """Adapter interface for brain of CustomerInfo."""

#     def __call__():  # pragma: no cover
#         """Returns dictionary of easily accessible keys and values."""


# class ICartAdapter(shopping.interfaces.ICartAdapter):
#     """Adapter interface for Cart."""
