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

    def get_ctype(self, name):
        """Returns content type info.

        :param name: Name of content type.
        :type name: test_types__Plone_Site__filter_content_types
        """
        types = getToolByName(self.portal, 'portal_types')
        return types.getTypeInfo(name)

    def test_types__collective_cart_shopping_Shop__schema(self):
        ctype = self.get_ctype('collective.cart.shopping.Shop')
        self.assertEqual(ctype.schema, 'slt.content.schema.IShop')

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

    def test_uninstall__types__collective_cart_shopping_Shop__schema(self):
        self.uninstall_package()
        ctype = self.get_ctype('collective.cart.shopping.Shop')
        self.assertEqual(ctype.schema, 'slt.content.schema.IShop')
