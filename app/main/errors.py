from . import main
from flask import render_template


@main.app_errorhandler(404)
def forbidden(e):
    return render_template('errors/404.html'), 404

@main.app_errorhandler(403)
def page_not_found(e):
    return render_template('errors/404.html'), 404

@main.app_errorhandler(500)
def internal_server_error(e):
    return render_template('errors/404.html'), 404
