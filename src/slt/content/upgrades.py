from Products.CMFCore.utils import getToolByName


PROFILE_ID = 'profile-slt.content:default'


def reimport_catalog(setup):
    """Reimport catalog"""
    setup.runImportStepFromProfile(PROFILE_ID, 'catalog', run_dependencies=False, purge_old=False)
    catalog = getToolByName(setup, 'portal_catalog')
    catalog.clearFindAndRebuild()


def reimport_memberdata_properties(setup):
    """Reimport memberdata properties"""
    setup.runImportStepFromProfile(PROFILE_ID, 'memberdata-properties', run_dependencies=False, purge_old=False)


def reimport_rolemap(setup):
    """Reimport rolemap"""
    setup.runImportStepFromProfile(PROFILE_ID, 'rolemap', run_dependencies=False, purge_old=False)


def reimport_typeinfo(setup):
    """Reimport typeinfo"""
    setup.runImportStepFromProfile(PROFILE_ID, 'typeinfo', run_dependencies=False, purge_old=False)
