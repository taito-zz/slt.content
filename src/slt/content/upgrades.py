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
    from collective.cart.shopping.interfaces import IOrderArticle
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

#     # catalog = getToolByName(context, 'portal_catalog')
#     # catalog.clearFindAndRebuild()


#     intids = getUtility(IIntIds)
#     res = []

#     for brain in adapter.get_brains(portal_type=['collective.cart.core.Article'], path=path):
#         obj = brain.getObject()
#         obj.vat_rate = float(obj.vat_rate)
#         alsoProvides(obj, IArticle)
#         modified(obj)
#         res.append(obj)

#     for brain in adapter.get_brains(portal_type=['collective.cart.core.Article', 'collective.cart.shopping.ArticleContainer'], path=path):
#         obj = brain.getObject()
#         try:
#             intids.unregister(obj)
#         except KeyError:
#             pass

#         from_id = intids.register(obj)

#     for obj in res:
#         # intids.unregister(obj)
#         # from_id = intids.register(obj)
#         if getattr(obj, 'related_items', None):
#             items = []
#             for uuid in obj.related_items:
#                 # to_id = intids.register(adapter.get_object(UID=uuid, path=path))
#                 item_object = adapter.get_object(UID=uuid, path=path)
#                 # intids.register(item_object)
#                 to_id = intids.getId(item_object)
#             # new_relationships.append(RelationValue(to_id))
#         # super(RelationListDataManager, self).set(new_relationships)

#                 rel = RelationValue(to_id)
#                 rel.from_object = obj
#                 items.append(rel)
#             obj.relatedItems = items
#     #         for item in obj.relatedItems:
#     #             item._from_id = from_id
#     #             index = obj.relatedItems.index(item)
#     #             item.to_id = intids.register(res[obj][index])
#     #             import pdb; pdb.set_trace()

#         # modified(obj)
#         obj.reindexObject()

#     #     res.append(obj)

#     # catalog = getToolByName(context, 'portal_catalog')
#     # catalog.clearFindAndRebuild()

#     # for obj in res:
#     #     alsoProvides(obj, IArticle)
#     #     modified(obj)

# #
# #     for brain in catalog(object_provides=[IArticle.__identifier__]):
# #         obj = brain.getObject()
# #         if hasattr(obj, 'relatedItems'):
# #             res.update({obj: [item.to_object for item in obj.relatedItems]})

# #     portal = getToolByName(context, 'portal_url').getPortalObject()
# #     parent = aq_parent(portal)
# #     parent.manage_renameObject('kauppa', 'luontokauppa')

# #     for obj in res:
# #         intids.unregister(obj)

# #     for obj in res:
# #         from_id = intids.register(obj)
# #         if hasattr(obj, 'relatedItems'):
# #             for item in obj.relatedItems:
# #                 item._from_id = from_id
# #                 index = obj.relatedItems.index(item)
# #                 item.to_id = intids.register(res[obj][index])
