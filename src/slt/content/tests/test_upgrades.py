from slt.content.tests.base import IntegrationTestCase

import mock


class TestCase(IntegrationTestCase):
    """TestCase for upgrade steps"""

    @mock.patch('slt.content.upgrades.getToolByName')
    def test_reimport_catalog(self, getToolByName):
        from slt.content.upgrades import reimport_catalog
        setup = mock.Mock()
        reimport_catalog(setup)
        setup.runImportStepFromProfile.assert_called_with('profile-slt.content:default', 'catalog', run_dependencies=False, purge_old=False)
        self.assertTrue(getToolByName().clearFindAndRebuild.called)

    def test_reimport_memberdata_properties(self):
        from slt.content.upgrades import reimport_memberdata_properties
        setup = mock.Mock()
        reimport_memberdata_properties(setup)
        setup.runImportStepFromProfile.assert_called_with('profile-slt.content:default', 'memberdata-properties', run_dependencies=False, purge_old=False)

    def test_reimport_rolemap(self):
        from slt.content.upgrades import reimport_rolemap
        setup = mock.Mock()
        reimport_rolemap(setup)
        setup.runImportStepFromProfile.assert_called_with('profile-slt.content:default', 'rolemap', run_dependencies=False, purge_old=False)

    def test_reimport_typeinfo(self):
        from slt.content.upgrades import reimport_typeinfo
        setup = mock.Mock()
        reimport_typeinfo(setup)
        setup.runImportStepFromProfile.assert_called_with('profile-slt.content:default', 'typeinfo', run_dependencies=False, purge_old=False)
