from scraper_library import Scraper
import os

class Scraper_pubmed(Scraper):
	
	def __init__(self,**kwargs):
		Scraper.__init__(self)
		self.base_url = "https://www.ncbi.nlm.nih.gov/pubmed/{}?report=abstract&format=text"
		self.files_names = 'abstract_{}.txt'
		self.directorio = 'Abstracts'
		self.files_path = os.path.join(os.getcwd(), self.directorio)
