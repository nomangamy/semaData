from extensions import db 

class DomainOwner(db.Model):
    id = db.Column(db.Integer,primary_key=True) 
    owner_name = db.Column(db.String(100),unique =True,nullable = False)
    owner_email = db.Column(db.String(200),nullable=False,unique =True)
    owner_phone = db.Column(db.String(15),nullable=False,unique=True)
    owner_address = db.Column(db.String(300),nullable=False,unique=False)
    domain_field = db.Column(db.String(200),nullable=False,unique=False)
    reference_number = db.Column(db.String(100),nullable=False,unique=True)

    def __repr__(self):
        return f"DomainOwner('{self.owner_id})'"
