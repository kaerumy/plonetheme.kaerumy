# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plonetheme.kaerumy.testing import (  # noqa: E501
    PLONETHEME_KAERUMY_INTEGRATION_TESTING,
)

import unittest


try:
    from Products.CMFPlone.utils import get_installer
except ImportError:
    get_installer = None


class TestSetup(unittest.TestCase):
    """Test that plonetheme.kaerumy is properly installed."""

    layer = PLONETHEME_KAERUMY_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        if get_installer:
            self.installer = get_installer(self.portal, self.layer["request"])
        else:
            self.installer = api.portal.get_tool("portal_quickinstaller")

    def test_product_installed(self):
        """Test if plonetheme.kaerumy is installed."""
        self.assertTrue(self.installer.is_product_installed("plonetheme.kaerumy"))

    def test_browserlayer(self):
        """Test that IPlonethemeKaerumyLayer is registered."""
        from plone.browserlayer import utils
        from plonetheme.kaerumy.interfaces import IPlonethemeKaerumyLayer

        self.assertIn(IPlonethemeKaerumyLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = PLONETHEME_KAERUMY_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        if get_installer:
            self.installer = get_installer(self.portal, self.layer["request"])
        else:
            self.installer = api.portal.get_tool("portal_quickinstaller")
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
        self.installer.uninstall_product("plonetheme.kaerumy")
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if plonetheme.kaerumy is cleanly uninstalled."""
        self.assertFalse(self.installer.is_product_installed("plonetheme.kaerumy"))

    def test_browserlayer_removed(self):
        """Test that IPlonethemeKaerumyLayer is removed."""
        from plone.browserlayer import utils
        from plonetheme.kaerumy.interfaces import IPlonethemeKaerumyLayer

        self.assertNotIn(IPlonethemeKaerumyLayer, utils.registered_layers())
