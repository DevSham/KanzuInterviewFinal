
from flask import Flask, jsonify, request
app = Flask(__name__)
categories = []
Article = [
    {"CategoryName": "Sports",
        "id": 1,
        "SportsArticle1": {
            "Articleid": 1,
            "author": "Shamim Nakayiza",
            "title": "Sports",
            "Description": "this is the most amazing sport I wish could do",
            "url": "https://www.adelaidenow.com.au/news/south-australia/military-style-plane-crash-lands-in-goolwa-paddock-pilot-and-passenger-escape-uninjured/news-story/83154535311ebea349fe8cfa823c7084",
            "Image": "img/2018-02-26-17-01-36-997.jpg",
            "publishedAt": "2019-march-1",
            "Content": "It took just minutes for an inner-west terrace to sell for $600,000 above reserve on Saturday. More than 150 people and 21 buyers turned out for the auction of the park-front Newtown home on the market for the first time in decades. Bidding on the six-bedroom… [+5331 chars]"
        }
     },

    {
        "CategoryName": "Health",
        "id": 2,
        "HealthArticle1": {
            "Articleid": 2,
            "author": "Zainab Kalerwee",
            "title": "Health",
            "Description": "This article gives reasons why there are many cancer rates.",
            "url": "https://www.adelaidenow.com.au/news/south-australia/military-style-plane-crash-lands-in-goolwa-paddock-pilot-and-passenger-escape-uninjured/news-story/83154535311ebea349fe8cfa823c7084",
            "Image": "img/1b995d2b4d6bc1dfbc73cfee414479c8.jpg",
            "publishedAt": "2019-march-1",
            "Content": "It took just minutes for an inner-west terrace to sell for $600,000 above reserve on Saturday. More than 150 people and 21 buyers turned out for the auction of the park-front Newtown home on the market for the first time in decades. Bidding on the six-bedroom… [+5331 chars]"
        }
    }
]


@app.route('/Article/api/v1/entry', methods=['POST'])
# Adding a category
def add_entry():
    entry = {
        "id": Article[-1]['id'] + 1,
        "CategoryName": request.json['CategoryName']
    }
    Article.append(entry)
    # 201 is a status code showing success
    return jsonify({"My_Categories": Article}), 201


@app.route('/Article/api/v1/entry', methods=['GET'])
# Returning all articles
def get_all_entries():
    categories = [entry for entry in Article]
    return jsonify({'Article_entries': categories})


@app.route('/Article/api/v1/entry/<int:entry_id>', methods=['GET'])
# Getting a specific category entry.
def get_one_category(entry_id):
    category = [entry for entry in Article if entry['id'] == entry_id]
    return jsonify({'My_Category': category})


@app.route('/Article/api/v1/entry/<int:entry_id>', methods=['PUT'])
# Edit category
def update_entry(entry_id):
    entry = [cat for cat in Article if cat['id'] == entry_id]
    entry[0]['CategoryName'] = request.json['CategoryName']
    return jsonify({"Category": entry})


@app.route('/Article/api/v1/entry/<int:cat_id>', methods=['DELETE'])
# Delete Category
def removeCategory(cat_id):
    category = [entry for entry in Article if entry['id'] == cat_id]
    Article.remove(category[0])
    return jsonify({"Categories": Article})


if __name__ == '__main__':
    app.run(debug=True)
