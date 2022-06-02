
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_moment import Moment
from datetime import datetime


db = SQLAlchemy()

#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#

class Venue(db.Model):
    __tablename__ = 'Venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    address = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    genres = db.Column(db.ARRAY(db.String), nullable=False)
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    website_link = db.Column(db.String(120))
    seeking_talent = db.Column(db.Boolean, default=False)
    seeking_description = db.Column(db.String(120))
    show = db.relationship('Show', backref=db.backref('venue', lazy='joined'), lazy='joined')
    
    def __repr__(self):
      return f'<Venue {self.id} {self.name} {self.city} {self.state}>'
    

    
class Show(db.Model):
      __tablename__ = 'Show'
      
      id = db.Column(db.Integer, primary_key=True)
      venue_id = db.Column(db.Integer, db.ForeignKey('Venue.id'))
      artist_id = db.Column(db.Integer, db.ForeignKey('Artist.id'))  
      start_time = db.Column(db.DateTime, default=datetime.now())    
        
      def __repr__(self):
          return f'<Show {self.id} {self.venue_id} {self.artist_id} {self.start_time}>'

class Artist(db.Model):
    __tablename__ = 'Artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    phone = db.Column(db.String(120))    
    genres = db.Column(db.ARRAY(db.String), nullable=False)
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    website_link = db.Column(db.String(120))
    seeking_venue = db.Column(db.Boolean, default=False)
    seeking_description = db.Column(db.String(120))
    show = db.relationship('Show', backref=db.backref('artist', lazy='joined'), lazy='joined')
    
    def __repr__(self):
          return f'<Artist {self.id} {self.name} {self.city} {self.state}>'


    

    