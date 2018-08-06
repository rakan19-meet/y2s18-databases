from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Knowledge(Base):
	__tablename__ = "knowledge"
	id = Column(Integer, primary_key = True)
	article_name = Column(String)
	topic = Column (String)
	rating = Column(Integer)

	def __repr__(self):
		return("id:{}\n"
			   "article name :{}\n"
			   "topic:{}\n"
			   "rating:{}").format(
				   self.id, self.article_name, self.topic, self.rating)
a = knowledge(article_name ="dance", topic = "dancing and personalities" rating = 7)
b = knowledge(article_name = "engineer", topic = "engineering in life", rating = 9)
c = knowledge(article_name = "politics", topic = "politics on a daily basis", rating = 8)
		
	





		
	# Create a table with 4 columns
	# The first column will be the primary key
	# The second column should be a string representing
	# the name of the Wiki article that you're referencing
	# The third column will be a string representing the 
	# topic of the article. The last column will be
	# an integer, representing your rating of the article.

	pass