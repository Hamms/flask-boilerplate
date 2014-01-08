# -*- coding: utf-8 -*-
"""
    players.models
    ~~~~~~~~~~~

    Models for the players module

    :author: Elijah Hamovitz
    :copyright: (c) 2014 by Elijah Hamovitz.
"""
from __future__ import unicode_literals

from app import db

class Player(db.Model):

    __tablename__ = 'players_player'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
