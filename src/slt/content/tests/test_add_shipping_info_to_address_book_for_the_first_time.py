from slt.content.tests.base import IntegrationTestCase

import mock


class TestCase(IntegrationTestCase):
    """TestCas to test subscriber: add_shipping_info_to_address_book_for_the_first_time"""

    @mock.patch('slt.content.subscriber.IShoppingSite')
    @mock.patch('slt.content.subscriber.IMember')
    def test_add_shipping_info_to_address_book_for_the_first_time(self, IMember, IShoppingSite):
        from slt.content.subscriber import add_shipping_info_to_address_book_for_the_first_time
        event = mock.Mock()
        area = self.create_content('slt.content.MemberArea', id='area')
        member = IMember()
        member.area = area
        member.default_shipping_info = True
        add_shipping_info_to_address_book_for_the_first_time(event)
        self.assertIsNone(area.get('shipping1'))

        member.default_shipping_info = False
        shopping_site = IShoppingSite()
        shopping_site.get_address.return_value = {}
        add_shipping_info_to_address_book_for_the_first_time(event)
        self.assertIsNotNone(area.get('shipping1'))
        self.assertIsNone(area.get('shipping1').info_type)

        shopping_site.billing_same_as_shipping = False
        area.manage_delObjects(['shipping1'])
        add_shipping_info_to_address_book_for_the_first_time(event)
        self.assertIsNotNone(area.get('shipping1'))
        self.assertEqual(area.get('shipping1').info_type, u'shipping')
