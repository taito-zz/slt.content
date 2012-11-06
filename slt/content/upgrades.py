from Products.CMFCore.utils import getToolByName

import logging


PROFILE_ID = 'profile-slt.content:default'


def update_typeinfo(context, logger=None):
    """Update typeinfo"""
    if logger is None:
        logger = logging.getLogger(__name__)
    setup = getToolByName(context, 'portal_setup')
    logger.info('Reimporting typeinfo.')
    setup.runImportStepFromProfile(
        PROFILE_ID, 'typeinfo', run_dependencies=False, purge_old=False)
