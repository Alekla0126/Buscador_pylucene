import lucene
from org.apache.lucene.queryparser.classic import QueryParser, MultiFieldQueryParser
from org.apache.lucene.index import IndexWriter, IndexWriterConfig, DirectoryReader
from org.apache.lucene.document import Document, Field, StringField, TextField
from org.apache.lucene.analysis.standard import StandardAnalyzer
from org.apache.lucene.store import SimpleFSDirectory
from org.apache.lucene.search import IndexSearcher
from java.io import StringReader
from java.nio.file import Paths


# ---------------------------------------------> Lucene ------------------------------------------------------
class Lucene(object):

    def __init__(self):
        pp = Paths.get("lucene_index")
        self.store = SimpleFSDirectory(pp)

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

    def search(self, query):
        reader = DirectoryReader.open(self.store)
        index_searcher = IndexSearcher(reader)
        query = QueryParser("content", self.getAnalyzer()).parse(query["content"])
        result = index_searcher.search(query, 10)
        return result
    
    def close(self):
        self.store.close()

    def instantiate(self):
        doc = []
        doc.append(Document())
        doc[0].add(Field('title', 'Software Engineering, Master of Science',
                       TextField.TYPE_STORED))
        doc[0].add(Field("docid", "1", StringField.TYPE_NOT_STORED))
        # doc[0].add(Field("journalist", "Ivana Kottasová", TextField.TYPE_NOT_STORED))
        doc[0].add(Field("content",
                       StringReader('''Most innovations in the automotive sector have been based on electronics and software. 
                       Developments such as mobility services, autonomous driving or automated driving, networking, infotainment 
                       and e-mobility contribute significantly to the industry. With the number of software-controlled functions 
                       in an automatic car, its IT architecture is also changing towards central, virtual high-speed computers. 
                       Our goal is to provide students with the most the state-of-the-art technology that will enable them to work 
                       and innovate in the automotive domain and any other business domain available in the market today.'''),
                       TextField.TYPE_NOT_STORED))

        doc.append(Document())
        doc[1].add(Field('title', 'Master in Computer Science and Software Engineering',
                       TextField.TYPE_STORED))
        doc[1].add(Field("docid", "2", StringField.TYPE_NOT_STORED))
        # doc[1].add(Field("journalist", "Melissa Bell, Stephanie Halasz", TextField.TYPE_NOT_STORED))
        doc[1].add(Field("content",
                       StringReader('''The SIT program is flexible and adapted to many different individual situations. 
                       It is available both onsite in Schaffhausen and in an online offering, as well as any onsite-online 
                       combination. It offers qualified students attractive scholarships and the possibility of a second year 
                       in one of our partner universities in Europe, the USA, and Asia.'''),
                       TextField.TYPE_NOT_STORED))

        doc.append(Document())
        doc[2].add(Field('title', 'M.Sc. in Computing',
                       TextField.TYPE_STORED))
        doc[2].add(Field("docid", "3", StringField.TYPE_NOT_STORED))
        # doc[2].add(Field("journalist", "George Ramsay", TextField.TYPE_NOT_STORED))
        doc[2].add(Field("content",
                       StringReader('''The term “software engineering” was coined in 1968, during the NATO conference in Garmish. 
                       It was used in response to the problems associated with a software development that then still young IT 
                       sector was facing. Although more than 40 years have passed, the software development in many IT companies 
                       is still chaotic. Software is frequently delivered after the deadline, it costs much more than anticipated 
                       at the beginning, developers are often forced to work over-hours, and despite all these efforts, the 
                       software that is delivered does not meet customer needs and contains too many defects. The goal of Software 
                       Engineering as a discipline, is to deliver solutions that can be used to mitigate the problems associated with 
                       the software development by applying engineering methods to its development. Since 1998, Poznan University of 
                       Technology offers a M.Sc. program in Software Engineering. The curriculum aims at providing graduates with the 
                       necessary knowledge and skills to perform three important roles in IT projects:
                       Project Manager – project management methodologies, risk management, planning (size and effort estimation of 
                       software development);
                       Analyst – business process modeling, elicitation of functional and non-functional requirements 
                       for information systems, and preparation of acceptance tests;
                       Architect, senior developer – object-oriented design, software architectures, real-time systems, 
                       and software testing.'''),
                       TextField.TYPE_NOT_STORED))
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
        item = raw_input()
        return item
# ------------------------------------------------------------------------------------------------------------

# ---------------------------------------------> Main --------------------------------------------------------
if __name__ == "__main__":
    lucene.initVM()
    proto = Lucene()
    docs = []
    docs = proto.instantiate()
    proto.index_documents((docs[0], docs[1], docs[2]))
    m = Menu()
    item = m.print_menu()
    result = proto.search({'content': item})
    for doc in result.scoreDocs:
        print(doc)
    proto.close()