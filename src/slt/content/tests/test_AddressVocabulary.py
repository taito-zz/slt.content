# -*- coding: utf-8 -*-
from slt.content.tests.base import IntegrationTestCase
from slt.content.vocabulary import AddressVocabulary

import mock


class AddressVocabularyTestCase(IntegrationTestCase):
    """TestCas for AddressVocabulary"""

    def test_subclass(self):
        self.assertTrue(issubclass(AddressVocabulary, object))

    def test_verifyObject(self):
        from zope.interface.verify import verifyObject
        from zope.schema.interfaces import IVocabularyFactory
        self.assertTrue(verifyObject(IVocabularyFactory, AddressVocabulary()))

    @mock.patch('slt.content.vocabulary.IMember')
    def test___call__(self, IMember):
        instance = AddressVocabulary()
        member = IMember()
        member.infos.return_value = []
        self.assertEqual(len(instance(self.portal)), 0)

        info = mock.Mock()
        info.first_name = u'Fırst'
        info.last_name = u'Läst'
        info.street = u'Str€€t'
        info.UID = u'uuid'
        member.infos.return_value = [info]
        self.assertEqual(len(instance(self.portal)), 1)
