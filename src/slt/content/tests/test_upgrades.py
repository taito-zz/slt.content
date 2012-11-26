from Products.CMFCore.utils import getToolByName
from slt.content.tests.base import IntegrationTestCase


class TestCase(IntegrationTestCase):
    """TestCase for upgrade steps."""

    def setUp(self):
        self.portal = self.layer['portal']

    def test_update_typeinfo(self):
        types = getToolByName(self.portal, 'portal_types')
        ctype = types.getTypeInfo('slt.content.MemberArea')
        ctype.global_allow = True
        self.assertTrue(ctype.global_allow)

        from slt.content.upgrades import update_typeinfo
        update_typeinfo(self.portal)

        self.assertFalse(ctype.global_allow)
