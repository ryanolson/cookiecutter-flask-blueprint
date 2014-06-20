# -*- coding: utf-8 -*-
"""
    {{ cookiecutter.blueprint_name }}.view
    {{ '~' * (cookiecutter.blueprint_name|count + 5) }}

    :author: {{ cookiecutter.author }}
    :copyright: (c) {{ cookiecutter.copyright }}
    :license: {{ cookiecutter.license }}, see LICENSE for more details.
"""
from flask import Blueprint
from flask import render_template, redirect, current_app, url_for, request
from flask.ext.login import login_required
from flask.ext.security import current_user
from werkzeug.local import LocalProxy
from werkzeug.datastructures import MultiDict

# Extensions
_social = LocalProxy(lambda: current_app.extensions['social'])
_security = LocalProxy(lambda: current_app.extensions['security'])

# Blueprint
bp = Blueprint('{{ cookiecutter.blueprint_name }}', __name__)

@bp.route('/')
def index():
    return render_template('{{ cookiecutter.blueprint_name }}/index.html')
