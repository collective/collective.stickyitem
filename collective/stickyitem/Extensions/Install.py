from Products.CMFCore.utils import getToolByName


def install(self):
    setup_tool = getToolByName(self, 'portal_setup')
    setup_tool.runAllImportStepsFromProfile('profile-collective.stickyitem:default')
    return "Imported install profile."


def uninstall(self):
    setup_tool = getToolByName(self, 'portal_setup')
    setup_tool.runAllImportStepsFromProfile('profile-collective.stickyitem:uninstall')
    return "Imported uninstall profile."
