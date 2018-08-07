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


def query_all_articles():
	knowledge = session.query(Knowledge).all()
	return knowledge
	

def query_article_by_topic(their_topic):
	knowledge = session.query(Knowledge).filter_by(topic=their_topic).first()
	return knowledge

def delete_article_by_topic(topic):
	session.query(Knowledge).filter_by(topic=topic).delete()
	session.commit()

def delete_all_articles():
	session.query(Knowledge).delete()
	session.commit()

def edit_rating(updated_rating, article_title):
	knowledge_object = session.query(
		Knowledge).filter_by(article_name=article_title)
	knowledge_object.rating=updated_rating
	session.commit()


def edit_article_rating():	
	pass

def delete_article_by_rating(threshold):
	session.query(Knowledge).filter(Knowledge.rating<threshold).delete()
	session.commit()


# add_article("dance", "dancing and personalities", 7 )
edit_rating(9,"dance")
print(query_all_articles())
(query_article_by_topic("dancing and peersonalities"))
delete_article_by_topic("dancing and peersonalities")
delete_all_articles()
delete_article_by_rating(10)



