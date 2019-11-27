from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from flask_migrate import Migrate


app = Flask(__name__)
CORS(app)

app.config["SECRET_KEY"] = "my secret key"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://steven:123@localhost:5432/TypeRacer"

db = SQLAlchemy(app)
Migrate = Migrate(app, db)


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String)


class Score(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.Integer)
    wpm = db.Column(db.Integer)
    errors = db.Column(db.Integer)
    user_id = db.Column(db.Integer)
    excerpt_id = db.Column(db.Integer, db.ForeignKey("excerpts.id"))

    def as_dict(self):
        return {c.name: str(getattr(self, c.name)) for c in self.__table__.columns}


class Excerpts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text)
    scores = db.relationship("Score", backref="exerpts", lazy=True)

    def as_dict(self):
        return {c.name: str(getattr(self, c.name)) for c in self.__table__.columns}


@app.route("/")
def root():
    return jsonify(["Hello", "World"])


@app.route("/excerpts")
def list():
    excerpts = Excerpts.query.all()
    jsonified_excerpts = []
    for excerpt in excerpts:
        jsonified_excerpts.append(excerpt.as_dict())
    return jsonify(jsonified_excerpts)


@app.route("/topscores")
def top_scores():
    scores = Score.query.all()
    ordered_scores = Score.query.order_by(Score.wpm.desc()).all()
    top_score = ordered_scores[0].as_dict()
    score_index = ordered_scores.index(scores[-1])
    all_scores = Score.query.all()
    total_scores = len(all_scores)

    current_excerpt_id = scores[-1].excerpt_id
    excerpt_scores = Score.query.filter_by(excerpt_id=current_excerpt_id)
    high_scores = []
    for excerpt in excerpt_scores:
        high_scores.append(excerpt.as_dict())
    return jsonify(top_score, total_scores, score_index, high_scores)


@app.route("/scores", methods=["POST"])
def create_score():
    score = Score(
        user_id=1,
        time=request.get_json()["time"],
        wpm=request.get_json()["wpm"],
        errors=request.get_json()["errorCount"],
        excerpt_id=request.get_json()["excerpt_id"],
    )
    db.session.add(score)
    db.session.commit()

    return jsonify(
        {
            "id": score.id,
            "time": score.time,
            "wpm": score.wpm,
            "errors": score.errors,
            "excerpt_id": score.excerpt_id,
        }
    )


if __name__ == "__main__":
    app.run(debug=True, ssl_context="adhoc")
