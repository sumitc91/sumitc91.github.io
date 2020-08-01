from upload_file.app import create_app, db
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

app = create_app()
db.create_all(app=app)
migrate = Migrate(app, db, directory='upload_file/migrations', compare_type=True)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
