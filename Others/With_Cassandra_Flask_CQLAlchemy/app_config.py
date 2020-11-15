from flask import Flask
from flask_cqlalchemy import CQLAlchemy
from cassandra.auth import PlainTextAuthProvider

app = Flask(__name__)
app.config['CASSANDRA_HOSTS'] = ['entsdseidc01-env2.idc1.level3.com']
app.config['CASSANDRA_KEYSPACE'] = "ticketing_mobile"
app.config['CASSANDRA_LAZY_CONNECT'] = True
app.config['CASSANDRA_RETRY_CONNECT'] = True
app.config['CASSANDRA_CONSISTENCY'] = 4

app.config['ENV'] = 'development'
app.config['DEBUG'] = True

CASSANDRA_SETUP_KWARGS = {'protocol_version': 3, "auth_provider": PlainTextAuthProvider(
    username='ticketing_mobile', password='T1ck_M0$Te$T'), 'connect_timeout':10000, 'control_connection_timeout': None}

app.config['CASSANDRA_SETUP_KWARGS'] = CASSANDRA_SETUP_KWARGS

db = CQLAlchemy(app);
logger = app.logger;

with app.app_context():
    import routes;