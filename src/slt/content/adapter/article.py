from collective.cart.shopping.adapter.article import ArticleAdapter as BaseArticleAdapter
from slt.content.interfaces import IArticle
from slt.content.interfaces import IDiscountBehavior
from zope.component import adapts


class ArticleAdapter(BaseArticleAdapter):
    """Adapter for content type: collective.cart.core.Article"""
    adapts(IArticle)

    def _registered_member_discount_available(self):
        """Returns True if discount for registered member is available else False

        :rtype: bool
        """
        member = self.context.restrictedTraverse('@@plone_portal_state').member()
        if member.getProperty('registration_number'):
            behavior = IDiscountBehavior(self.context)
            if behavior.registered_member_discount_enabled:
                if behavior.registered_member_discount_price:
                    return True
        return False

    def discount_available(self):
        """Returns True if discount is available else False

        :rtype: bool
        """
        if super(ArticleAdapter, self).discount_available():
            return True
        elif self._registered_member_discount_available():
            return True
        else:
            return False

    def discount_end(self):
        """Returns localized date for discount end"""
        if not self._registered_member_discount_available() and super(ArticleAdapter, self).discount_available():
            return super(ArticleAdapter, self).discount_end()

    def _registered_member_discount_less_than_termed_discount(self):
        """Returns True if registered member discount is available and it is less than termed discount else False

        :rtype: bool
        """
        money = super(ArticleAdapter, self).gross()
        discount_money = IDiscountBehavior(self.context).registered_member_discount_money
        return self._registered_member_discount_available() and money > discount_money

    def gross(self):
        """Returns gross money

        :rtype: moneyed.Money
        """
        if self._registered_member_discount_less_than_termed_discount():
            return IDiscountBehavior(self.context).registered_member_discount_money
        else:
            return super(ArticleAdapter, self).gross()
        # money = super(ArticleAdapter, self).gross()
        # discount_money = IDiscountBehavior(self.context).registered_member_discount_money

        # if self._registered_member_discount_available() and money > discount_money:
        #     money = discount_money

        # return money
