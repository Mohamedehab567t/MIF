from flask import Flask, render_template, url_for, redirect, request, flash, session
from forms import EmailForm, VoteForm
from DB import Student, SaveVote, VoteC
from functions import calcAgree , calcDisAgree

app = Flask(__name__)

app.config['SECRET_KEY'] = "bhtresxcvbfdee456yu8765redcfghjmnbvcfgtyhu765rfth"


@app.route('/', methods=['POST', 'GET'])
@app.route('/home', methods=['POST', 'GET'])
def home():
    form = EmailForm()
    if form.validate_on_submit():
        session['Email'] = form.email.data
        return redirect(url_for('vote'))
    if form.errors:
        for errorfield in form.errors:
            for errorM in form[errorfield].errors:
                flash(errorM, 'danger')
                print(errorM)
    return render_template('Login.html', form=form)


@app.route('/vote', methods=['POST', 'GET'])
def vote():
    user = Student.find_one({'email': session.get('Email')})
    name = user['name']
    form = VoteForm()
    voteDB = VoteC.find()
    VotedUser = VoteC.find_one({'name' : user['name']})
    if VotedUser :
        print(VotedUser['name'])
    getNumOFAgrees = filter(calcAgree, voteDB)
    NumOFAgrees = len(list(getNumOFAgrees))
    all = list(VoteC.find())
    NumOFDisAgrees = len(all) - NumOFAgrees
    if NumOFDisAgrees < 0:
        NumOFDisAgrees = 0
    return render_template('vote.html', name=name, form=form , d = NumOFDisAgrees , a = NumOFAgrees , user = VotedUser)


@app.route('/data', methods=['POST', 'GET'])
def data():
    state = request.get_json()
    user = Student.find_one({'email': session.get('Email')})
    name = user['name']
    vote = {
        'name': name,
        'state': state['state']
    }
    SaveVote(vote)
    voteDB = VoteC.find()
    getNumOFAgrees = filter(calcAgree, voteDB)
    NumOFAgrees = len(list(getNumOFAgrees))
    all = list(VoteC.find())
    NumOFDisAgrees = len(all) - NumOFAgrees
    if NumOFDisAgrees < 0:
        NumOFDisAgrees = 0
    data = {
        'agree': str(NumOFAgrees),
        'disagree': str(NumOFDisAgrees),
        'state' : state
    }

    print(data['disagree'])
    print(data['agree'])
    print(len(all))
    for vote in voteDB :
        print(vote['name'])
    return data


@app.route('/req')
def req():
    return render_template('req.html')


if __name__ == '__main__':
    app.run(debug=True)
