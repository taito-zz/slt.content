from setuptools import find_packages
from setuptools import setup


setup(
    name='slt.content',
    version='0.18.1',
    description="Provides content types for SLT shopping site.",
    long_description=open("README.rst").read(),
    classifiers=[
        "Framework :: Plone",
        "Framework :: Plone :: 4.3",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7"],
    keywords='',
    author='Taito Horiuchi',
    author_email='taito.horiuchi@abita.fi',
    url='https://github.com/taito/slt.content',
    license='None-free',
    packages=find_packages('src', exclude=['ez_setup']),
    package_dir={'': 'src'},
    namespace_packages=['slt'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'collective.cart.shopping',
        'plone.app.dexterity [relations]',
        'setuptools'],
    extras_require={'test': ['Products.CMFPlacefulWorkflow', 'hexagonit.testing']},
    entry_points="""
    # -*- Entry points: -*-

    [z3c.autoinclude.plugin]
    target = plone
    """)
