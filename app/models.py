from werkzeug.security import generate_password_hash,check_password_hash
from . import login_manager
from datetime import datetime
from flask_login import UserMixin
from app import db


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
    
class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True, index = True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String()) 
    pass_secure = db.Column(db.String(255))
    providers = db.relationship('Providers',backref = 'author',lazy = 'dynamic') 

    @property
    def password(self):
        raise AttributeError("You can't read the password attribute")

    @password.setter
    def password(self,password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def save_user(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'User{self.username}'

class Providers(db.Model):
    __tablename__='providers'

    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(255))
    content = db.Column(db.String(2550))
    date_posted = db.Column(db.DateTime, default = datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    reviews = db.relationship('Reviews', backref = 'author', lazy = True) 

    def save_provider(self):
        db.session.add(self)
        db.session.commit()
    

    def __repr__(self):
        return f'Providers{self.title}'


class Reviews(db.Model):
    __tablename__ = 'reviews'

    id = db.Column(db.Integer,primary_key = True)
    review = db.Column(db.String(255))
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    provider_id = db.Column(db.Integer,  db.ForeignKey("providers.id"))

    def save_review(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'Review{self.review}'


    @classmethod
    def get_reviews(cls,id):
        reviews = Review.query.filter_by(providers_id=id).all()
        return reviews
        
    @classmethod
    def clear_reviews(cls):
        Review.all_reviews.clear()

    @classmethod
    def get_reviews(cls,id):

        response = []


        for review in cls.all_reviews:
            if review.provider_id == id:
                response.append(review)

        return response
class Catering:
    __tablename__='catering'

    id = db.Column(db.Integer,primary_key=True)
    location = db.Column(db.Integer)
    company = db.Column(db.String(255))
    service = db.Column(db.String(2550))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    reviews = db.relationship('Reviews', backref = 'author', lazy = True) 

    def save_catering(self):
        db.session.add(self)
        db.session.commit()
    

    def __repr__(self):
        return f'Catering({self.company},{self.service})'

class Grounds:
    __tablename__='grounds'

    id = db.Column(db.Integer,primary_key=True)
    location = db.Column(db.Integer)
    company = db.Column(db.String(255))
    service = db.Column(db.String(2550))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    reviews = db.relationship('Reviews', backref = 'author', lazy = True) 

    def save_grounds(self):
        db.session.add(self)
        db.session.commit()
    

    def __repr__(self):
        return f'Grounds({self.company},{self.service})'

class Cars:
    __tablename__='cars'

    id = db.Column(db.Integer,primary_key=True)
    location = db.Column(db.Integer)
    company = db.Column(db.String(255))
    service = db.Column(db.String(2550))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    reviews = db.relationship('Reviews', backref = 'author', lazy = True) 

    def save_cars(self):
        db.session.add(self)
        db.session.commit()
    

    def __repr__(self):
        return f'Cars({self.company},{self.service})'

class Photography:
    __tablename__='photography'

    id = db.Column(db.Integer,primary_key=True)
    location = db.Column(db.Integer)
    company = db.Column(db.String(255))
    service = db.Column(db.String(2550))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    reviews = db.relationship('Reviews', backref = 'author', lazy = True) 

    def save_photography(self):
        db.session.add(self)
        db.session.commit()
    

    def __repr__(self):
        return f'Photography({self.company},{self.service})'

class Tents:
    __tablename__='tents'

    id = db.Column(db.Integer,primary_key=True)
    location = db.Column(db.Integer)
    company = db.Column(db.String(255))
    service = db.Column(db.String(2550))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    reviews = db.relationship('Reviews', backref = 'author', lazy = True) 

    def save_tents(self):
        db.session.add(self)
        db.session.commit()
    

    def __repr__(self):
        return f'Tents({self.company},{self.service})'

class Music:
    __tablename__='music'

    id = db.Column(db.Integer,primary_key=True)
    location = db.Column(db.Integer)
    company = db.Column(db.String(255))
    service = db.Column(db.String(2550))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    reviews = db.relationship('Reviews', backref = 'author', lazy = True) 

    def save_music(self):
        db.session.add(self)
        db.session.commit()
    

    def __repr__(self):
        return f'Music({self.company},{self.service})'


