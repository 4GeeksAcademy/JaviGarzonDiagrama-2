from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Integer, ForeignKey, Enum
from sqlalchemy.orm import relationship


db = SQLAlchemy()

class Usuario(db.Model):
    __tablename__ = 'user'
    
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True)
    firstname = Column(String(50), nullable=False)
    secondname = Column(String(50), nullable=False)
    email = Column(String(50), unique=True, nullable=False)

    comments = relationship('Comment', backref='user', lazy=True)

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "firstname": self.firstname,
            "secondname": self.secondname,
            "email": self.email,
        }

class Comment(db.Model):
    __tablename__ = 'comment'
    
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(200), nullable=False)
    author_id = Column(Integer, ForeignKey('User.id'), nullable=False)
    post_id = Column(Integer, ForeignKey('Post.id'), nullable=False)  # Se asume que existe un modelo Post
    
    comment = relationship('Comentario', backref='post', lazy=True)

    def serialize(self):
        return {
            "id": self.id,
            "comment_text": self.comment_text,
            "author": self.author_id, 
            "post": self.post_id, 
        }
    
class Comentario (db.Model):
    __tablename__ = 'post'  
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('User.id'), nullable=False)
    
    post = relationship('Comentario', backref='post', lazy=True)

def serialize(self):
        return {
            "id": self.id,
            "id": self.user_id,            
        }

class Media (db.Model):
    __tablename__ = 'Media'  
    id = Column(Integer, primary_key=True)
    type= Column(Enum, nullable=False)
    url = Column(String(100), nullable=False)
    post_id = Column(Integer, ForeignKey('Post.id'), nullable=False)

def serialize(self):
        return {
            "id": self.id,
            "type": self.type, 
            "url": self.url,
            "post": self.post,           
        }