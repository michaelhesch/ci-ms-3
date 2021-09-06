from app import create_app, db
from app.models import User, Photo, Category

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Photo': Photo, 'Category': Category}
