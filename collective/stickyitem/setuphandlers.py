from zope.component import getSiteManager
from zope.component import getGlobalSiteManager
from collective.stickyitem.schemaextender import SortingDate


def uninstall(context):
    """ Do customized uninstallation.
    """
    if context.readDataFile('stickyitem_uninstall.txt') is None:
        return
    site = context.getSite()
    lsm = getSiteManager(site)
    gsm = getGlobalSiteManager()
    if lsm == gsm:
        return
    unregistered = []
    registrations = tuple(lsm.registeredAdapters())
    for registration in registrations:
        factory = registration.factory
        if factory == SortingDate:
            required = registration.required
            provided = registration.provided
            name = registration.name
            lsm.unregisterAdapter(factory=factory,
                required=required, provided=provided, name=name)
            unregistered.append(str(required))


