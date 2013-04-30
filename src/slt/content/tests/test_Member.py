from slt.content.adapter.interface import Member
from slt.content.interfaces import IMember
from slt.content.tests.base import IntegrationTestCase

import mock


class MemberTestCase(IntegrationTestCase):
    """TestCase for Member"""

    def test_subclass(self):
        from collective.base.adapter import Adapter
        self.assertTrue(issubclass(Member, Adapter))

    def test_verifyObject(self):
        from zope.interface.verify import verifyObject
        self.assertTrue(verifyObject(IMember, IMember(self.portal)))

    @mock.patch('slt.content.adapter.interface.getToolByName')
    def test_area(self, getToolByName):
        IMember(self.portal).area()
        self.assertTrue(getToolByName().getHomeFolder.called)

    @mock.patch('slt.content.adapter.interface.getToolByName')
    def test_default_billing_info(self, getToolByName):
        adapter = IMember(self.portal)
        getToolByName().getHomeFolder().default_billing_info = 'uuid'
        adapter.get_brain = mock.Mock()
        adapter.default_billing_info()
        adapter.get_brain.assert_called_with(UID='uuid')

    @mock.patch('slt.content.adapter.interface.getToolByName')
    def test_default_shipping_info(self, getToolByName):
        adapter = IMember(self.portal)
        getToolByName().getHomeFolder().default_shipping_info = 'uuid'
        adapter.get_brain = mock.Mock()
        adapter.default_shipping_info()
        adapter.get_brain.assert_called_with(UID='uuid')

    @mock.patch('slt.content.adapter.interface.getToolByName')
    def test_infos(self, getToolByName):
        from collective.cart.shopping.interfaces import ICustomerInfo
        adapter = IMember(self.portal)
        getToolByName().getHomeFolder().getPhysicalPath.return_value = ['', 'path']
        adapter.get_brains = mock.Mock()
        adapter.infos()
        adapter.get_brains.assert_called_with(ICustomerInfo, path='/path', depth=1)

    @mock.patch('slt.content.adapter.interface.getToolByName')
    def test_rest_of_infos(self, getToolByName):
        adapter = IMember(self.portal)
        info1 = mock.Mock()
        info1.UID = 'uuid1'
        info2 = mock.Mock()
        info2.UID = 'uuid2'
        info3 = mock.Mock()
        info3.UID = 'uuid3'
        adapter.get_brains = mock.Mock(return_value=[info1, info2, info3])
        self.assertEqual(adapter.rest_of_infos('uuid1'), [info2, info3])
        self.assertEqual(adapter.rest_of_infos('uuid2'), [info1, info3])
        self.assertEqual(adapter.rest_of_infos('uuid3'), [info1, info2])
