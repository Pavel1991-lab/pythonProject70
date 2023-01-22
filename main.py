from flask import Flask, jsonify, request
from utils import all, one

app = Flask(__name__)

@app.get('/movie/<title>')
def index(title: str):
   querry =  f"""
   SELECT * FROM netflix
   WHERE title = '{title}'
   ORDER BY date_added desc
   """
   querry_result = one(querry)

   if querry_result is None:
      return jsonify(status = 404)

   film =  {
      'title': querry_result['title'],
      'country': querry_result['country'],
      'release_year': querry_result['release_year'],
      'genre': querry_result['listed_in'],
      'description': querry_result['description']
   }
   return jsonify(film)

@app.get('/movie/<year1>/to/<year2>')
def index_1(year1: str, year2: str):
   querry =  f"""
   SELECT * FROM netflix
   WHERE release_year BETWEEN 
   '{year1}' and '{year2}'
   ORDER BY date_added desc
   LIMIT 100
   """
   result = []
   for i in all(querry):
      result.append(
         {  'title': i['title'],
          'release_year': i['release_year']}
      )

   return jsonify(result)



@app.get('/rating/<value>')
def index_3(value: str):
   querry =  f"""
   SELECT * FROM netflix
   """

   if value == 'children':
      querry += 'WHERE rating = "G"'
   elif value == 'family':
      querry += 'WHERE rating = "G" or rating = "PG" or rating = "PG - 13"'
   elif value == 'adult':
      querry += 'WHERE rating = "R" or rating = "NC - 17"'


   result = []

   for i in all(querry):
      result.append(
         {'title': i['title'],
          'rating' : i['rating'],
          'description' : i['description']}
      )
   return jsonify(result)

@app.get('/genre/<genre>')
def index_4(genre: str):
   querry = f"""
     SELECT * FROM netflix
     WHERE listed_in = '{genre}'
     ORDER BY date_added DESC
     LIMIT 10
     """
   result = []
   for i in all(querry):
      result.append(
         {'title': i['title'],
          'description': i['description']}
      )
   return jsonify(result)


app.run(debug=True)



