from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
movies = []
@app.route('/movies', methods=['GET'])
def get_movies():
    """Retrieve all movies or search by title."""
    search = request.args.get('search', '').lower()
    if search:
        filtered_movies = [movie for movie in movies if search in movie['title'].lower()]
        return jsonify(filtered_movies), 200
    return jsonify(movies), 200

@app.route('/movies', methods=['POST'])
def create_movie():
    """Add a new movie."""
    data = request.json
    movie = {
        'id': len(movies) + 1,
        'title': data['title'],
        'description': data['description'],
        'rating': data.get('rating', 0)
    }
    movies.append(movie)
    return jsonify({'message': 'Movie added successfully!'}), 201

@app.route('/movies/<int:movie_id>', methods=['PUT'])
def update_movie(movie_id):
    """Update a movie."""
    movie = next((movie for movie in movies if movie['id'] == movie_id), None)
    if not movie:
        return jsonify({'error': 'Movie not found'}), 404

    data = request.json
    movie['title'] = data.get('title', movie['title'])
    movie['description'] = data.get('description', movie['description'])
    movie['rating'] = data.get('rating', movie['rating'])
    return jsonify({'message': 'Movie updated successfully!'}), 200

@app.route('/movies/<int:movie_id>', methods=['DELETE'])
def delete_movie(movie_id):
    """Delete a movie."""
    global movies
    movies = [movie for movie in movies if movie['id'] != movie_id]
    return jsonify({'message': 'Movie deleted successfully!'}), 200

if __name__ == '__main__':
    app.run(debug=True)
