# import os
# import sys
# PROJECT_ROOT = os.path.abspath(os.path.join(
#                   os.path.dirname(__file__), 
#                   os.pardir)
# )
# sys.path.append(PROJECT_ROOT)
# import utils

# phrases = ["Can you recommed some upscale restaurants in Newyork?",
#            "What are the famous places we should not miss in Russia?"
# ]

# for phrase in phrases:
#   print("-"*100)
#   print("Input_phrase: ", phrase)
#   print("-"*100)
#   para_phrases = utils.parrot.parrot.augment(input_phrase=phrase)
#   for para_phrase in para_phrases:
#       print(para_phrase)



x = "Messi is my name, i love football"

y = x.split(".")
print(y)