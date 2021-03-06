#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module is used to create a from for our Flask application"""

from flask_wtf import FlaskForm
from wtforms.fields import *
from wtforms.validators import Required, Email, DataRequired, Length, InputRequired,EqualTo, NumberRange
from neo4j.v1 import GraphDatabase, basic_auth

""" Class TestForm notre classe pour le formulaire que l'on proposera
    à l'utilisateur
    :param FlaskForm: classe form de WTForms
"""
class TestForm(FlaskForm):
    """
        Notre formulaire demande un nom, un label de départ pour un noeud,
        un autre label pour le noeud d'arrivée
    """
    name = StringField('Name or part of name',
                       validators=[DataRequired("Write something, please"),
                                   Length(min=4, message=("Please give a longer name "))])
    label_d = SelectField(u'Label de départ',
                          choices=[('Intermediary','Intermediary'),
                                       ('Address','Address'),
                                       ('Officer','Officer'),
                                       ('Entity','Entity'),
                                       ('Country','Country')],
                          )
    label_f = SelectField(u'Label d\'arrivée',
                          choices=[('Intermediary','Intermediary'),
                                       ('Address','Address'),
                                       ('Officer','Officer'),
                                       ('Entity','Entity'),
                                       ('Country','Country')])
    check = BooleanField("Exact match for field name")
"""
Class CountryForm: 
: param FlaskForm: classe form de WTForms
"""
class CountryForm(FlaskForm):
  """
    Le formulaire prend en paramètre deux pays, un de départ et un d'arrivé
  """
  choices=[(u'South Africa',u'South Africa'),
            (u'Liechtenstein',u'Liechtenstein'),
            (u'Monaco',u'Monaco'),
            (u'Lebanon',u'Lebanon'),
            (u'Switzerland',u'Switzerland'),
            (u'Malaysia',u'Malaysia'),
            (u'Spain',u'Spain'),
            (u'United Kingdom',u'United Kingdom'),
            (u'Jersey',u'Jersey'),
            (u'France',u'France'),
            (u'Luxembourg',u'Luxembourg'),
            (u'Taiwan',u'Taiwan'),
            (u'Estonia',u'Estonia'),
            (u'Mexico',u'Mexico'),
            (u'Argentina',u'Argentina'),
            (u'Guernsey',u'Guernsey'),
            (u'United States',u'United States'),
            (u'Venezuela',u'Venezuela'),
            (u'Hong Kong',u'Hong Kong'),
            (u'Panama',u'Panama'),
            (u'Saudi Arabia',u'Saudi Arabia'),
            (u'Germany',u'Germany'),
            (u'Kuwait',u'Kuwait'),
            (u'Poland',u'Poland'),
            (u'Brazil',u'Brazil'),
            (u'Turkey',u'Turkey'),
            (u'Egypt',u'Egypt'),
            (u'Canada',u'Canada'),
            (u'Portugal',u'Portugal'),
            (u'Russia',u'Russia'),
            (u'Isle of Man',u'Isle of Man'),
            (u'Malta',u'Malta'),
            (u'Hungary',u'Hungary'),
            (u'Israel',u'Israel'),
            (u'Greece',u'Greece'),
            (u'Philippines',u'Philippines'),
            (u'Italy',u'Italy'),
            (u'China',u'China'),
            (u'Gibraltar',u'Gibraltar'),
            (u'Bahamas',u'Bahamas'),
            (u'Honduras',u'Honduras'),
            (u'Australia',u'Australia'),
            (u'Austria',u'Austria'),
            (u'Sweden',u'Sweden'),
            (u'Slovenia',u'Slovenia'),
            (u'Uruguay',u'Uruguay'),
            (u'Thailand',u'Thailand'),
            (u'Ecuador',u'Ecuador'),
            (u'Colombia',u'Colombia'),
            (u'United Arab Emirates',u'United Arab Emirates'),
            (u'Peru',u'Peru'),
            (u'Czech Republic',u'Czech Republic'),
            (u'South Korea',u'South Korea'),
            (u'Costa Rica',u'Costa Rica'),
            (u'Andorra',u'Andorra'),
            (u'Cyprus',u'Cyprus'),
            (u'Cayman Islands',u'Cayman Islands'),
            (u'Latvia',u'Latvia'),
            (u'Antigua and Barbuda',u'Antigua and Barbuda'),
            (u'Guatemala',u'Guatemala'),
            (u'Ukraine',u'Ukraine'),
            (u'New Zealand',u'New Zealand'),
            (u'Chile',u'Chile'),
            (u'El Salvador',u'El Salvador'),
            (u'Seychelles',u'Seychelles'),
            (u'Uganda',u'Uganda'),
            (u'Iceland',u'Iceland'),
            (u'Bolivia',u'Bolivia'),
            (u'Belgium',u'Belgium'),
            (u'Netherlands',u'Netherlands'),
            (u'Niue',u'Niue'),
            (u'Montenegro',u'Montenegro'),
            (u'Serbia',u'Serbia'),
            (u'Norway',u'Norway'),
            (u'Macao',u'Macao'),
            (u'Kenya',u'Kenya'),
            (u'Syria',u'Syria'),
            (u'Viet Nam',u'Viet Nam'),
            (u'Turks and Caicos Islands',u'Turks and Caicos Islands'),
            (u'Bermuda',u'Bermuda'),
            (u'Barbados',u'Barbados'),
            (u'Denmark',u'Denmark'),
            (u'Mauritius',u'Mauritius'),
            (u'Mozambique',u'Mozambique'),
            (u'Japan',u'Japan'),
            (u'Finland',u'Finland'),
            (u'Iran',u'Iran'),
            (u'Singapore',u'Singapore'),
            (u'Bahrain',u'Bahrain'),
            (u'Saint Kitts and Nevis',u'Saint Kitts and Nevis'),
            (u'Nigeria',u'Nigeria'),
            (u'Dominican Republic',u'Dominican Republic'),
            (u'British Virgin Islands',u'British Virgin Islands'),
            (u'Tunisia',u'Tunisia'),
            (u'Belarus',u'Belarus'),
            (u'India',u'India'),
            (u'Indonesia',u'Indonesia'),
            (u'Ireland',u'Ireland'),
            (u'Vanuatu',u'Vanuatu'),
            (u'Paraguay',u'Paraguay'),
            (u'Nicaragua',u'Nicaragua'),
            (u'Aruba',u'Aruba'),
            (u'Sri Lanka',u'Sri Lanka'),
            (u'Puerto Rico',u'Puerto Rico'),
            (u'Qatar',u'Qatar'),
            (u'Lesotho',u'Lesotho'),
            (u'Cuba',u'Cuba'),
            (u'Côte d\'Ivoire',u'Côte d\'Ivoire'),
            (u'Tanzania',u'Tanzania'),
            (u'Romania',u'Romania'),
            (u'Jordan',u'Jordan'),
            (u'Macedonia',u'Macedonia'),
            (u'Zimbabwe',u'Zimbabwe'),
            (u'Bulgaria',u'Bulgaria'),
            (u'Djibouti',u'Djibouti'),
            (u'Moldova',u'Moldova'),
            (u'Ghana',u'Ghana'),
            (u'Senegal',u'Senegal'),
            (u'Belize',u'Belize'),
            (u'Curaçao',u'Curaçao'),
            (u'Lithuania',u'Lithuania'),
            (u'Croatia',u'Croatia'),
            (u'Trinidad and Tobago',u'Trinidad and Tobago'),
            (u'Bangladesh',u'Bangladesh'),
            (u'Angola',u'Angola'),
            (u'Saint Vincent and the Grenadines',u'Saint Vincent and the Grenadines'),
            (u'Sudan',u'Sudan'),
            (u'Oman',u'Oman'),
            (u'Morocco',u'Morocco'),
            (u'Kazakhstan',u'Kazakhstan'),
            (u'Saint Lucia',u'Saint Lucia'),
            (u'Malawi',u'Malawi'),
            (u'Georgia',u'Georgia'),
            (u'Libya',u'Libya'),
            (u'U.S. Virgin Islands',u'U.S. Virgin Islands'),
            (u'Liberia',u'Liberia'),
            (u'Pakistan',u'Pakistan'),
            (u'Zambia',u'Zambia'),
            (u'Dominica',u'Dominica'),
            (u'Botswana',u'Botswana'),
            (u'Sint Maarten (Dutch part)',u'Sint Maarten (Dutch part)'),
            (u'Samoa',u'Samoa'),
            (u'American Samoa',u'American Samoa'),
            (u'Haiti',u'Haiti'),
            (u'Anguilla',u'Anguilla'),
            (u'Cambodia',u'Cambodia'),
            (u'Mongolia',u'Mongolia'),
            (u'Central African Republic',u'Central African Republic'),
            (u'Burkina Faso',u'Burkina Faso'),
            (u'Yemen',u'Yemen'),
            (u'Nepal',u'Nepal'),
            (u'Cape Verde',u'Cape Verde'),
            (u'Cook Islands',u'Cook Islands'),
            (u'Iraq',u'Iraq'),
            (u'Namibia',u'Namibia'),
            (u'Jamaica',u'Jamaica'),
            (u'DR Congo',u'DR Congo'),
            (u'Uzbekistan',u'Uzbekistan'),
            (u'Cameroon',u'Cameroon'),
            (u'Chad',u'Chad'),
            (u'Laos',u'Laos'),
            (u'Azerbaijan',u'Azerbaijan'),
            (u'Brunei',u'Brunei'),
            (u'Algeria',u'Algeria'),
            (u'Nauru',u'Nauru'),
            (u'Maldives',u'Maldives'),
            (u'Madagascar',u'Madagascar'),
            (u'Sierra Leone',u'Sierra Leone'),
            (u'Rwanda',u'Rwanda'),
            (u'Somalia',u'Somalia'),
            (u'Armenia',u'Armenia'),
            (u'Swaziland',u'Swaziland'),
            (u'Turkmenistan',u'Turkmenistan'),
            (u'Mali',u'Mali'),
            (u'Guam',u'Guam'),
            (u'Martinique',u'Martinique'),
            (u'Albania',u'Albania'),
            (u'Tajikistan',u'Tajikistan'),
            (u'Fiji',u'Fiji'),
            (u'Gabon',u'Gabon'),
            (u'Slovakia',u'Slovakia'),
            (u'Saint Martin (French part)',u'Saint Martin (French part)'),
            (u'Myanmar',u'Myanmar'),
            (u'Marshall Islands',u'Marshall Islands'),
            (u'Gambia',u'Gambia'),
            (u'Togo',u'Togo'),
            (u'Benin',u'Benin'),
            (u'Guinea',u'Guinea'),
            (u'Suriname',u'Suriname'),
            (u'Bosnia and Herzegovina',u'Bosnia and Herzegovina'),
            (u'Niger',u'Niger'),
            (u'Ethiopia',u'Ethiopia'),
            (u'Guyana',u'Guyana'),
            (u'Palestine',u'Palestine'),
            (u'Guinea-Bissau',u'Guinea-Bissau'),
            (u'Solomon Islands',u'Solomon Islands'),
            (u'Equatorial Guinea',u'Equatorial Guinea'),
            (u'Réunion',u'Réunion'),
            (u'Papua New Guinea',u'Papua New Guinea'),
            (u'Grenada',u'Grenada'),
            (u'San Marino',u'San Marino'),
            (u'Kyrgyzstan',u'Kyrgyzstan'),
            (u'North Korea',u'North Korea')]

  countrya = SelectField(u'Starting Country',choices=choices)
  countryb = SelectField(u'Ending Country',choices=choices)
  value = IntegerField('Search depth', 
          default = 1, validators=[Required(), NumberRange(1, 99, "Must be between 1 and 99")])
