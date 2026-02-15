from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Integer, String, Float, Boolean
import os
from dotenv import load_dotenv
from sqlalchemy.orm import DeclarativeBase

from forms import CafeForm


load_dotenv()

app = Flask(__name__)

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

app.config['SECRET_KEY'] = os.getenv('FLASK_KEY')
Bootstrap5(app)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///cafe.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db.init_app(app)


# Create database model that matches the cafe.db to read from it
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)

    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)

    seats: Mapped[str | None] = mapped_column(String(250))
    coffee_price: Mapped[str | None] = mapped_column(String(250))

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/cafe')
def cafe():
    cafes = db.session.execute(db.select(Cafe))
    cafes = cafes.scalars().all()
    return render_template('cafes.html', cafes=cafes)

@app.route('/add', methods=['GET', 'POST'])
def add():
    form = CafeForm()
    if form.validate_on_submit():
        new_cafe = Cafe(
            name=form.name.data,
            map_url=form.map_url.data,
            img_url=form.img_url.data,
            location=form.location.data,
            has_sockets=form.has_sockets.data,
            has_toilet=form.has_toilet.data,
            has_wifi=form.has_wifi.data,
            can_take_calls=form.can_take_calls.data,
            seats=form.seats.data,
            coffee_price=form.coffee_price.data,
        )
        db.session.add(new_cafe)
        db.session.commit()
        return redirect(url_for('cafe'))
    return render_template('add_cafe.html', form=form)


@app.route('/show/<int:cafe_id>', methods=['GET', 'POST'])
def show_cafe(cafe_id):
    requested_cafe = db.get_or_404(Cafe, cafe_id)
    return render_template('show_cafe.html', cafe=requested_cafe)


if __name__ == '__main__':
    app.run(debug=False, port=5002)






