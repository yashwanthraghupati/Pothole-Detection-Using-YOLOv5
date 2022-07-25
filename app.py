from flask import Flask, render_template, url_for, request
import os
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/uploader', methods=['GET', 'POST'])
def uploader():
    if request.method == 'POST':
        f = request.files['file']
        g = request.files['file']
        file_ext = f.filename.split(".")[-1]

        if(file_ext == 'jpg'):
            f.filename = 'original'+'.jpg'
            f.save('static/DetectionInput/'+f.filename)
          
            path = r" python detect.py --weights C:\Users\yashw\Desktop\PotholeDetection\runs\train\yolov5s_results10\weights\best.pt --source static/DetectionInput/original.jpg --conf 0.4 --exist-ok"
            os.system(path)  # change path name

            print(f.filename)
            return render_template('Output.html')
        else:
            return index(msg="Invalid file")


if __name__ == "__main__":
    app.run(debug=True,port=8000)
