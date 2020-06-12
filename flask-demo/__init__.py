from flask import Flask

app = Flask(__name__)
app.config.from_object('search_book.config.Development')

from search_book.views import views