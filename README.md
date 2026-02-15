# ☕ Cafe & WiFi Finder  
**A Flask Web Application for Discovering Work-Friendly Cafés**

A full-stack Flask application that helps users discover cafés with reliable WiFi, power sockets, and comfortable seating—built with clean architecture, modern SQLAlchemy (2.0 style), and form validation.

This project demonstrates practical backend development skills, database modeling, and frontend integration using Flask.

---

## 👨‍💻 Why This Project Matters (For Recruiters)

This project showcases my ability to:

- Design and work with **existing databases** (SQLite)
- Use **SQLAlchemy ORM (2.0 / Mapped style)**
- Build **CRUD web applications** using Flask
- Implement **form validation** with Flask-WTF
- Structure a maintainable Flask project
- Connect backend data to frontend templates
- Handle static assets correctly
- Build user-friendly, responsive UI components

It reflects real-world backend development rather than tutorial-only patterns.



## 🚀 Live Features

- Browse cafés with essential work amenities
- Add new cafés via validated forms
- View café images and locations
- Open Google Maps directly from listings
- Clearly see Coffee Prices, WiFi, Toilet, seating, and call-friendliness
- Hero-style landing page
- Responsive layout



## 🛠️ Tech Stack

 Layer       |                       Technology 

| Backend                     | Python, Flask |
| ORM                         | Flask-SQLAlchemy (SQLAlchemy 2.0) |
| Database                    | SQLite |
| Forms                       | Flask-WTF |
| Frontend                    | HTML5, CSS3, Bootstrap |
| Templating                  | Jinja2 |



## 🗄️ Database Design

The app uses a **pre-existing SQLite database** (`cafes.db`).  
No new tables are created in production.

### Cafe Model (SQLAlchemy 2.0 Style)

- `id` (Primary Key)
- `name`
- `location`
- `img_url`
- `map_url`
- `has_sockets` (Boolean)
- `has_toilet` (Boolean)
- `has_wifi` (Boolean)
- `can_take_calls` (Boolean)
- `seats`
- `coffee_price`

This reflects **accurate schema mapping**, not database recreation.

---

## 📸 Screenshots

![Home Page]('./static/hero.png')

![Cafes Listings]('screenshots/cafes.png')

![view]('./screenshots/cafe_view.png')

![Add Page]('./screenshots/add.png')

# Cafe-and-WiFi-App
