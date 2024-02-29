#!/usr/bin/env python

# Python script that queues multiple prompts to a ComfyUI server
#
# Adapted from https://medium.com/@yushantripleseven/comfyui-using-the-api-261293aa055a
# Michael Ang
# A.rt I.ntel 2024
#
# Steps:
# - load the ComfyUI workflow saved as "API JSON"
# - for each of the prompts
#  - calculate a unique filename prefix based on the current time
#   - change the workflow parameters
#     - prompt
#     - output filename prefix
#   - post the complete workflow to the server
#
# The output images are saved in the outputs directory of the ComfyUI installation with
# an additional suffix added to the filename, e.g. if the prefix is 'generated_20240229-133808-852495'
# the output will be at:
# {ComfyUI directory}/output/generated_20240229-133808-852495_00001_.png


import json
from urllib import request, parse
import random

# Timestamp code adapted from
# https://stackoverflow.com/questions/50368143/create-unique-id-based-on-date-in-python
from datetime import datetime

# ======================================================================
# This function sends a prompt workflow to the specified URL 
# (http://127.0.0.1:8188/prompt) and queues it on the ComfyUI server
# running at that address.
def queue_prompt(prompt_workflow):
    p = {"prompt": prompt_workflow}
    data = json.dumps(p).encode('utf-8')
    req =  request.Request("http://127.0.0.1:8188/prompt", data=data)
    request.urlopen(req)    
# ======================================================================
    
# Returns a unique timestamp in human readable form
# Adapted from https://stackoverflow.com/questions/50368143/create-unique-id-based-on-date-in-python
def uniqueTimeStamp():
  return datetime.now().strftime('%Y%m%d-%H%M%S-%f')

# read workflow api data from file and convert it into dictionary 
# assign to var prompt_workflow
prompt_workflow = json.load(open('sd15_api.json'))

# create a list of prompts
prompt_list = []
prompt_list.append("photo of a man sitting in a cafe")
prompt_list.append("photo of a woman standing in the middle of a busy street")
prompt_list.append("drawing of a cat sitting in a tree")
prompt_list.append("beautiful scenery nature glass bottle landscape, purple galaxy bottle")

# give some easy-to-remember names to the nodes
prompt_pos_node = prompt_workflow["2"]
ksampler_node = prompt_workflow["3"]
save_image_node = prompt_workflow["11"]

# for every prompt in prompt_list...
for index, prompt in enumerate(prompt_list):
  fileprefix = 'generated_' + uniqueTimeStamp()
  print("Queuing prompt:")
  print("  Output filename prefix: " + fileprefix)
  print("  Prompt: " + prompt)

  # set the text prompt for positive CLIPTextEncode node
  prompt_pos_node["inputs"]["text"] = prompt

  # set a random seed in KSampler node 
  ksampler_node["inputs"]["seed"] = random.randint(1, 100000)
  seed = ksampler_node["inputs"]["seed"] # get seed to use in filename

  # Make the sampler keep the same seed (for regenerating in UI)
  # Necessary since "save as API" doesn't seem to save this field
  # into the json
  ksampler_node["inputs"]["control_after_generate"] = "fixed"


  # set filename prefix to be the same as prompt
  # (truncate to first 100 chars if necessary)
  #fileprefix = 'generated_' + str(seed) + '_' + prompt
  #if len(fileprefix) > 100:
  #  fileprefix = fileprefix[:100]

  save_image_node["inputs"]["filename_prefix"] = fileprefix

  # everything set, add entire workflow to queue.
  queue_prompt(prompt_workflow)