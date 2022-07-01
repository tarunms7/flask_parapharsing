import re
from flask import Flask,request
import os
import sys
# from parrot import Parrot
import torch
import warnings
import json
from flask_cors import CORS,cross_origin
from operator import ge
import torch
from transformers import PegasusForConditionalGeneration, PegasusTokenizer
warnings.filterwarnings("ignore")

# PROJECT_ROOT = os.path.abspath(os.path.join(
#                   os.path.dirname(__file__), 
#                   os.pardir)
# )
# sys.path.append(PROJECT_ROOT)
# # import utils
# parrot = Parrot(model_tag="prithivida/parrot_paraphraser_on_T5", use_gpu=True)

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

@app.route("/test", methods = ["GET","POST"])
def test():
  if request.method == "POST":
    # return "Post request received"
    print("post request received")
    data = request.get_json(force = True)
    text= data["input"]
    # output = {}
    # print("-"*100)
    # print("Input_phrase: ", phrases)
    # print("-"*100)
    # count = 1
    # for phrase in phrases:
    #   if phrase == "":
    #     continue
    #   phrase = phrase+"."
    #   print("phrase after adding the dot : ",phrase)
    #   para_phrases = parrot.augment(
    #     input_phrase=phrase,
    #     use_gpu=False,
    #     do_diverse=True, 
    #     adequacy_threshold = 0.8, 
    #     fluency_threshold = 0.8
    #   )
    #   output[count] = []
    #   output[count] = para_phrases
    #   count+=1
    # print(output)
    # print(type(output))



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
    print("get request received")
    
    return "<h1>Data is sent <h1>"
    # return "Get request received"

if __name__ == "__main__":
  app.run(debug = True)