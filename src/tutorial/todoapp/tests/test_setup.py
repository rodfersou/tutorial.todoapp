# -*- coding: utf-8 -*-
"""Setup/installation tests for this package."""

from tutorial.todoapp.tests.base import IntegrationTestCase
from plone import api

import unittest2 as unittest


class TestInstall(IntegrationTestCase):
    """Test installation of tutorial.todoapp into Plone."""

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']

    def test_product_installed(self):
        """Test if tutorial.todoapp is installed in portal_quickinstaller."""
        installer = api.portal.get_tool('portal_quickinstaller')
        self.assertTrue(installer.isProductInstalled('tutorial.todoapp'))

    def test_uninstall(self):
        """Test if tutorial.todoapp is cleanly uninstalled."""
        installer = api.portal.get_tool('portal_quickinstaller')
        installer.uninstallProducts(['tutorial.todoapp'])
        self.assertFalse(installer.isProductInstalled('tutorial.todoapp'))

    # metadata.xml
    def test_dependencies_installed(self):
        """Test that all dependencies are installed."""
        installer = api.portal.get_tool('portal_quickinstaller')
        self.assertTrue(installer.isProductInstalled('plone.app.dexterity'))

    # types/todo_item.xml
    def test_todo_item_installed(self):
        """Test that Todo Item content type is listed in portal_types."""
        types = api.portal.get_tool('portal_types')
        self.assertIn('todo_item', types.objectIds())

    # workflows/todo_item_workflow/definition.xml
    def test_todo_item_workflow_installed(self):
        """"Test that todo_item_workflow is listed in portal_workflow."""
        workflow = api.portal.get_tool('portal_workflow')
        self.assertIn('todo_item_workflow', workflow.objectIds())

    # workflows.xml
    def test_todo_item_workflow(self):
        """Test if todo_item is present and mapped to Todo Item content type."""
        workflow = api.portal.get_tool('portal_workflow')
        for portal_type, chain in workflow.listChainOverrides():
            if portal_type in ('todo_item', ):
                self.assertEquals(('todo_item_workflow',), chain)


def test_suite():
    """This sets up a test suite that actually runs the tests in the class
    above."""
    return unittest.defaultTestLoader.loadTestsFromName(__name__)
