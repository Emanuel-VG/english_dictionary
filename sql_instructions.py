sql = [
    # Create tables
    "CREATE TABLE category (id INTEGER PRIMARY KEY,type TEXT NOT NULL);",
    "CREATE TABLE topic (id INTEGER PRIMARY KEY, name TEXT NOT NULL,category_id INT NOT NULL,FOREIGN KEY (category_id) REFERENCES subcategory (id));",
    "CREATE TABLE noun_category(id INTEGER PRIMARY KEY, name )"
    "CREATE TABLE nouns (id INTEGER PRIMARY KEY, name TEST NOT NULL,)",
    "INSERT INTO category (type) VALUES ('adjective'),('adverb'),('conjunction'),('determiner'),('interjection'),('verb'),('preposition'),('pronoun'),('noun');",
    "INSERT INTO subcategory (type,category_id) VALUES ('')"
]
