# -*- coding: utf-8 -*-
"""
    main.views
    ~~~~~~~~~~~

    Views for the main module

    :author: Elijah Hamovitz
    :copyright: (c) 2014 by Elijah Hamovitz.
"""
from __future__ import unicode_literals

from flask import render_template, Blueprint, flash, redirect, url_for

mod = Blueprint('main', __name__)

@mod.route('/', methods=['GET'])
def index():
    return render_template('main/index.html')

