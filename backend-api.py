from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///apps.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class App(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    app_name = db.Column(db.String(100), nullable=False)
    version = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text)

    def to_dict(self):
        return {
            'id': self.id,
            'app_name': self.app_name,
            'version': self.version,
            'description': self.description
        }

# Create database tables
with app.app_context():
    db.create_all()

@app.route('/add-app', methods=['POST'])
def add_app():
    data = request.json
    new_app = App(
        app_name=data['app_name'],
        version=data['version'],
        description=data.get('description', '')
    )
    db.session.add(new_app)
    db.session.commit()
    return jsonify(new_app.to_dict()), 201

@app.route('/get-app/<int:id>', methods=['GET'])
def get_app(id):
    app_detail = App.query.get_or_404(id)
    return jsonify(app_detail.to_dict())

@app.route('/delete-app/<int:id>', methods=['DELETE'])
def delete_app(id):
    app_detail = App.query.get_or_404(id)
    db.session.delete(app_detail)
    db.session.commit()
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
