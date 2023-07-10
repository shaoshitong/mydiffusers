import diffusers
import datasets
from datasets import load_dataset
dataset = load_dataset("lambdalabs/pokemon-blip-captions")
dataset.save_to_disk("./")