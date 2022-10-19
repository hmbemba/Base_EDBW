import edgedb
from db.edbw.EdgeDBModel import EdgeDBModel
from db.edbw.Properties import Type
import pprint
import os
from dotenv import load_dotenv

pp = pprint.PrettyPrinter(indent=4)
load_dotenv()

localClient = edgedb.create_client()
remoteClient = edgedb.create_client(dsn=os.eviron['DSN'], tls_security='insecure')

InvoicesModel = EdgeDBModel(modelName='Invoices', client=localClient )#remoteClient)
InvoicesModel.addProperty(_propertyName = 'three_word_name', _propertyType = Type.str, _req = True)

#InvoicesModel.getByProperty(printStr=True, propName='three_word_name', propType=Type.str, _three_word_name='TameHolographcScallop')

#InvoicesModel.insert(printStr=True, _three_word_name="hello world")

#InvoicesModel.updateEntry(uuid="123",printStr=True, title="blade runner")

#InvoicesModel.delEntry(uuid="123", printStr=True)