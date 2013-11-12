from plone.app.contentlisting.interfaces import IContentListingObject
from slt.content.adapter.content_listing_object import ArticleContentListingObject
from slt.content.tests.base import IntegrationTestCase


class ArticleContentListingObjectTestCase(IntegrationTestCase):
    """TestCase for ArticleContentListingObject"""

    def test_subclass(self):
        from collective.cart.shopping.adapter.content_listing_object import ArticleContentListingObject as Base
        self.assertTrue(issubclass(ArticleContentListingObject, Base))

    def test_verifyObject(self):
        from zope.interface.verify import verifyObject
        article = self.create_content('collective.cart.core.Article')
        instance = IContentListingObject(article)
        self.assertTrue(verifyObject(IContentListingObject, instance))

    def test__repr_(self):
        article = self.create_content('collective.cart.core.Article')
        instance = IContentListingObject(article)
        self.assertEqual(instance.__repr__(), '<slt.content.adapter.content_listing_object.ArticleContentListingObject instance at /plone/collective-cart-core-article>')

    def test_feed_order(self):
        article = self.create_content('collective.cart.core.Article')
        instance = IContentListingObject(article)
        self.assertEqual(instance.feed_order(), u'Edit')

        instance._realobject.feed_order = 3
        self.assertEqual(instance.feed_order(), 3)
