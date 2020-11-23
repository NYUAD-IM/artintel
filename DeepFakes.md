# Deep Fakes Colabs
[Avatars4All by Eyaler](https://github.com/eyaler/avatars4all)
- [Colab to do realtime deep fake using First Order Model in browser using webcam](https://colab.research.google.com/github/eyaler/avatars4all/blob/master/fomm_live.ipynb)
- [Colab to generate and downlaod deep fake talking head video](https://colab.research.google.com/github/eyaler/avatars4all/blob/master/fomm_bibi.ipynb)


### Installation
[DeepFaceLab Linux installation](https://github.com/nagadit/DeepFaceLab_Linux)

Before installing:
```
conda install ffmpeg
```

Before pip requirements install:
```
conda install python=3.6.8
```

After pip install - fix broken libraries
```
pip uninstall Pillow scipy
pip install Pillow scipy
```

To run the scripts
```
cd scripts
source <script_name>
```

### Tutorial
[Linux DeepFaceLab tutorial](https://pub.dfblue.com/pub/2019-10-25-deepfacelab-tutorial)
