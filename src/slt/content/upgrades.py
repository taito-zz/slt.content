from Products.CMFCore.utils import getToolByName
from abita.utils.utils import reimport_profile


PROFILE_ID = 'profile-slt.content:default'


def reimport_catalog(context):
    """Reimport catalog"""
    reimport_profile(context, PROFILE_ID, 'catalog')
    catalog = getToolByName(context, 'portal_catalog')
    catalog.clearFindAndRebuild()


def reimport_rolemap(context):
    """Reimport rolemap"""
    reimport_profile(context, PROFILE_ID, 'rolemap')


def reimport_typeinfo(context):
    """Reimport typeinfo"""
    reimport_profile(context, PROFILE_ID, 'typeinfo')


def provide_interfaces(context):
    """Provide interfaces"""
    from collective.base.interfaces import IAdapter
    from collective.cart.core.interfaces import IOrderContainer
    from collective.cart.shipping.interfaces import IOrderShippingMethod
    from collective.cart.shopping.interfaces import IArticleContainer
    from collective.cart.shopping.interfaces import IOrderArticle
    from plone.dexterity.utils import createContentInContainer
    from slt.content.interfaces import IArticle
    from slt.content.interfaces import IMemberArea
    from slt.content.interfaces import IOrder
    from zope.interface import alsoProvides
    from zope.lifecycleevent import modified

    adapter = IAdapter(context)
    path = adapter.portal_path()

    for brain in adapter.get_brains(portal_type=['collective.cart.core.Article'], path=path):
        obj = brain.getObject()
        obj.vat_rate = float(obj.vat_rate)
        alsoProvides(obj, IArticle)
        modified(obj)

    for brain in adapter.get_brains(portal_type=['collective.cart.core.Cart'], path=path):
        obj = brain.getObject()
        alsoProvides(obj, IOrder)
        modified(obj)

    for brain in adapter.get_brains(portal_type=['collective.cart.core.CartArticle'], path=path):
        obj = brain.getObject()
        alsoProvides(obj, IOrderArticle)
        modified(obj)

    for brain in adapter.get_brains(portal_type=['collective.cart.core.CartContainer'], path=path):
        obj = brain.getObject()
        alsoProvides(obj, IOrderContainer)
        modified(obj)

    for brain in adapter.get_brains(portal_type=['collective.cart.shipping.CartShippingMethod'], path=path):
        obj = brain.getObject()
        alsoProvides(obj, IOrderShippingMethod)
        modified(obj)

    for brain in adapter.get_brains(portal_type=['slt.content.MemberArea'], path=path):
        obj = brain.getObject()
        alsoProvides(obj, IMemberArea)
        modified(obj)

    for brain in adapter.get_brains(portal_type=['collective.cart.shopping.ArticleContainer'], path=path):
        obj = brain.getObject()
        alsoProvides(obj, IArticleContainer)
        modified(obj)

    portal = adapter.portal()
    tilaukset = portal['tilaukset']
    container = createContentInContainer(portal, 'collective.cart.core.OrderContainer', title='Tilaukset',
        next_order_id=tilaukset.next_cart_id, checkConstraints=False)
    modified(container)
