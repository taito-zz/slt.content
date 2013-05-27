===========
slt.content
===========

This package contains content types for SLT shopping site.

Changelog
---------

0.13 (2013-05-27)
=================

- Added fields for registered member discount. [taito]

0.12.4 (2013-05-18)
===================

- Fixed upgrade step. [taito]

0.12.3 (2013-05-17)
===================

- Fixed upgrade step. [taito]

0.12.2 (2013-05-07)
===================

- Cosmetics. [taito]

0.12.1 (2013-05-07)
===================

- Updated upgrade step. [taito]

0.12 (2013-05-03)
=================

- Added upgrade step. [taito]

0.11 (2013-04-30)
=================

- Removed dependency from five.grok. [taito]

0.10 (2013-04-11)
=================

- Moved test packaged to extras_require. [taito]
- Added attribute: registration_number to content type: collective.cart.core.Cart. [taito]

0.9 (2013-03-20)
================

- Specified adaptable context to ICart to avoid conflict error. [taito]

0.8 (2013-03-18)
================

- Overrode method: link_to_order_for_customer of adapter ShoppingMethod from package: collective.cart.shopping. [taito]

0.7 (2013-03-18)
================

- Covered tests. [taito]
- Tested with Plone-4.2.5. [taito]

0.6.1 (2013-03-12)
==================

- Updated translations. [taito]

0.6 (2013-03-12)
================

- Removed unnecessary modules. [taito]

0.5 (2013-01-30)
================

- Updated permission to edit Member Area. [taito]

0.4 (2012-12-20)
================

- Added field: feed_order to content type: collective.cart.core.Artilce for ordering top page feed. [taito]

0.3 (2012-11-26)
================

- Added upgrade step to set global_allow True for collective.cart.core.Artilce.
  [taito]
- Added testing integration to Travis CI. [taito]

0.2 (2012-11-13)
================

- Added upgrade step to add collective.cart.shopping.CustomerInfo
  to allowed_content_types of slt.content.MemberArea.
  [taito]

0.1 (2012-10-15)
================

- Initial release. [taito]
