#! python.exe

articles =  {
        1: {
            "name": "CPU",
            "price": 400
        },
        2: {
            "name": "RAM",
            "price": 200
        },
        3: {
            "name": "GPU",
            "price": 300
        },
        4: {
            "name": "HDD",
            "price": 250
        },
        5: {
            "name": "DVD",
            "price": 4150
        }
    }

def get_articles():
    return articles

def display_article_checkbox(article_id, article):
    print ('<input type="checkbox" name="' + str(article_id) + '" value=' + article.get('name', 'n/a') + '>' + article.get('name', 'n/a') + '	' + str(article.get('price', 'n/a')) + 'kn <br>')

def display_basket_checkbox(article_id, amount):
    article_name = articles.get(int(article_id), {}).get("name", "n/a")
    print ('<input type="checkbox" name="' + str(article_id) + '" value=' + article_name + '>' + article_name + '	' + str(amount) + 'kom <br>')

