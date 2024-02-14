from flask import Flask,render_template,request
from werkzeug.utils import secure_filename
#from translate import tranlate_lang
from flask import *
from sampletranlator import eng_to_hindi
import os
import pandas as pd
import numpy as np

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "uploads/"
app.secret_key = 'translate'



@app.route("/home")
def homenew():
    return render_template("homepage.html")


@app.route('/translate', methods = ['GET', 'POST'])
def translate():
    if request.method == 'POST':
        f = request.files['file']
        filename = secure_filename(f.filename)
        f.save(app.config['UPLOAD_FOLDER'] + filename)
        file = open(app.config['UPLOAD_FOLDER'] + filename,"r")
        #ff="C:\\Nandika\\lttool\\webapp\\uploads"+"\\"+filename
        ff="uploads"+"\\"+filename
        #print(ff)
        #cc ,audio,audioeng= eng_to_hindi("C:\\Nandika\\lttool\\webapp\\uploads"+"\\"+filename)
        cc ,audio,audioeng= eng_to_hindi("uploads"+"\\"+filename)
        if cc == "File type not supported":
            error="File type not supported"
            #flash("File type not supported")
            return render_template('homepage.html',content="File type not supported")
        if cc == "file not readable":
            error="File type not supported"
            return render_template('homepage.html',content="please upload a well formed file")
        if cc.endswith(".xlsx"):
            pd.options.display.max_colwidth = 100
            df = pd.read_excel("uploads\\"+cc,names=["Translated Text:"])
            return render_template('homepage.html',content=df,dwf=cc,audio=audio,audioeng=audioeng)
        else:
            fnew=open("uploads\\"+cc, "r",encoding="utf-8")
            content=" "
            for line in fnew:
                line=str(line)
                content= content+"\n"+line
                continue
            #print(content)   
            return render_template('homepage.html',content=content,dwf=cc,audio=audio,audioeng=audioeng)
    else:
        return render_template('homepage.html')



@app.route("/howto")
def content():
    return render_template("howto.html")


@app.route('/uploads/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    # Appending app path to upload folder path within app root folder
    uploads = os.path.join(current_app.root_path, app.config['UPLOAD_FOLDER'])
    uploads=uploads.replace('/','\\')
    print(uploads)
    # Returning file from appended path
    return send_from_directory(directory=uploads, path=filename,as_attachment=True)

    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
