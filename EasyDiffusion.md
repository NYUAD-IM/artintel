# EasyDiffusion (2024)


## Installing Easy Diffusion on a Mac

1. For IM laptops - create a new directory in ```Documents``` called ```artintel```
2. Download [Easy Diffusion](https://easydiffusion.github.io/docs/installation/)
3. Unzip by clicking on download in Chrome
4. Move `easy-diffusion` directory to ```Documents/artintel/easy-diffusion```
5. Start Terminal.app - easiest way is to press command-space and type "terminal"
6. ```cd ~/Documents/artintel/easy-diffusion```
7. ```./start.sh``` - this will take awhile the first time as the SD 1.5 model is downloaded
8. Web browser should open

Installing more models:
- Download e.g. [Realistic Vision model](https://civitai.com/models/4201?modelVersionId=245598), based on SD 1.5
- Choose the smaller safetensors file (~2GB)
- Move to ```~/artintel/easy-diffusion/models/stable-diffusion```
- Click reload icon next to model name
- The prompt guidance (cfg), sampler, and number of steps may need to be adjusted, see the model page notes for hints
