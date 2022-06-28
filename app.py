import re
from flask import Flask,request
import os
import sys
from parrot import Parrot
import torch
import warnings
import json
warnings.filterwarnings("ignore")

PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__), 
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)
# import utils
parrot = Parrot(model_tag="prithivida/parrot_paraphraser_on_T5", use_gpu=True)
app = Flask(__name__)


@app.route("/")
def hello():
  return "<h1>Hello World </h1>"

@app.route("/test", methods = ["GET","POST"])
def test():
  if request.method == "POST":
    # return "Post request received"
    print("post request received")
    phrases = ["Can you recommed some upscale restaurants in Newyork?",
           "What are the famous places we should not miss in Russia?"
    ]

    for phrase in phrases:
      print("-"*100)
      print("Input_phrase: ", phrase)
      print("-"*100)
      para_phrases = parrot.augment(input_phrase=phrase)
      for para_phrase in para_phrases:
          print(para_phrase)

    return json.jsonify()
  else:
    print("get request received")
    
    return "<h1>Data is sent <h1>"
    # return "Get request received"

if __name__ == "__main__":
  app.run(debug = True)