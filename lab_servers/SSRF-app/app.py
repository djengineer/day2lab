from flask import request, Flask, send_file
import requests

app = Flask(__name__)

index_form = """
IMAGE RETRIEVER
<br>
Try http://localhost:5000/sampleimage
<br>
<form method='post' action="/">
<label for="image_url">Image URL:</label>
<input width="300px" type="text" id="image_url" name="image_url" value="http://localhost:5000/sampleimage">
<input type="submit" id="submit-button" name="submit-button" value="Submit" />
</form>
<br><br><br><hr><br><br><br>
We use the SSRF attack to get image from mutillidae
<br>
SSRF example URL: <br>http://127.0.0.1/images/coykillericon-50-38.png<br>
<br>
This shows that we can launch URL based attacks to other sites from this application.
"""

@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		url = request.form["image_url"]
		print(url)
		try:
			getimg = requests.get(url).content
			print(getimg)
		except Exception as e:
			print(e)
		return getimg
	else:
		return index_form
		
@app.route('/sampleimage', methods=['GET'])
def sampleimage():
	filename = 'sample.jpg'
	return send_file(filename, mimetype='image/jpeg',as_attachment=True)



if __name__=="__main__":
	app.run()
