from Products.CMFCore.utils import getToolByName
from abita.utils.utils import reimport_profile


PROFILE_ID = 'profile-slt.content:default'


def reimport_typeinfo(context):
    """Reimport typeinfo"""
    reimport_profile(context, PROFILE_ID, 'typeinfo')


def reimport_catalog(context):
    """Reimport catalog"""
    reimport_profile(context, PROFILE_ID, 'catalog')
    catalog = getToolByName(context, 'portal_catalog')
    catalog.clearFindAndRebuild()
