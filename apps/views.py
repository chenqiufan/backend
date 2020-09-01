from apps import app
from apps.user_api_v1.views import api_bp

app.register_blueprint(api_bp)