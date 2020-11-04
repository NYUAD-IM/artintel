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