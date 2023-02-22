# Stable Diffusion Guide (2023)

The lab computers have [Stable Diffusion](https://github.com/Stability-AI/stablediffusion) installed with the [Easy Diffusion](https://github.com/cmdr2/stable-diffusion-ui) web UI. The web UI is accessible while on campus or using the VPN.

[Stable Diffusion web UI links (Brightspace, class students only)](https://brightspace.nyu.edu/d2l/le/lessons/265669/units/8229531)

Available models:
- [Stable Diffusion 2](https://github.com/Stability-AI/stablediffusion)
  - [Stable Diffusion 2.1 base](https://huggingface.co/stabilityai/stable-diffusion-2-1-base)
    - Designed for 512x512 output
    - Recommended for exploring prompts
    - 5GB model checkpoint
  - [Stable Diffusion 2.1](https://huggingface.co/stabilityai/stable-diffusion-2-1)
    - Designed for 768x768 output
    - Slower than base since higher resolution
    - Recommended for higher resolution output after exploring prompts
    - 5GB model checkpoint
-  Stable Diffusion 1.4
  - Previous version, mostly of historical interest

Note: when exploring text to image models some links (e.g. to custom trained models) eventually lead to NSFW content.

## Easy Diffusion (Stable Diffusion Web UI)

- [How to use](https://github.com/cmdr2/stable-diffusion-ui/wiki/How-to-Use)
- [UI Overview](https://github.com/cmdr2/stable-diffusion-ui/wiki/UI-Overview)
- [Writing prompts](https://github.com/cmdr2/stable-diffusion-ui/wiki/Writing-prompts)

### Recommended settings
- Set Model (start with v2-1_512-ema-pruned)
- Set the Image Size (512x512 for 512 model, or 768x768 for 768 model)

Recommended initial settings:


These settings offer a good balance of speed and quality while exploring while using our shared machines. Once you have a prompt or image that you like you can experiment with other settings to increase the quality of the final output.

### Writing the prompt
- Write your prompt and negative prompt
- With the Euler Ancestral sampler (recommended for initial ideation) running more inference steps ("Draw another 25 steps") may significantly change the image. Other samplers generally increase the quality rather than changing the image 

### Saving the prompt
- Click the copy icon next to the prompt window to copy the settings as JSON code

### Crediting your images
"Created with Stable Diffusion 2.1 using prompt {prompt}" and include prompt JSON with code formatting.

e.g.

### Increasing output quality
- Use the 768x768 model
- Change samplers and run more inference steps
  - The recommended / default Euler Ancestral is fast but will change the image rather than increasing the quality
  - Use your generated image as input, change to a different sampler, and run more inference steps
  - See [Stable Diffusion Samplers](https://nightcafe.studio/blogs/info/stable-diffusion-samplers) for sampler suggestions
  - [Easy Diffusion samplers](https://github.com/cmdr2/stable-diffusion-ui/wiki/How-to-Use#samplers)
  - Hover over image and "Draw another 25 steps"
- Fix faces (runs another model over the generated image to fix faces)
- Upscale your image (runs another model to upscale)

## Writing prompts
- [Stable Diffusion Prompt Book](https://openart.ai/promptbook)

- Consider both the prompt and the negative prompt
- Add emphasis (weighting) to different parts of the prompt to increase their importance
- What prompts produce good / poor output? What prompts are blocked?

## Inpainting / Image to Image

Techniques
- Start with an input image that you create (e.g. a simple drawing) and use that to condition the generated image.
- Take a generated output image and use that as the input image to continue refining / tweaking it
- Mask part of the input image to have Stable Diffusion just paint those areas. E.g. draw a simple skyline into one of your photos then mask that area to have Stable Diffusion replace your drawing with generated imagery