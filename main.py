from flask import Flask, render_template, request
import uuid
from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = "user_uploads"
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/create", methods=["GET", "POST"])
def create():
    myid = uuid.uuid1()

    if request.method == "POST":
        print(request.files.keys())

        rec_id = request.form.get("uuid")
        desc = request.form.get("text")
        input_files = []

        for key, file in request.files.items():
            print(key, file)

            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)

                save_path = os.path.join(app.config["UPLOAD_FOLDER"], rec_id)
                os.makedirs(save_path, exist_ok=True)

                file.save(os.path.join(save_path, filename))
                input_files.append(filename)

        with open(os.path.join(save_path, "desc.txt"), "w") as f:
            f.write(desc)
        for fl in input_files:
         with open(os.path.join(save_path, "input.txt"), "a") as f:
            
                f.write(f"file '{fl}'\nduration 1\n")
                
    return render_template("create.html", myid=myid)

@app.route("/gallery")
def gallery():
    reels = os.listdir("static/reels")
    print(reels)
    return render_template("gallery.html", reels=reels)

if __name__ == '__main__':
    # Render port automatically assign karte, naitar default 5000 vapra
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)