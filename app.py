import re
from flask import Flask,request
import os
import sys
import torch
import warnings
import json
from flask_cors import CORS,cross_origin
from operator import ge
from transformers import PegasusForConditionalGeneration, PegasusTokenizer


model_name = 'tuner007/pegasus_paraphrase'
torch_device = 'cuda' if torch.cuda.is_available() else 'cpu'
tokenizer = PegasusTokenizer.from_pretrained(model_name)
model = PegasusForConditionalGeneration.from_pretrained(model_name).to(torch_device)



def get_response(input_text,num_return_sequences):
  batch = tokenizer.prepare_seq2seq_batch([input_text],truncation=True,padding='longest',max_length=100, return_tensors="pt").to(torch_device)
  translated = model.generate(**batch,max_length=100,num_beams=10, num_return_sequences=num_return_sequences, temperature=1.5)
  tgt_text = tokenizer.batch_decode(translated, skip_special_tokens=True)
  return tgt_text







app = Flask(__name__)
CORS(app)

@app.route("/")
@cross_origin() 
def hello():
  return "<h1>Hello World </h1>"
@cross_origin() 
@app.route("/test", methods = ["GET","POST"])
def test():
  print("called test")
  if request.method == "POST":
    data = request.get_json(force=True)
    text= data["input"]
    print(text)
    inp = text.split(".")
    output = {}
    count = 1
    for xyz in inp:
      if xyz != "":
        xyz+="."
        output[count] = get_response(xyz,5)
        count+=1
    json_object = json.dumps(output, indent = 4) 

    return json_object
  else:
    return "<h1>Data is sent <h1>"

 
if __name__ == "__main__":
  app.run(host = '0.0.0.0',port=4000, debug=True)