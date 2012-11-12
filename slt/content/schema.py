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
