from collective.cart import shopping
from plone.directives import form
from slt.content import _
from slt.content.vocabulary import infos
from zope import schema


class IMemberArea(form.Schema):
    """Schema interface for MemberArea."""

    default_billing_info = schema.Choice(
        title=_("Default Billing Info"),
        source=infos,
        required=False)

    default_shipping_info = schema.Choice(
        title=_("Default Shipping Info"),
        source=infos,
        required=False)


class IArticleSchema(shopping.interfaces.IArticle):

    feed_order = schema.Int(
        title=_(u'Feed Order'),
        description=_(u'Order number for top page feed.'),
        required=False)
