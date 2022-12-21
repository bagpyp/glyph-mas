#%%

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
  return render_template('index.html')
#   return """<form action="/fuckcops" method="get">
#   <label for="fname">First name:</label>
#   <input type="text" id="fname" name="fname"><br><br>
#   <label for="lname">Last name:</label>
#   <input type="text" id="lname" name="lname"><br><br>
#   <input type="submit" value="Submit">
# </form>"""

@app.route('/top')
def top():
  return render_template('top_page.html')

@app.route("/fuckcops")
def post_form():
  fname = request.args.get('fname')
  lname = request.args.get('lname')

  # function_that_saves_to_the_db(arg1, arg2)

  return "Argument 1: %s | Argument 2: %s" % (fname, lname)
  
