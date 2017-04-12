# -*- coding: utf-8 -*-


from flask_wtf import FlaskForm
from wtforms.fields import *
from wtforms.validators import Required, Email, DataRequired, Length
from neo4j.v1 import GraphDatabase, basic_auth

class SignupForm(FlaskForm):
    name = StringField('name', validators=[DataRequired(),
                                           Length(max=20, message=(u'Please give a name shorter'))])
 

    submit = SubmitField(u'Signup')

"""class NeoForm(FlaskForm):
    driver = GraphDatabase.driver("bolt://localhost", auth=basic_auth("neo4j", "neo"))
    session = driver.session()
    result = session.run("match (o:Officer) return distinct toLower(o.name) as name")

    choices = []

    for r in result:
        choices.append((r["name"])
    #print(choices)
    
    name = SelectField("name", choices)
"""
class TestForm(FlaskForm):
	name = StringField('Name')
	label_d = SelectField(u'Label de départ', choices=[('Intermediary','Intermediary'), ('Address','Address'), ('Officer','Officer'), ('Entity','Entity'), ('Country','Country')])
	label_f = SelectField(u'Label d\'arrivée', choices=[('Intermediary','Intermediary'), ('Address','Address'), ('Officer','Officer'), ('Entity','Entity'), ('Country','Country')])

