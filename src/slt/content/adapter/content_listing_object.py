from Acquisition import aq_get
from plone.app.contentlisting.catalog import CatalogContentListingObject
from plone.app.contentlisting.realobject import RealContentListingObject
from plone.app.contentlisting.interfaces import IContentListingObject
from slt.content.interfaces import IArticle
from zope.component import adapts
from zope.interface import implements
from collective.cart.shopping.interfaces import IArticleAdapter


class FeedToShopTopContentListingObject(RealContentListingObject):
    adapts(IArticle)

    def __repr__(self):
        return "<slt.content.adapter.content_listing_object.FeedToShopTopContentListingObject instance at {}".format(self.getPath())

    def is_discount(self):
        return IArticleAdapter(self._realobject).discount_available()

    def klass(self):
        if self.is_discount():
            return 'discount'
        else:
            return 'normal'

    def feed_order(self):
        return self._realobject.feed_order
