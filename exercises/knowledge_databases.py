from knowledge_model import Base, Knowledge

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_article(article_name, topic, rating):
	My_knowledge = 	Knowledge(
		article_name = article_name,
		topic = topic,
		rating = rating)
		session.add(My_knowledge)
		session.commit()
add_article("dance", "dancing and personalities", 7 )

def query_all_articles():
	pass

def query_article_by_topic():
	pass

def delete_article_by_topic():
	pass

def delete_all_articles():
	pass

def edit_article_rating():
	pass
