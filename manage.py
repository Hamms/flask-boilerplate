#!/usr/bin/env python

from flask.ext.script import Manager, Server
from flask.ext.script.commands import Clean, ShowUrls
from flask.ext.alembic import ManageMigrations

from app import create_app

app = create_app()

manager = Manager(app)
manager.add_command("runserver", Server(host=app.config.get('HOST'), port=app.config.get('PORT')))
manager.add_command("clean", Clean())
manager.add_command("showurls", ShowUrls())
manager.add_command("migrate", ManageMigrations())

if __name__ == "__main__":
    manager.run()

