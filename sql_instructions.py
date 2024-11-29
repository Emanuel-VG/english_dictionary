sql = [
    # Create tables
    "CREATE TABLE category (id INTEGER PRIMARY KEY,type TEXT NOT NULL);",
    "CREATE TABLE subcategory (id INTEGER PRIMARY KEY,type TEXT NOT NULL,category_id INT NOT NULL,FOREIGN KEY (category_id) REFERENCES category (id) );",
    "CREATE TABLE topic (id INTEGER PRIMARY KEY, name TEXT NOT NULL,subcategory_id INT NOT NULL,FOREIGN KEY (subcategory_id) REFERENCES subcategory (id));",
    "CREATE TABLE nouns (id INTEGER PRIMARY KEY, )",
    "INSERT INTO category (type) VALUES ('adjective'),('adverb'),('conjunction'),('determiner'),('interjection'),('verb'),('preposition'),('pronoun'),('noun');",
    "INSERT INTO subcategory (type,category_id) VALUES ('')"
]
