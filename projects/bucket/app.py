from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.vbf0leo.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/bucket", methods=["POST"])
def bucket_post():
    bucket_receive = request.form['bucket_give']
    all_buckets = list(db.bucket.find({}, {'_id': False}))

    doc = {
        'num': ++len(all_buckets),
        'bucket':bucket_receive,
        'done': 0
    }
    db.bucket.insert_one(doc)

    print(bucket_receive)
    return jsonify({'msg': '등록 완료!'})

@app.route("/bucket/done", methods=["POST"])
def bucket_done():
    num = request.form['num']
    db.bucket.update_one({'num': int(num)}, {'$set': {'done': 1}})
    return jsonify({'msg': '버킷 리스트 완료!'})

@app.route("/bucket", methods=["GET"])
def bucket_get():
    bucket_list = list(db.bucket.find({}, {'_id': False}))
    print(bucket_list)
    return jsonify({'buckets': bucket_list})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)