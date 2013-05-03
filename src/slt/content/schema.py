from collective.cart.shopping.schema import ArticleSchema as BaseArticleSchema
from plone.supermodel.model import Schema
from slt.content import _
from zope import schema


class MemberAreaSchema(Schema):
    """Schema for content type: slt.content.MemberArea"""

    default_billing_info = schema.Choice(
        title=_("Default Billing Info"),
        source='slt.content.address',
        required=False)

    default_shipping_info = schema.Choice(
        title=_("Default Shipping Info"),
        source='slt.content.address',
        required=False)


class ArticleSchema(BaseArticleSchema):
    """Schema for content type: collective.cart.core.Article"""

    feed_order = schema.Int(
        title=_(u'Feed Order'),
        description=_(u'Order number for top page feed.'),
        required=False)


# Deprecated

IArticleSchema = ArticleSchema
IMemberArea = MemberAreaSchema
