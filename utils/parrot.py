from parrot import Parrot
import torch
import warnings
warnings.filterwarnings("ignore")

global parrot
parrot = Parrot(model_tag="prithivida/parrot_paraphraser_on_T5", use_gpu=True)