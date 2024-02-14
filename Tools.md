# A.rt I.ntel Tools

Software tools and techniques available for class use. We prefer
open source tools and datasets where possible so that we can
make our own explorations and modifications rather than simply
using pre-packaged software to achieve an already curated result.

# 2024

## Image Generation

[Stable Diffusion](https://stability.ai/)
- prompt / guidance based image generation
- open diffusion based model
- training set was previously available (LAION)
- can be downloaded and run on laptops
  - Mac with Apple Silicon and 16GB+ RAM
  - Windows laptop with nVidia GPU
- models have been fine-tuned and expanded on by community
  - e.g. tweaked / additional models available on [Civit.ai](https://civitai.com/) (note: some content there is NSFW)
  - improved models have good quality results

[Easy Diffusion](https://easydiffusion.github.io/)
- runs locally or on server and provides simple web interface
- default model is stock Stable Diffusion 1.5
- can use other SD-based models such as Dream Shaper
- installed and running on IM Lab machines
- has UI for in-painting and using Control Net models for fine-grained image generation / manipulation
- generated images can be saved to local computer through your web browser

[ComfyUI](https://github.com/comfyanonymous/ComfyUI)
- runs locally or on server and provides graph/node-based web UI
- the machine learning graph / pipeline is directly visible / editable
- very efficient operation with only changed parts of graph being executed
- possible to set up complex workflows, for example to compare different models with the same prompt, different upscale operations, etc
- the complete workflow (node graph and settings) is stored into the metadata of each generated image (as JSON) so reloading or sharing a workflow is as simple
as loading the generated image into ComfyUI
- possible to generate very high quality files with single execution of workflow
    - e.g. 8192x8192 from SDXL generating at 1024x1024 with 8x upscale on M3 Mac with 36GB unified RAM
- can generate images "realtime" using SDXL Turbo with "generate on changed" setting enabled ([SDXL Turbo workflow](https://comfyanonymous.github.io/ComfyUI_examples/sdturbo/))
- can connect TouchDesigner and ComfyUI using [TDComfyUI](https://github.com/olegchomp/TDComfyUI)
  - ComfyUI exposes a web API for setting workflow parameters and sending receiving images
  - parameters of ComfyUI workflow are directly accessible in TouchDesigner and possible to send / receive images

