from database.DB_connect import DBConnect
from model.artist import Artist
from model.collegamenti import Collegamenti
class DAO:

    @staticmethod
    def get_artisti_filtrati(n_alb):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print('Errore connessione database')
            return None
        cursor = cnx.cursor(dictionary=True)
        query = '''SELECT a.id,a.name
                    FROM artist a,album alb
                    WHERE a.id = alb.artist_id
                    GROUP BY a.id,a.name
                    HAVING COUNT(*) >= %s'''
        try:
            cursor.execute(query,(n_alb,))
            for row in cursor:
                artist = Artist(
                    id = row['id'],
                    name =  row['name']
                )
                result.append(artist)
                print(artist)
        except Exception as e:
            print(f'Errore nella query: {e}')
        finally:
            cursor.close()
            cnx.close()
        return result
    @staticmethod
    def get_collegamenti():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print('Errore connessione database')
            return None
        cursor = cnx.cursor(dictionary=True)
        #la verifica di appartenenza ai nodi viene fatta nel model
        query = '''select ar1.id as ar1,ar2.id as a2,COUNT(genre_id) as peso
                    from artist ar1,artist ar2,album al1,album al2,track t1,track t2
                    where ar1.id = al1.artist_id and ar2.id = al2.artist_id and t1.album_id = al1.id and t2.album_id = al2.id and t1.genre_id = t2.genre_id
                    group by  ar1,ar2'''
        try:
            cursor.execute(query)
            for row in cursor:
                collegamenti = Collegamenti(
                    a1=row['ar1'],
                    a2=row['ar2'],
                    peso=row['peso']
                )
                result.append(collegamenti)
                print(collegamenti)
        except Exception as e:
            print(f'Errore nella query: {e}')
        finally:
            cursor.close()
            cnx.close()
        return result
l = DAO.get_collegamenti()