from flask import render_template, Blueprint

views = Blueprint('views', __name__)


@views.route('/')
def index():
    return render_template("index.html")




@views.route('/driver')
def driver():
    return render_template("internal/driver/driver_main.html")

@views.route('/driver_active_routes')
def driver_active_routes():
    return render_template("internal/driver/driver_active_routes.html")

@views.route('/driver_routes_history')
def driver_routes_history():
    return render_template("internal/driver/driver_routes_history.html")

@views.route('/driver_vehicle')
def driver_vehicle():
    return render_template("internal/driver/driver_vehicle.html")




@views.route('/maintenance')
def maintenance():
    return render_template("internal/maintenance/maintenance_main.html")

@views.route('/maintenance_assignments')
def maintenance_assignments():
    return render_template("internal/maintenance/maintenance_assignments.html")

@views.route('/maintenance_request_parts')
def maintenance_request_parts():
    return render_template("internal/maintenance/maintenance_request_parts.html")

@views.route('/maintenance_vehicles')
def maintenance_vehicle():
    return render_template("internal/maintenance/maintenance_vehicles.html")



@views.route('/fueling')
def fueling():
    return render_template("internal/fueling/fueling_main.html")

@views.route('/fueling_info')
def fueling_info():
    return render_template("internal/fueling/fueling_info.html")

@views.route('/fueling_vehicle_update')
def fueling_vehicle_update():
    return render_template("internal/fueling/fueling_vehicle_update.html")

@views.route('/add_fueling')
def add_fueling():
    return render_template("internal/fueling/add_fueling.html")

