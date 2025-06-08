from flask import Blueprint, request, jsonify
from models import Book, db


bp = Blueprint('api', __name__)

@bp.route('/api/books', methods=['GET'])
def getBooks():
    books = Book.query.all()
    return jsonify([{
        'id': b.id,
        'title': b.title,
        'author': b.author,
        'read': b.read,
    } for b in books])