from collective.cart.shopping.adapter.content_listing_object import ArticleContentListingObject as BaseArticleContentListingObject
from slt.content.interfaces import IArticle
from zope.component import adapts


class ArticleContentListingObject(BaseArticleContentListingObject):
    adapts(IArticle)

    def __repr__(self):
        return "<slt.content.adapter.content_listing_object.ArticleContentListingObject instance at {}>".format(self.getPath())

    def feed_order(self):
        """Return feed order

        :rtype: int
        """
        return self._realobject.feed_order
