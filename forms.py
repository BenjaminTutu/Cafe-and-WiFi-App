from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, BooleanField
from wtforms.validators import DataRequired, URL

# create a form to add new cafés

class CafeForm(FlaskForm):
    name = StringField('Cafe Name', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])

    img_url = StringField('Image URL', validators=[DataRequired(), URL()])
    map_url = StringField('Google Maps URL', validators=[DataRequired(), URL()])

    has_sockets = BooleanField('Has Sockets')
    has_toilet = BooleanField('Has Toilet')
    has_wifi = BooleanField('Has WiFi')
    can_take_calls = BooleanField('Can Take Calls')

    seats = StringField('Number of Seats')
    coffee_price = StringField('Coffee Price')

    submit = SubmitField('Submit')










# class CafeForm(FlaskForm):
#     cafe = StringField('Cafe Name', validators=[DataRequired()])
#     location = StringField('Location', validators=[DataRequired()])
#     img_url = StringField('Image URL', validators=[DataRequired(), URL()])
#     map_url = StringField('Google Maps URL', validators=[DataRequired(), URL()])    
#     has_sockets = StringField('Has Sockets?', validators=[DataRequired()])
#     has_toilet = StringField('Has Toilet?', validators=[DataRequired()])
#     coffee_rating = SelectField('Coffee Rating', choices=["⭐", "⭐⭐", "⭐⭐⭐", "⭐⭐⭐⭐", "⭐⭐⭐⭐⭐"], validators=[DataRequired()])
#     wifi_rating = SelectField("WiFi Strength Rating", choices=["Select WiFiRating","💪", "💪💪", "💪💪💪", "💪💪💪💪", "💪💪💪💪💪"], validators=[DataRequired()])
#     power_rating = SelectField("Power Availability", choices=["Select Power Rating", "🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌" ], validators=[DataRequired()])
#     seats = SelectField("Seats Availability", choices=["Select Seats Availability", "💺", "💺💺", "💺💺💺", "💺💺💺💺", "💺💺💺💺💺"], validators=[DataRequired()])
#     submit = SubmitField('Submit')


