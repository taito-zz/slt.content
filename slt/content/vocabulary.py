from five import grok
from slt.content.interfaces import IMember
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary


@grok.provider(IContextSourceBinder)
def infos(context):
    terms = []
    for brain in IMember(context).infos:
        info = u'{} {}: {}'.format(brain.first_name, brain.last_name, brain.street)
        terms.append(SimpleVocabulary.createTerm(info, str(brain.UID), info))
    return SimpleVocabulary(terms)
