from flask import Flask
import donors_route, organ_route, patient_route

app = Flask(__name__)

app.register_blueprint(donors_route.bp)
app.register_blueprint(organ_route.bp)
app.register_blueprint(patient_route.bp)

if __name__ == '__main__':
    app.run(debug=True)