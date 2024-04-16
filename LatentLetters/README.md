# Letters through the Latent Space

![Latent Letters](LatentLetters.jpg?raw=true)

Near realtime generative AI images from webcam input using TouchDesigner and Stable Diffusion / ComfyUI.

## Workshop description

'Letters through the Latent Space' is an interactive workshop where participants co-create a realtime AI system that enhances written letters with diverse visual styles. As participants write, their handwritten letters are passed through an AI model that generates augmentations such as transforming the writing into graffiti or watercolors. The themes of the workshop include creative and critical use of AI, use of AI in real-time interactive systems, hands-on collaborative learning, and inclusive access to technology through the use of open and free tools. Participants will not just use the system but participate in collectively modifying it through prompt engineering and tweaking the machine learning model parameters as the system runs. 

![Setup overview](setup_overview.jpg?raw=true)

## Installation
1. Install TouchDesigner
2. Install ComfyUI
3. Install TDComfyUI
   * Install TDComfyUI component
4. Install custom nodes in ComfyUI
   * Install ComfyUI Manager using download or git clone
   * Manager->Install Custom Nodes
     * Search for "tooling" to install External Tooling module
     * Search for "controlnet" to install ControlNet module
5. Install models in ComfyUI
   * Copy [DreamShaper 8 LCM](https://civitai.com/models/4384?modelVersionId=252914) model to ComfyUI/models/checkpoints
   * Manager->Install Models
     * Search for "canny" and install ```control_v11p_sd15_canny_fp16.safetensors```
  
### Installation notes
MacOS Sonoma: As of April 16, 2024 it was necessary to downgrade pytorch inside the ComfyUI virtual environment to get SD1.5 based models to generate properly:

```
$ cd ComfyUI 
$ ./venv/bin/pip install torch==2.1.2 torchvision
```
