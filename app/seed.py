import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app, db
from app.models import Guest, Episode
app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    guest1 = Guest(name="Michael J. Fox", occupation="actor")
    guest2 = Guest(name="Sandra Bernhard", occupation="Comedian")
    guest3 = Guest(name="Tracey Ullman", occupation="television actress")

    ep1 = Episode(date="1/11/99", number=1)
    ep2 = Episode(date="1/12/99", number=2)

    db.session.add_all([guest1, guest2, guest3, ep1, ep2])
    db.session.commit()
