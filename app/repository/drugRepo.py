from app.database import db
from app.repository.baseRepo import BaseRepo
from app.models.drugs import Drugs

class drugRepo(BaseRepo):
    model = Drugs
