from flask import Flask, render_template
from app.landing import bp


@bp.route('/')
@bp.route('/index')
def test():
    return render_template('./LandingPage/index.html')
