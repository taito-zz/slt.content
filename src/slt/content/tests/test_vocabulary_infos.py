# -*- coding: utf-8 -*-
from slt.content.tests.base import IntegrationTestCase

import mock


class TestCase(IntegrationTestCase):
    """TestCas to test vocabulary: infos"""

    @mock.patch('slt.content.vocabulary.IMember')
    def test_infos(self, IMember):
        from slt.content.vocabulary import infos
        member = IMember()
        member.infos = []
        self.assertEqual(len(infos(self.portal)), 0)

        info = mock.Mock()
        info.first_name = u'Fırst'
        info.last_name = u'Läst'
        info.street = u'Str€€t'
        info.UID = u'uuid'
        member.infos = [info]
        self.assertEqual(len(infos(self.portal)), 1)
