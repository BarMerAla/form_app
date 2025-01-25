from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, SubmitField, SelectField, DateTimeField
from wtforms.validators import DataRequired, Length

class TransactionForm(FlaskForm):
    author = StringField('Имя', validators=[DataRequired(), Length(max=128)])
    sum = IntegerField('Сумма',validators=[DataRequired()])
    category = SelectField('Категория', choices=[('Проживание', 'Проживание'), 
                                                ('Транспорт', 'Транспорт'), 
                                                ('Билеты', 'Билеты'),
                                                ('Прочее', 'Прочее')],
                            validators=[DataRequired(), Length(max=32)])
    comment = TextAreaField('Комментарии', validators=[DataRequired(), Length(max=128)])
    dateTime = DateTimeField('Время добавления', format='%Y-%m-%dT%H:%M', validators=[DataRequired()])
    submit = SubmitField('Добавить')