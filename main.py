from flask import Flask, render_template
import utils

app = Flask(__name__)


@app.route('/')
def index():
    candidates = utils.get_all()
    return render_template('list.html', candidates=candidates)


@app.route('/candidates/<int:pk>')
def get_candidates_by_pk(pk):
    candidate = utils.get_candidate(pk)
    return render_template("single.html", candidate=candidate)


@app.route('/search/<candidate_name>')
def get_candidates_by_name(candidate_name):
    candidates = utils.get_candidates_by_name(candidate_name)
    return render_template("search.html", candidates=candidates, count=len(candidates))


@app.route('/skill/<skill_name>')
def get_candidates_by_skill(skill_name):
    candidates = utils.get_candidates_by_skill(skill_name)
    return render_template("skills.html", candidates=candidates, count=len(candidates), skill=skill_name)


if __name__ == '__main__':
    app.run(debug=True)
