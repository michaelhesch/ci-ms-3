from flask import render_template
from app.errors import bp


@bp.app_errorhandler(403)
def not_found_error(error):
    return render_template('errors/403.html', title='403 Error'), 404


@bp.app_errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html', title='404 Error'), 404


@bp.app_errorhandler(500)
def internal_error(error):
    return render_template('errors/500.html', title='500 Error'), 500
