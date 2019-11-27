from app import db, Excerpts


excerpts = [
    "Then we choose a dependency to run it.",
    "Heroku is used for production.",
    "HTML is for structure.",
    "CSS is for styling.",
    "JS adds behavior.",
    "React was built by Facebook.",
    "Bootstrap was originally developed by Twitter.",
    "We should make sure not to add our venv to Git.",
    "We should make sure not to add our .env to Git.",
    "Python dictionaries are the same as JS objects.",
    "We should probably stick to Flexbox as much as we can.",
    "We should probably stick to Flexbox as much as we can.",
    "SQL means Structured Query Language.",
    "We can produce APIs with Flask if we want to.",
    "React Native follows most of the core principles of React.",
    "Justify content center should sound familiar.",
    "React Bootstrap contains components as well as Bootstrap.",
    "We havent learned how to do push notifications yet.",
]


for excerpt in excerpts:
    new_excerpt = Excerpts(body=excerpt)
    db.session.add(new_excerpt)
    db.session.commit()
