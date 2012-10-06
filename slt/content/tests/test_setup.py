from Products.CMFCore.utils import getToolByName
from slt.content.tests.base import IntegrationTestCase


class TestCase(IntegrationTestCase):
    """TestCase for Plone setup."""

    def setUp(self):
        self.portal = self.layer['portal']

    def test_installed__package(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.assertTrue(installer.isProductInstalled('slt.content'))

    def test_browserlayer(self):
        from slt.content.browser.interfaces import ISltContentLayer
        from plone.browserlayer import utils
        self.assertIn(ISltContentLayer, utils.registered_layers())

    def test_metadata__version(self):
        setup = getToolByName(self.portal, 'portal_setup')
        self.assertEqual(
            setup.getVersionForProfile('profile-slt.content:default'), u'0')

    def test_metadata__installed__collective_cart_shopping(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.failUnless(installer.isProductInstalled('collective.cart.shopping'))

    def uninstall_package(self):
        """Uninstall package: slt.content."""
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        installer.uninstallProducts(['slt.content'])

    def test_uninstall__package(self):
        self.uninstall_package()
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.assertFalse(installer.isProductInstalled('slt.content'))

    def test_uninstall__browserlayer(self):
        self.uninstall_package()
        from slt.content.browser.interfaces import ISltContentLayer
        from plone.browserlayer import utils
        self.assertNotIn(ISltContentLayer, utils.registered_layers())

    def test_uninstall__metadata__installed__collective_cart_shopping(self):
        self.uninstall_package()
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.failUnless(installer.isProductInstalled('collective.cart.shopping'))
