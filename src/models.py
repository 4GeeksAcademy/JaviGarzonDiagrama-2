from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Integer, ForeignKey, Enum
from sqlalchemy.orm import relationship


db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'users'  # Cambié el nombre de la tabla para evitar conflictos

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
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
    __tablename__ = 'comments'  # Cambié el nombre de la tabla

    id = Column(Integer, primary_key=True)
    comment_text = Column(String(200), nullable=False)
    author_id = Column(Integer, ForeignKey('users.id'), nullable=False)  # Referencia corregida
    post_id = Column(Integer, ForeignKey('posts.id'), nullable=False)  # Asegúrate de que 'posts' es el nombre correcto

    post = relationship('Post', backref='comments', lazy=True)  # Ahora dentro de la clase

    def serialize(self):
        return {
            "id": self.id,
            "comment_text": self.comment_text,
            "author": self.user.serialize(),  # Serializa al usuario
            "post_id": self.post_id
        }
    
class Post (db.Model):
    __tablename__ = 'post'  
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    
    post = relationship('Comment', backref='Comment', lazy=True)

def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,            
        }

class Media (db.Model):
    __tablename__ = 'Media'  
    id = Column(Integer, primary_key=True)
    type= Column(Enum, nullable=False)
    url = Column(String(100), nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'), nullable=False)

def serialize(self):
        return {
            "id": self.id,
            "type": self.type, 
            "url": self.url,
            "post": self.post_id,           
        }