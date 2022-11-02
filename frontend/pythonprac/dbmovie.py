from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.vbf0leo.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

print(db.movies.find_one({'title':'가버나움'})['star'])

star = db.movies.find_one({'title':'가버나움'})['star']
movies = list(db.movies.find({'star':star},{'_id':False}))

for movie in movies:
    print(movie['title'])