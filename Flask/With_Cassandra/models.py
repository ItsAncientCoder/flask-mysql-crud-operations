from app_config import db

import uuid
import datetime as dt

class t_advance_search(db.Model):
#     __tablename__ = 't_advance_search';
#     __keyspace__ = 'ticketing_mobile';
    email = db.columns.Text(primary_key=True);
    id = db.columns.UUID(primary_key=True, default=uuid.uuid4);
    search_name = db.columns.Text();
    search_query = db.columns.Text();
    last_modified_time = db.columns.DateTime(default=dt.datetime.utcnow());
    
    def toJson(self):
        return {'id': self.id, 'email': self.email, 'search_name': self.search_name, 
                'search_query': self.search_query, 'last_modified_time': self.last_modified_time};
    def __str__(self):
        return '{0}'.format({'id': self.id, 'email': self.email, 'search_name': self.search_name, 
                'search_query': self.search_query, 'last_modified_time': self.last_modified_time});