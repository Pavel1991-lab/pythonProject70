import sqlite3


def all(query: str):
   with sqlite3.connect('netflix.db') as con:
       con.row_factory = sqlite3.Row
       result = []

       for i in con.execute(query).fetchall():
           result.append(dict(i))

       return result

def one(querry: str):
    with sqlite3.connect('netflix.db') as con:
        con.row_factory = sqlite3.Row
        result = con.execute(querry).fetchone()

    if result is None:
        return None
    else:
        return dict(result)



def cast_with_Hofman(name_1: str='Jack Black', name_2: str='Dustin Hoffman'):
   querry = f"""
     SELECT * FROM netflix
     WHERE netflix.cast like 'Jack Black' and netflix.cast like 'Dustin Hoffman'
     """
   cast = []
   set_cast = set()

   for i in all(querry):
      for actor in i['cast'].split(','):
         cast.append(actor)

   for actor in cast:
      if set.cast.count(actor) > 2:
         set_cast.add(actor)
   return list(set_cast)




def step_6(film: str, year, genre: str):
    with sqlite3.connect('netflix.db') as con:
        cursor = con.cursor()
        querry = f"""
        SELECT title, description FROM netflix
        WHERE "type" = '{film}' AND
        release_year = '{year}' AND
        "listed_in" = '{genre}'
        """
        cursor.execute(querry)
        for i in cursor.fetchall():
            return i

print(step_6("Film", 2011, "Dramas"))