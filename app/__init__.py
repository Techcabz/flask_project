from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    app.config['TEMPLATES_AUTO_RELOAD'] = True

    # Register blueprints
    from app.views.main import main
    app.register_blueprint(main)

    return app