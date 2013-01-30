from slt.content.tests.base import IntegrationTestCase

import mock


class TestCase(IntegrationTestCase):
    """TestCase for upgrade steps."""

    def setUp(self):
        self.portal = self.layer['portal']

    @mock.patch('slt.content.upgrades.getToolByName')
    @mock.patch('slt.content.upgrades.reimport_profile')
    def test_reimport_catalog(self, reimport_profile, getToolByName):
        from slt.content.upgrades import reimport_catalog
        reimport_catalog(self.portal)
        reimport_profile.assert_called_with(self.portal, 'profile-slt.content:default', 'catalog')
        self.assertTrue(getToolByName().clearFindAndRebuild.called)

    @mock.patch('slt.content.upgrades.reimport_profile')
    def test_reimport_rolemap(self, reimport_profile):
        from slt.content.upgrades import reimport_rolemap
        reimport_rolemap(self.portal)
        reimport_profile.assert_called_with(self.portal, 'profile-slt.content:default', 'rolemap')

    @mock.patch('slt.content.upgrades.reimport_profile')
    def test_reimport_typeinfo(self, reimport_profile):
        from slt.content.upgrades import reimport_typeinfo
        reimport_typeinfo(self.portal)
        reimport_profile.assert_called_with(self.portal, 'profile-slt.content:default', 'typeinfo')
