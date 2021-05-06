import lucene
import json
from org.apache.lucene.queryparser.classic import QueryParser, MultiFieldQueryParser
from org.apache.lucene.index import IndexWriter, IndexWriterConfig, DirectoryReader
from org.apache.lucene.document import Document, Field, StringField, TextField
from org.apache.lucene.analysis.standard import StandardAnalyzer
from org.apache.lucene.store import SimpleFSDirectory
from org.apache.lucene.search import IndexSearcher
from java.io import StringReader
from java.nio.file import Paths
from Tkinter import *


# ---------------------------------------------> Lucene ------------------------------------------------------
class Lucene(object):

    def __init__(self):
        pp = Paths.get("lucene_index")
        self.store = SimpleFSDirectory(pp)
        # --------------------------------> Se abre el archivo JSON.
        f = open('files.json')
        # --------------------------------> Se regresa un JSON.
        self.documents = json.load(f)

    def index_documents(self, docs):
        analyzer = self.getAnalyzer()
        index_writer_config = IndexWriterConfig(analyzer)
        index_writer_config.setOpenMode(IndexWriterConfig.OpenMode.CREATE)
        index_writer = IndexWriter(self.store, index_writer_config)
        for doc in docs:
            index_writer.addDocument(doc)
        index_writer.commit()

    def getAnalyzer(self):
        return StandardAnalyzer()

    def search_content(self, query):
        reader = DirectoryReader.open(self.store)
        index_searcher = IndexSearcher(reader)
        query = QueryParser("content", self.getAnalyzer()).parse(query["content"])
        result = index_searcher.search(query, 10)
        return result
    
    def search_title(self, query):
        reader = DirectoryReader.open(self.store)
        index_searcher = IndexSearcher(reader)
        query = QueryParser('title', self.getAnalyzer()).parse(query['title'])
        result = index_searcher.search(query, 10)
        return result
    
    def close(self):
        self.store.close()

    def instantiate(self):
        doc = []
        for index in range(len(self.documents['documents'][0])):
            name = "document"+str(index+1)
            doc.append(Document())
            doc[index].add(Field('title', self.documents['documents'][0][name]["title"], TextField.TYPE_STORED))
            doc[index].add(Field("docid", self.documents['documents'][0][name]["docid"], StringField.TYPE_NOT_STORED))
            doc[index].add(Field("journalist", self.documents['documents'][0][name]["journalist"], TextField.TYPE_NOT_STORED))
            doc[index].add(Field("content", self.documents['documents'][0][name]["content"],TextField.TYPE_NOT_STORED))
        return doc
# ------------------------------------------------------------------------------------------------------------


# ---------------------------------------------> Menu --------------------------------------------------------
class bcolors:

    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Menu(object):

    def print_menu(self):
        print('')
        print(bcolors.WARNING + '██████╗ ██╗   ██╗███████╗ ██████╗ █████╗ ██████╗  ██████╗ ██████╗')
        print(bcolors.WARNING + '██╔══██╗██║   ██║██╔════╝██╔════╝██╔══██╗██╔══██╗██╔═══██╗██╔══██╗')
        print(bcolors.WARNING + '██████╔╝██║   ██║███████╗██║     ███████║██║  ██║██║   ██║██████╔╝')
        print(bcolors.OKCYAN + '██╔══██╗██║   ██║╚════██║██║     ██╔══██║██║  ██║██║   ██║██╔══██╗')
        print(bcolors.OKCYAN + '██████╔╝╚██████╔╝███████║╚██████╗██║  ██║██████╔╝╚██████╔╝██║  ██║')
        print(bcolors.OKCYAN + '╚═════╝  ╚═════╝ ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚═╝  ╚═╝')
        print(bcolors.OKGREEN+'|')
        print(bcolors.OKGREEN+'|')
        print(bcolors.OKGREEN+' \ Introduce la palabra a buscar --> '),
        try:
            item = raw_input()
        except:
            print('Introduce una cadena valida')
        return item
# ------------------------------------------------------------------------------------------------------------


# ---------------------------------------------> Main --------------------------------------------------------
if __name__ == "__main__":

    lucene.initVM()
    proto = Lucene()
    docs = []
    docs = proto.instantiate()
    proto.index_documents(docs)
    while True:
    
        m = Menu()
        item = m.print_menu()
        print('En el título: ')
        result = proto.search_title({'title': item})
        for doc in result.scoreDocs:
            print(doc)
        print('En el contenido: ')
        result = proto.search_content({'content': item})
        for doc in result.scoreDocs:
            print(doc)

    
# ------------------------------------------------------------------------------------------------------------