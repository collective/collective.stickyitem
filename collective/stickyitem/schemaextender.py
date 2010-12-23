from Products.Archetypes.public import DateTimeField, CalendarWidget
from Products.ATContentTypes.interfaces import IATNewsItem
from archetypes.schemaextender.interfaces import ISchemaExtender
from archetypes.schemaextender.field import ExtensionField
from plone.indexer.decorator import indexer
from zope.interface import implements
from zope.i18nmessageid import MessageFactory

_ = MessageFactory('collective.stickyitem')



@indexer(IATNewsItem)
def my_effective(object, **kw):
    return getattr(object, 'sortingdate', None) or object.effective()


class SortingDateField(ExtensionField, DateTimeField):
    """
    """


class SortingDate(object):
    implements(ISchemaExtender)

    _fields = [
        SortingDateField("sortingdate",
            schemata = "default",
            default_method = "effective",
            widget = CalendarWidget(
                ),
            ),

        ]


    def __init__(self, context):
        self.context = context

    def getFields(self):
        return self._fields
