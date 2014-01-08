# -*- coding: utf-8 -*-
"""
    flask boilerplate
    ~~~~~~~~~~~~~~~~~

    Simple barebones flask project

    :author: Elijah Hamovitz
    :copyright: (c) 2014 by Elijah Hamovitz.
"""
from flask import Flask, render_template
from flask_debugtoolbar import DebugToolbarExtension

from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(config_overrides={}):
    """Create and return an Flask app instance"""
    # create app; load config
    app = Flask(__name__)
    app.config.from_object('config')
    app.config.update(**config_overrides)

    db.init_app(app)

    # flask-debug-toolbar
    DebugToolbarExtension(app)

    if app.config.get('DEBUG_TOOLBAR'):
        toolbar = DebugToolbarExtension(app)

    # error page handlers
    @app.errorhandler(404)
    def not_found(error):
        return render_template('404.html'), 404

    @app.errorhandler(500)
    def server_error(error):
        return render_template('500.html'), 500

    # register blueprints
    from app.main.views import mod as main_module

    app.register_blueprint(main_module)

    # load models
    from app.players.models import Player

    return app
