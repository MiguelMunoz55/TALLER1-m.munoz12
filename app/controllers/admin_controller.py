from flask import Blueprint, render_template
from flask_login import login_required, current_user
from app.models.perro import Perro

admin_blueprint = Blueprint("admin", __name__, url_prefix="/admin")

@admin_blueprint.route("/dashboard")
@login_required
def dashboard():
    if not current_user.es_admin:
        return "Acceso denegado", 403

    # Obtener todos los perros de la base de datos
    perros = Perro.query.all()
    
    return render_template("admin/dashboard.html", user=current_user, perros=perros)
