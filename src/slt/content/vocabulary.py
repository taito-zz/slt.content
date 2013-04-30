from slt.content.interfaces import IMember
from zope.interface import implements
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleVocabulary


class AddressVocabulary(object):
    implements(IVocabularyFactory)

    def __call__(self, context):
        terms = []
        for brain in IMember(context).infos():
            info = u'{} {}: {}'.format(brain.first_name, brain.last_name, brain.street)
            terms.append(SimpleVocabulary.createTerm(info, str(brain.UID), info))
        return SimpleVocabulary(terms)

AddressVocabularyFactory = AddressVocabulary()
