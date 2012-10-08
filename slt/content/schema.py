from collective.cart import shopping
from plone.directives import form
from sll.shopping import _
from zope import schema


class IShop(shopping.interfaces.IShop):
    """Schema interface for Shop."""

    number_of_feed_on_top = schema.Int(
        title=_('Number of Feed on Top'),
        description=_(
            u'description_number_of_feed_on_top',
            default=u'This number of articles will be fed to shop top page in maximum.'),
        default=6,
        min=0)


class IMemberArea(form.Schema):
    """Schema interface for MemberArea."""
