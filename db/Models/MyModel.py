import edgedb
from db.edbw.EdgeDBModel import EdgeDBModel
from db.edbw.Properties import Type
import pprint
pp = pprint.PrettyPrinter(indent=4)

client = edgedb.create_client()

InvoicesModel = EdgeDBModel(modelName='Invoices', client=client)
InvoicesModel.addProperty(_propertyName = 'three_word_name', _propertyType = Type.str, _req = True)

#InvoicesModel.getByProperty(printStr=True, propName='three_word_name', propType=Type.str, _three_word_name='TameHolographcScallop')

#InvoicesModel.insert(printStr=True, _three_word_name="hello world")

#InvoicesModel.updateEntry(uuid="123",printStr=True, title="blade runner")

#InvoicesModel.delEntry(uuid="123", printStr=True)