from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, RadioField
from wtforms.validators import DataRequired, Optional


class CronForm(FlaskForm):
    executable = StringField('executable', validators=[DataRequired()])
    account = StringField('account', validators=[DataRequired()])
    type = RadioField('Label',
                      choices=[('horly', 'horly'), ('daily', 'daily'), ('weekly', 'weekly'), ('monthly', 'monthly')])

    minutes = IntegerField('minutes', validators=[Optional()])
    hour = IntegerField('hour', validators=[Optional()])


class UserForm(FlaskForm):
    account = StringField('account', validators=[DataRequired()])


class RawForm(FlaskForm):
    executable = StringField('executable', validators=[DataRequired()])
    raw = StringField('raw', validators=[DataRequired()])
