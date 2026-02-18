from flask import Flask
from models import create_table, insert_user

app = Flask(__name__)

# Create database table when app starts
create_table()

@app.route("/")
def home():
    insert_user("John Doe", "johndoe@example.com", 30)
    return "User inserted into database!"

if __name__ == "__main__":
    app.run(debug=True)
