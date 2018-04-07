import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','we_rent.settings')

import django
django.setup()
from management.models import State, Country

def populate():
	# Create a tuple of States
	states= ('Alabama', 'Alaska', 'Arizona','Arkansas','California','Colorado',
 			'Connecticut','Delaware','Florida','Georgia','Hawaii','Idaho','Illinois',
 			'Indiana','Iowa','Kansas','Kentucky','Louisiana','Maine','Maryland',
 			'Massachusetts','Michigan','Minnesota','Mississippi','Missouri','Montana',
 			'Nebraska','Nevada','New Hampshire','New Jersey','New Mexico','New York',
 			'North Carolina','North Dakota','Ohio','Oklahoma','Oregon','Pennsylvania',
 			'Rhode Island','South Carolina','South Dakota','Tennessee','Texas','Utah',
 			'Vermont','Virginia','Washington','West Virginia','Wisconsin','Wyoming'
 			)
	countries = ('Afghanistan','Aland Islands','Albania','Algeria','American Samoa',
				'Andorra','Angola','Anguilla','Antarctica','Antigua and Barbuda',
				'Argentina','Armenia','Aruba','Australia','Austria','Azerbaijan',
				'Bahamas','Bahrain','Bangladesh','Barbados','Belarus','Belgium',
				'Belize','Benin','Bermuda','Bhutan','Bolivia, Plurinational State of',
				'Bonaire, Sint Eustatius and Saba','Bosnia and Herzegovina','Botswana',
				'Bouvet Island','Brazil','British Indian Ocean Territory',
				'Brunei Darussalam','Bulgaria','Burkina Faso','Burundi','Cambodia',
				'Cameroon','Canada','Cape Verde','Cayman Islands',
				'Central African Republic','Chad','Chile','China','Christmas Island',
				'Cocos (Keeling) Islands','Colombia','Comoros','Congo',
				'Congo, the Democratic Republic of the','Cook Islands','Costa Rica',
				"Cote d'Ivoire",'Croatia','Cuba','Curacao','Cyprus','Czech Republic',
				'Denmark','Djibouti','Dominica','Dominican Republic','Ecuador','Egypt',
				'El Salvador','Equatorial Guinea','Eritrea','Estonia','Ethiopia',
				'Falkland Islands (Malvinas)','Faroe Islands','Fiji','Finland','France',
				'French Guiana','French Polynesia','French Southern Territories','Gabon',
				'Gambia','Georgia','Germany','Ghana','Gibraltar','Greece','Greenland',
				'Grenada','Guadeloupe','Guam','Guatemala','Guernsey','Guinea','Guinea-Bissau',
				'Guyana','Haiti','Heard Island and McDonald Islands',
				'Holy See (Vatican City State)','Honduras','Hong Kong','Hungary','Iceland',
				'India','Indonesia','Iran, Islamic Republic of','Iraq','Ireland','Isle of Man',
				'Israel','Italy','Jamaica','Japan','Jersey','Jordan','Kazakhstan','Kenya',
				'Kiribati',"Korea, Democratic People's Republic of",'Korea, Republic of',
				'Kuwait','Kyrgyzstan',"Lao People's Democratic Republic",'Latvia','Lebanon',
				'Lesotho','Liberia','Libya','Liechtenstein','Lithuania','Luxembourg','Macao',
				'Macedonia, the former Yugoslav Republic of','Madagascar','Malawi','Malaysia',
				'Maldives','Mali','Malta','Marshall Islands','Martinique','Mauritania','Mauritius',
				'Mayotte','Mexico','Micronesia, Federated States of','Moldova, Republic of',
				'Monaco','Mongolia','Montenegro','Montserrat','Morocco','Mozambique','Myanmar',
				'Namibia','Nauru','Nepal','Netherlands','New Caledonia','New Zealand','Nicaragua',
				'Niger','Nigeria','Niue','Norfolk Island','Northern Mariana Islands','Norway','Oman',
				'Pakistan','Palau','Palestine, State of','Panama','Papua New Guinea','Paraguay',
				'Peru','Philippines','Pitcairn','Poland','Portugal','Puerto Rico','Qatar','Reunion',
				'Romania','Russian Federation','Rwanda','Saint Barthelemy',
				'Saint Helena, Ascension and Tristan da Cunha','Saint Kitts and Nevis','Saint Lucia',
				'Saint Martin (French part)','Saint Pierre and Miquelon',
				'Saint Vincent and the Grenadines','Samoa','San Marino','Sao Tome and Principe',
				'Saudi Arabia','Senegal','Serbia','Seychelles','Sierra Leone','Singapore',
				'Sint Maarten (Dutch part)','Slovakia','Slovenia','Solomon Islands','Somalia',
				'South Africa','South Georgia and the South Sandwich Islands','South Sudan',
				'Spain','Sri Lanka','Sudan','Suriname','Svalbard and Jan Mayen','Swaziland',
				'Sweden','Switzerland','Syrian Arab Republic','Taiwan, Province of China',
				'Tajikistan','Tanzania, United Republic of','Thailand','Timor-Leste','Togo','Tokelau',
				'Tonga','Trinidad and Tobago','Tunisia','Turkey','Turkmenistan',
				'Turks and Caicos Islands','Tuvalu','Uganda','Ukraine','United Arab Emirates',
				'United Kingdom','United States','United States Minor Outlying Islands','Uruguay',
				'Uzbekistan','Vanuatu','Venezuela, Bolivarian Republic of','Viet Nam',
				'Virgin Islands, British','Virgin Islands, U.S.','Wallis and Futuna','Western Sahara',
				'Yemen','Zambia','Zimbabwe'
				)
	for state in states:
		add_state(state)

	for country in countries:
		add_country(country)


def add_state(state):
	s = State.objects.get_or_create(name=state)[0]
	s.save()

def add_country(country):
	c = Country.objects.get_or_create(name=country)[0]
	c.save()

# Start execution
if __name__ == '__main__':
	print('Starting management population script...')
	populate()

