from Products.Archetypes.public import DateTimeField, CalendarWidget
from archetypes.schemaextender.interfaces import ISchemaExtender
from archetypes.schemaextender.field import ExtensionField
from plone.indexer.decorator import indexer
from zope.component import adapts
from zope.interface import implements, Interface
from zope.i18nmessageid import MessageFactory

_ = MessageFactory('collective.stickyitem')


class IStickyItem(Interface):
    """ Marker for sticky item news item
    """


@indexer(IStickyItem)
def my_effective(object, **kw):
    return getattr(object, 'sortingdate', None) or object.effective()


class SortingDateField(ExtensionField, DateTimeField):
    """
    """


class SortingDate(object):
    adapts(IStickyItem)
    implements(ISchemaExtender)

    _fields = [
        SortingDateField("sortingdate",
            schemata="dates",
            widget=CalendarWidget(
                    label=_(u'label_sortingdate', default=u'Sorting Date'),
                ),
            ),

        ]

    def __init__(self, context):
        self.context = context

    def getFields(self):
        return self._fields
