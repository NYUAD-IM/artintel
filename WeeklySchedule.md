# Weekly Schedule - Fall 2021

* [Week 1 - Introduction / What is Machine Learning?](#week1)
* [Week 2 - Speculative Design / Neural Networks](#week2)
* [Week 3 - Speculative Design Project Due (9/14) / Visual Project Introduction](#week3)
* [Week 4 - Convolutional Neural Networks / Neural Network Training](#week4)
* [Week 5 - Neural Network Training / Politics in AI](#week5)
* [Week 6 - Visual Project Check-in / Bias in Datasets](#week6)
* [Week 7 - Visual Project Due (10/12) / Sound / Text Project Introduction](#week7)
* FALL BREAK
* [Week 8 - Sound / Text Tools / Ethics and Bias](#week8)
* [Week 9 - Present Sound / Text ideas](#week9)
* [Week 10 - Other Techniques Sound / Autoencoders](#week10)
* [Week 11 - Sound / Text Project Due (11/16) / Final Project Introduction](#week11)
* [Week 12 - Interactive Applications / ml5.js](#week12)
* [Week 13 - CLASS MEETS MONDAY Present Final Project ideas / NO CLASS](#week13)
* [Week 14 - Final Project check-in / Other topics](#week14)
* [Week 15 - Final Project Due (12/14)](#week15)

## <a name="week1"></a>Week 1 - Introduction / What is Machine Learning?

### <a name="week1.1"></a>Week 1.1 Introduction (8/31)
- Introductions
- Course overview
- In-class discussion
  - Synthetic faces
    - [This Person Does Not Exist](https://thispersondoesnotexist.com/)
    - “Unique, worry-free model photos” https://generated.photos/
    - [Progression in the capabilities of face generation](https://machinelearningmastery.com/wp-content/uploads/2019/06/Example-of-the-Progression-in-the-Capabilities-of-GANs-from-2014-to-2017.png)
  - Deep Fakes
    - [Making a political figure deliver a new speech](https://www.theverge.com/tldr/2018/4/17/17247334/ai-fake-news-video-barack-obama-jordan-peele-buzzfeed)
  - Text generation - fake news
    - [Fake-News-Generating AI Deemed Too Dangerous for Public Release](https://www.extremetech.com/extreme/285857-fake-news-generating-ai-deemed-too-dangerous-for-public-release)
    - [OpenAI Releases Fake News Bot It Previously Deemed Too Dangerous](https://www.extremetech.com/extreme/301662-openai-releases-fake-news-bot-it-previously-deemed-too-dangerous)
    - [Faking the News with Natural Language Processing and GPT-2](https://medium.com/@ageitgey/deepfaking-the-news-with-nlp-and-transformer-models-5e057ebd697d)
  - Speech Synthesis
    - [Val Kilmer reclaims his voice through AI technology after throat cancer](https://www.thenationalnews.com/arts-culture/film/2021/08/21/val-kilmer-reclaims-his-voice-through-ai-technology-after-throat-cancer/)
    - [Ultra-realistic voice cloning](https://www.descript.com/overdub)
  - Code generation
    - [GitHub Copilot](https://copilot.github.com/)
  - Text to image
    - [OpenAI DALL-E](https://openai.com/blog/dall-e/)
    - [Mindblowing AI pixel art](https://boingboing.net/2021/08/19/mindblowing-ai-pixel-art.html)
      - [CLIPIT PixelDraw Colab](https://colab.research.google.com/drive/1uya2CzekydPASALHtgrwxOekBMlaWGON?usp=sharing)
  - [Florida cops use AI to target people for a new "enhanced scrutiny" program](https://boingboing.net/2021/07/27/florida-cops-use-ai-to-target-people-for-a-new-enhanced-scrutiny-program.html)
  - [Moral Machine](https://www.moralmachine.net/) - A platform for public participation in and discussion of the human perspective on machine-made moral decisions
  - [B0na F1de Artist Collective](https://www.b0naf1de.com/) - Jonghyun Jee's final project

  #### Homework (due before start of next class)
  - **Sign up** for Discord using the [Discord invite](https://brightspace.nyu.edu/d2l/le/lessons/110671/units/5693439) on Brightspace  (optional, recommended)
    - Discord is a third-party service. Use of Discord is optional, please consider anything you post there to be public.
  - **Read**
    - Creative AI:  [https://medium.com/@creativeai/creativeai-9d4b2346faf3](https://medium.com/@creativeai/creativeai-9d4b2346faf3)  
    - What is AI &amp; History (Optional/Recommended): [Chapter 1 - Introduction - Artificial Intelligence a Modern Approach](http://web.cecs.pdx.edu/~mperkows/CLASS_479/2017_ZZ_00/02__GOOD_Russel=Norvig=Artificial%20Intelligence%20A%20Modern%20Approach%20(3rd%20Edition).pdf)

  - **Create** a pixel art image using CLIPIT PixelDraw **OR** a face using StyleGAN2
    - **Create** a pixel art image using the [CLIPIT PixelDraw example](https://colab.research.google.com/drive/1uya2CzekydPASALHtgrwxOekBMlaWGON?usp=sharing) and post it in the Discord (or send via email). If you have problems, ask for help! Make sure to save the example to your Google Drive before making edits. Why did you choose your prompt and what do you think the result reveals about how the image generation algorithm works? You can uncheck ```use_pixeldraw``` to see the generated image without pixelation.
    - **Create** a face using the [StyleGAN2 Colab example](https://colab.research.google.com/gist/mangtronix/e19e0c4025fb20e26b7f83990780f0a0/stylegan2-google-colab-example.ipynb) and post it in the Discord (or send via email). If you have problems, ask for help! Make sure to save the example to your Google Drive before making edits.
      - (Optional) Post your generated face or video on social media (or through email, etc) and see what the response is. It's up to you to decide how to communicate your post (you can make it clear it's a generated face or not).





### <a name="week1.1"></a>Week 1.2 (9/2)
- Review homework (CLIPIT / StyleGAN2)

- What is Artificial Intelligence - Machine Learning?
  - [Intro to Machine Learning (YouTube)](https://www.youtube.com/watch?v=KNAWp2S3w94&t=50s)
  - [Neural Networks](https://ml4a.github.io/ml4a/neural_networks/)
  - [Inceptionism: Going Deeper into Neural Networks](https://ai.googleblog.com/2015/06/inceptionism-going-deeper-into-neural.html)
  - [9 of the Funniest and Most Shocking AI Fails](https://lovetheidea.co.uk/9-funniest-shocking-ai-fails/)

- Overview
  - Supervised Learning
  - Unsupervised Learning
  - Reinforcement Learning

  #### Homework (complete before start of next class)
  <!-- - **Read and try** (on Colab) [Make Your Own - Neural Network](http://www.mediafire.com/file/72oi6vzp9l2ps9a/Make_Your_Own_Neural_Network_-_Chapter_1_and_2.pdf/file) - Chapter 2 pages 122-149 (Python coding up until Neural Network code) -->
  - **Read** about supervised / unsupervised / reinforcement learning https://blogs.nvidia.com/blog/2018/08/02/supervised-unsupervised-learning/
  - **Read** Neural Networks: [https://ml4a.github.io/ml4a/neural_networks/](https://ml4a.github.io/ml4a/neural_networks/)

  - **Find** a creative or interesting application of AI and **add** the link to the [Brightspace Discussion](https://brightspace.nyu.edu/d2l/le/110671/discussions/topics/261633/View) with a short explanation of what's interesting about it
  - (Optional) Deep Dream details (we’ll look at this again later when we talk about Convolutional Neural Networks) https://ai.googleblog.com/2015/06/inceptionism-going-deeper-into-neural.html

<!--
- **Read** Looking Inside Neural Networks https://ml4a.github.io/ml4a/looking_inside_neural_nets/

-->

## <a name="week2"></a>Week 2 - Speculative Design / Neural Networks

### <a name="week2.1"></a>Week 2.1 Introduction to Speculative Design (9/7)
- Review homework (new image, interesting applications)
- Talk about Speculative Design project
  - <a href="https://github.com/NYUAD-IM/artintel/blob/master/Projects.md#project-1-speculative-design-due-921">Speculative Design Project requirements<a/>
- Form groups for Speculative Design Project
- Lecture references:
  - [Critical Design - Dunne & Raby](http://dunneandraby.co.uk/content/bydandr/13/0)
  - [Speculative Design - Inside Design](https://www.invisionapp.com/inside-design/speculative-design/)
  - [The Futures Cone, use and history](https://thevoroscope.com/2017/02/24/the-futures-cone-use-and-history/)
  - [Stealing from the future with speculative design](https://uxdesign.cc/stealing-from-the-future-with-speculative-design-e769059b6689)
  - [Robotic Feral Dogs - Natalie Jeremijenko](https://inhabitat.com/robotic-pollution-sniffing-eco-dogs/robotic-pollution-sniffing-eco-dogs-robotic-feral-dogs-robo-eco-dogs-robo-pollution-sniffing-dogs-natalie-jeremijenko-jeff-warren-diego-rotalde-feral-robots-robotic-design-robotic-eco-dogs-4/)
  - [Here's a Baby VR Headset for the Parents of the Future - Stuart Candy](https://www.vice.com/en_au/article/d38adx/baby-vr-headset-future-parents-stuart-candy)
  - [The Optimization of Parenthood - Addie Wagenknecht](https://vimeo.com/43489750)

  - Product References:
      - [Neuralink product page](https://neuralink.com/applications/)
      - [AI meeting scheduler](https://x.ai/)

Class examples:
  - [iPhone Deep Fusion image processing](https://cdn.vox-cdn.com/thumbor/tlZw5DfFLzhsEYjW7SNhJFSH0Cg=/0x0:2000x1333/1200x0/filters:focal(0x0:2000x1333):no_upscale()/cdn.vox-cdn.com/uploads/chorus_asset/file/19187275/lcimg_e39768f8_e95b_4100_b3e7_e2b009bc429d.jpg)
  - [A collection of pre-trained StyleGAN 2 models to download](https://pythonawesome.com/a-collection-of-pre-trained-stylegan-2-models-to-download/)
    - See the difference in quality of faces compared to horses
  - Uncanny Valley
    - [What Is the Uncanny Valley?](https://spectrum.ieee.org/what-is-the-uncanny-valley)
      - [The Uncanny Valley: The Original Essay by Masahiro Mori](https://spectrum.ieee.org/the-uncanny-valley)
    - [Honda's new ASIMO robot, more human-like than ever](https://phys.org/news/2014-04-honda-asimo-robot-human-like.html) 2014
    - [Sophia, Hanson Robotics’ most advanced human-like robot](https://www.hansonrobotics.com/sophia/)
      - [The agony of Sophia, the world's first robot citizen condemned to a lifeless career in marketing (Wired)](https://www.wired.co.uk/article/sophia-robot-citizen-womens-rights-detriot-become-human-hanson-robotics)
    - [This person does not exist](https://thispersondoesnotexist.com/)
    - [lilmequela Instagram influencer - 🤖 19-year-old Robot living in LA 💖 (Instagram)](https://www.instagram.com/lilmiquela/?hl=en)
  - Neuralink
    - [Elon Musk's Neuralink monkey brain demo explained (YouTube)](https://www.youtube.com/watch?v=3Ya-bAYri84)
    - [Elon Musk's Neuralink 'shows monkey playing Pong with mind' (BBC)[https://www.bbc.com/news/technology-56688812]
  - [A Facebook-scale simulator to detect harmful behaviors (Facebook AI)](https://ai.facebook.com/blog/a-facebook-scale-simulator-to-detect-harmful-behaviors/)

#### Homework (due before start of next class)
- **Read**
  - [Speculative Everything](https://readings.design/PDF/speculative-everything.pdf)
    - Read Chapter 1, Chapter 2 (pages 11-16), Chapter 3
- **Review** the [Speculative Design Project requirements](https://github.com/NYUAD-IM/artintel/blob/master/Projects.md#project-1-speculative-design-due-921)
- **Make your group** for the Speculative Design project in the [Projects Doc](https://docs.google.com/spreadsheets/d/1_eyQ4XfzGKpqMIW7FatoDbHBJSAqyPfrkKcyCI66gbI/edit?usp=sharing)
- **Start** developing ideas for a speculative design project about future applications of AI and be prepared to share your idea next class
- **Update** your idea in the [Projects Doc](https://docs.google.com/spreadsheets/d/1_eyQ4XfzGKpqMIW7FatoDbHBJSAqyPfrkKcyCI66gbI/edit?usp=sharing) before class.


### <a name="week2.2"></a>Week 2.2 Neural Networks (9/9)
- Neural Networks
  - [Professor’s perceptron paved the way for AI – 60 years too soon](https://news.cornell.edu/stories/2019/09/professors-perceptron-paved-way-ai-60-years-too-soon)
  - [Perceptron (Wikipedia)](https://en.wikipedia.org/wiki/Perceptron)
  - [Neural Networks (ml4a)](https://ml4a.github.io/ml4a/neural_networks/)
  - [What’s the Difference Between Supervised, Unsupervised, Semi-Supervised and Reinforcement Learning?](https://blogs.nvidia.com/blog/2018/08/02/supervised-unsupervised-learning/)
- Classification Using Neural Networks
  - [Classification of Rock, Paper, Scissors ](https://www.youtube.com/watch?v=KNAWp2S3w94&feature=youtu.be&t=50)
<!-- - Introduction to neural network training -->


#### Homework (due before start of next class)
- Finish your Speculative Design Project and be ready to present in class
  - Refer to [Projects - Speculative Design Project](Projects.md#projects) for the detailed requirements


## <a name="week3"></a>Week 3 - Speculative Design Presentations / Visual Project Introduction

### <a name="week3.1"></a>Week 3.1 - Speculative Design Project Presentations (9/14)
- Speculative Design Project Presentations
  - Give a 5-10 minute presentation of your project and be prepared for feedback from the class

<!--
### <a name="week3.2"></a>Week 3.2 - Speculative Design Workshop (9/16)
- Review speculative design ideas
- Start working on the design ideas

-->


#### Homework (due before start of next class)
- **Create** a new image or other output using one of these Colab notebooks (try to use one of your own input images rather than the built-in ones) https://towardsdatascience.com/12-colab-notebooks-that-matter-e14ce1e3bdd0
  - **Post** your image to the Discord (or send to me via email) with a short explanation of how you made it
  - If you have a problem with the Tensorflow version (e.g "AdamOptimizer not found") add [this code](https://colab.research.google.com/notebooks/tensorflow_version.ipynb)

- (Optional) Read and try the neural network "from scratch" code in [Make Your Own Neural Network Chapter 2](http://www.mediafire.com/file/72oi6vzp9l2ps9a/Make_Your_Own_Neural_Network_-_Chapter_1_and_2.pdf/file)
  - [GitHub repository with examples](https://github.com/makeyourownneuralnetwork/makeyourownneuralnetwork)

### <a name="week3.2"></a>Week 3.2 - Introduction to Visual tools (9/16)
- Review homework

- Discuss Visual Project
  - [Visual Project requirements](https://github.com/NYUAD-IM/artintel/blob/master/Projects.md#project-2-visual-due-last-class-before-spring-break-1014")
    - Create an image, series of images or video using a machine learning algorithm (e.g. using Colab, Artbreeder, other online tools)
    - The work should somehow address one of the concepts we’ve covered in class (e.g. extending creativity, who is the author?, real/fake, AI revolution, bias, etc)

- Introduction to Visual tools  

- Class tools
  - Colab / Neural Network Introduction
    - [Colab Introduction (Colab](https://colab.research.google.com/notebooks/intro.ipynb)
    - [Deep Learning Basics (Colab)](https://colab.research.google.com/github/lexfridman/mit-deep-learning/blob/master/tutorial_deep_learning_basics/deep_learning_basics.ipynb)
    - [Python Tutorial With Google Colab (Colab)](https://colab.research.google.com/drive/1sLkLW3H3PbSC1kyeNNt5WpQivcYqBg69?usp=sharing)

    - [VQGAN+Clip with WikiArt GAN - DALL-E alternative (Colab)](https://colab.research.google.com/drive/1kUVn_pkm83nCWFNAQxNzSS9glxHkZi1Z?usp=sharing)
      - There are English versions of this Colab available, the version above is working with the model from WikiArt. See [Generating AI “Art” with VQGAN+CLIP](https://learn.adafruit.com/generating-ai-art-with-vqgan-clip) for instructions
      - Inspired by [OpenAI DALL-E text to image](https://openai.com/blog/dall-e/)

## <a name="week4"></a>Week 4 - Convolutional Neural Networks

### <a name="week4.1"></a>Week 4.1 - Convolutional Neural Networks (9/21)
- AI in the news
  - [Police to Deploy Snitch Bots That Search for 'Undesirable Social Behaviors'](https://gizmodo.com/singapore-police-to-deploy-snitch-bots-that-search-for-1847629866)
  - [Pandemic Robots Deployed in Parks to Remind Humans of Their Own Mortality](https://gizmodo.com/pandemic-robots-deployed-in-singapore-parks-to-remind-h-1843335679)
  - [Police use Tesla's autopilot to stop the car after drunk driver passes out](https://boingboing.net/2021/09/20/police-use-teslas-autopilot-to-stop-the-car-after-drunk-driver-passes-out.html)

- Introduction to Visual tools continued

  - Machine learning on our lab computers
    - [Lab Computer access](LabComputers.md)
    - [Deep Face Lab](https://github.com/iperov/DeepFaceLab)

  - Machine learning in the browser
    - [ml5.js](https://ml5js.org/)
    - [ml5.js Webcam Classification Demo](https://editor.p5js.org/AndreasRef/sketches/BJkaHBMYm)  


- How convolutional neural networks work
- Examples of convolutional neural networks
  - StyleGAN
- Training and retraining of CNNs

- Lecture links
  - [Convolutional Neural Networks - ml4a](https://ml4a.github.io/ml4a/convnets/)
  - [Convolution demo](https://ml4a.github.io/demos/convolution/)
  - [Convolution all filters demo](https://ml4a.github.io/demos/convolution_all/)
  - [ConvNet viewer](https://ml4a.github.io/guides/ConvnetViewer/)
  - [Convolutional Neural Network Visualization by Otavio Good (YouTube)](https://www.youtube.com/watch?v=f0t-OCG79-U)
  - [WaveNet audio generation](https://deepmind.com/blog/article/wavenet-generative-model-raw-audio)
  - [StyleGAN explanation](https://towardsdatascience.com/explained-a-style-based-generator-architecture-for-gans-generating-and-tuning-realistic-6cb2be0f431)
  - [Convolutional Neural Network Colab](https://colab.research.google.com/github/NYUAD-IM/artintel/blob/master/Code/Week_04/Convolutional_Neural_Network.ipynb#scrollTo=Iv1SLDu_bYXh)
  - [OpenAI Microscope](https://openai.com/blog/microscope/)
    - [Inception 1 - Deep Dream](https://microscope.openai.com/models/inceptionv1?models.technique=deep_dream)
  - [ConvNetJS digit classification demo](https://cs.stanford.edu/people/karpathy/convnetjs/demo/mnist.html)

- **Make your group** for the Visual Design project in the [Projects Doc](https://docs.google.com/spreadsheets/d/1_eyQ4XfzGKpqMIW7FatoDbHBJSAqyPfrkKcyCI66gbI/edit?usp=sharing)
- **Start** developing ideas for the Visual Project
  and be prepared to share your idea next class
- **Update** your idea in the [Projects Doc](https://docs.google.com/spreadsheets/d/1_eyQ4XfzGKpqMIW7FatoDbHBJSAqyPfrkKcyCI66gbI/edit?usp=sharing) before class.


### <a name="week4.2"></a>Week 4.2 -  Neural Network Training (9/23)
- Share project ideas

- Neural Network Training References
  - [How Neural Networks are Trained](https://ml4a.github.io/ml4a/how_neural_networks_are_trained/)
  - [Classification Colab](https://colab.research.google.com/github/tensorflow/docs/blob/master/site/en/tutorials/keras/classification.ipynb#scrollTo=yWfgsmVXCaXG)
  - [ml4a Demos](https://ml4a.github.io/demos/)
  - [ml5js Webcam Classification Demo](https://editor.p5js.org/AndreasRef/sketches/BJkaHBMYm)
  - [MobileNet details](https://towardsdatascience.com/review-mobilenetv1-depthwise-separable-convolution-light-weight-model-a382df364b69)
  - [How to Train StyleGAN to Generate Realistic Faces](https://towardsdatascience.com/how-to-train-stylegan-to-generate-realistic-faces-d4afca48e705)
    - (Advanced)[Training a GAN from your Own Images: StyleGAN2 ADA (YouTube)](https://www.youtube.com/watch?v=kbDd5lW6rkM)
  - [The Illustrated VQGAN](https://ljvmiranda921.github.io/notebook/2021/08/08/clip-vqgan/)

- Overview of Brightspace Reading Responses
  - Post your reading response as a new thread in the Brightspace Discussion Topic for that reading

#### Homework (due before start of next class)
  - **Read** [The AI Revolution - Part 1](https://waitbutwhy.com/2015/01/artificial-intelligence-revolution-1.html)
and AI develops more capabilities? How will the relationship between humans and machines change?
  - **Write** 3-4 paragraphs of response in the [Brightspace Readings Discussion](https://brightspace.nyu.edu/d2l/le/110671/discussions/topics/268945/View)
    - How far do you think we are towards Artificial General Intelligence? What are some of the changes (positive and negative) you see coming as machine learning

## <a name="week5"></a>Week 5 - Neural Network Training

### <a name="week5.1"></a>Week 5.1 - How Neural Networks are Trained (9/28)
- Schedule update
- Discussion: The AI Revolution

- [Useful Colabs](UsefulColabs.md)
- Lab access

- [Lab computers](https://github.com/NYUAD-IM/artintel/blob/master/LabComputers.md)
  - Training example using SampleRNN
    - [https://github.com/mangtronix/samplernn-pytorch](https://github.com/mangtronix/samplernn-pytorch)

  - [tmux: The 10 Most Important Commands](https://danielmiessler.com/study/tmux/)
  - [Tmux Cheat Sheet & Quick Reference](https://tmuxcheatsheet.com/)
  - [How to Send Push Notifications to Your Phone From Any Script](https://medium.com/better-programming/how-to-send-push-notifications-to-your-phone-from-any-script-6b70e34748f6)
  - [IFTTT - If This, Then That](https://ifttt.com/)
  - [FileZilla SFTP client](https://filezilla-project.org/)


- Training Examples
  - VQGAN+CLIP using 'A painting of the Tower of London by Pablo Picasso' different models
    - [VQGAN+CLIP (mangtronix) Tower by Picasso WikiArt](https://colab.research.google.com/drive/1WY4HYKErqAbrQTpmtUt96cEXEW-GjK_a?usp=sharing)
    - [VQGAN+CLIP (mangtronix) - Tower by Picasso ImageNet](https://colab.research.google.com/drive/1MMbEHFnkQXh_Cm1R_7njVjO6znkpfjps?usp=sharing)
  - [GAN Training Colab](https://colab.research.google.com/github/tensorflow/docs/blob/master/site/en/tutorials/generative/dcgan.ipynb?authuser=2)
  - [Finetuning GPT-2 on your own text Colab](https://colab.research.google.com/drive/1uKXS6a9q5qrcU3UdSRpCjYnKHbC-N4pb?usp=sharing)
  - [Simple image classifier in-browser using ml5.js](https://editor.p5js.org/AndreasRef/sketches/BJkaHBMYm)
  - [More ML4A in-browser demos](https://ml4a.github.io/demos/)
  - [Alias-Free GAN](https://nvlabs.github.io/alias-free-gan/)
    - Demonstrates how slight differences in the neural network layout force the network to learn higher-level patterns. e.g. original StyleGAN2 became trained to absolute pixel coordinates.

<!-- add training exercise -->

#### Homework (due before start of next class)
  - **Read** the following articles and be ready to discuss in class
    - [Hikvision Markets Uyghur Ethnicity Analytics, Now Covers Up](https://ipvm.com/reports/hikvision-uyghur)
    - [Facebook apology as AI labels black men 'primates'](https://www.bbc.com/news/technology-58462511)
    - [Lying to the ghost in the machine](http://www.antipope.org/charlie/blog-static/2021/03/lying-to-the-ghost-in-the-mach.html)


### <a name="week5.2"></a>Week 5.2 - Guest Lecture - Joerg Blumtritt (9/30)
  - Guest Lecture with [Joerg Blumtritt](https://nyuad.nyu.edu/en/academics/divisions/arts-and-humanities/faculty/joerg-blumtritt.html)
  - Discussion including these topics:
    - [Hikvision Markets Uyghur Ethnicity Analytics, Now Covers Up](https://ipvm.com/reports/hikvision-uyghur)
    - [Facebook apology as AI labels black men 'primates'](https://www.bbc.com/news/technology-58462511)
    - [Lying to the ghost in the machine](http://www.antipope.org/charlie/blog-static/2021/03/lying-to-the-ghost-in-the-mach.html)

#### Homework (due before start of next class 10/5)
- **Work** on your Visual Project
- **Prepare** to share your idea at our next class together on 10/7
  - What is your latest idea?
  - What Colabs / software are you using?
  - Is there anything you need help with? Feel free to ask on Discord as you go!


<!--

- Links for project tools
  - [Manga GAN](https://github.com/nikitaa30/Manga-GAN)
  - [DeepFaceLab](https://github.com/iperov/DeepFaceLab) for making Deep Fake videos
  - [Cartoonize](https://github.com/experience-ml/cartoonize) cartoonize images/video
  - [Cartoonize webapp - Mangtronix edition](https://colab.research.google.com/drive/1iS8Nv_RYYKV5jOYw4ecyBTUrxZ7l5ufj?usp=sharing) run the CartoonGAN webapp on your own colab - allows generating longer videos
  - [CartoonGAN](https://github.com/mnicnc404/CartoonGan-tensorflow) more advanced cartoon example, has instructions for training your own dataset

- Colab notebooks for generating images / video
  - [StyleGAN2 Colab example](https://colab.research.google.com/gist/mangtronix/e19e0c4025fb20e26b7f83990780f0a0/stylegan2-google-colab-example.ipynb)
  - [Neural Style Transfer Colab](https://colab.research.google.com/drive/1-7ZMHjCG2lTdsZMpVMSpDWzTG6e-cwf3)
  - [12 Colabs That Matter](https://towardsdatascience.com/12-colab-notebooks-that-matter-e14ce1e3bdd0)
  - [Neural Synthesis](https://colab.research.google.com/drive/1xeJAhTEwI3TNH_CJnTMq5AJuPkOs8sJ6)
- [Image scraping](ImageScraping.md)



-->


## <a name="week6"></a>Week 6 - Visual project check-in / Bias in Datasets

### <a name="week6.1"></a>Visual Project Check-In
- Project idea discussion and feedback


#### Homework (due before start of next class)
  - **Read** [Excavating AI: The Politics of Images in Machine Learning Training Sets](https://www.biennial.com/journal/issue-9/excavating-ai-the-politics-of-images-in-machine-learning-training-sets)
and AI develops more capabilities? How will the relationship between humans and machines change?
  - **Write** 3-4 paragraphs of response in the [Brightspace Readings Discussion](https://brightspace.nyu.edu/d2l/le/110671/discussions/topics/269790/View)



### <a name="week6.2"></a>Week 6 - Bias in Datasets (10/7)
- Reading discussion - The Politics of Images in Machine Learning Training Sets
- [AI colorization (Twitter)](https://twitter.com/gwenckatz/status/1381652071695351810)
- [Joy Buolamwini - How I'm fighting bias in algorithms](https://www.ted.com/talks/joy_buolamwini_how_i_m_fighting_bias_in_algorithms)
- [Hidden Bias](https://pair.withgoogle.com/explorables/hidden-bias/)
  
  
- Breaking new
  - [AI outperforms doctors at spotting breast cancer, say NYUAD researchers](https://www.thenationalnews.com/uae/2021/10/06/ai-outperforms-doctors-at-spotting-breast-cancer-say-researchers/)
  - [Improving Breast Cancer Detection in Ultrasound Imaging Using AI (tech details)](https://developer.nvidia.com/blog/improving-breast-cancer-detection-in-ultrasound-imaging-using-ai/)

#### Homework (due before start of next class)
- **Finish** your Visual Project
- **Add** the links to your project and documentation to the [Projects Doc](https://docs.google.com/spreadsheets/d/1_eyQ4XfzGKpqMIW7FatoDbHBJSAqyPfrkKcyCI66gbI/edit?usp=sharing)
- **Prepare a 5 minute presentation of your project and be ready to receive and give feedback


<!--
## <a name="week6.5"></a>Week 6.5 - Fall Break-ish

### <a name="week6.5.1"></a>Legislative day (10/18)
  - **Asynchronous class (do on your own time)**

#### Homework (due before start of next class)
  - **Watch** a film prominently featuring AI
    - Suggestions:
      - [Wikipedia list of AI films](https://en.wikipedia.org/wiki/List_of_artificial_intelligence_films)
      - [Guardian Top 20 Artificial Intelligence Films](https://www.theguardian.com/culture/gallery/2015/jan/08/the-top-20-artificial-intelligence-films-in-pictures)
  - **Write** a response in the [Readings Doc](https://docs.google.com/document/d/1MWwb1x4ylSdiikkB_WQlyuZd_ytVueZV2hIFopOc5_w/edit?usp=sharing)
    - What role does AI play in the film?
    - Do you agree with how AI is portrayed in its implications on society?
    - What does the film reveal about our feelings towards AI?

-->

## <a name="week7"></a>Week 7 - Visual Project presentations / Sound and Text Introduction

<!--
### <a name="week7.1"></a>Week 7 (10/26) - Autoencoders, other forms of neural networks (or guest lecture)
- [MNIST digits autoencoder Colab](https://colab.research.google.com/github/AFAgarap/examples/blob/master/community/en/autoencoder.ipynb)
- [pix2pix ml4a](https://ml4a.github.io/guides/Pix2Pix/)
- [pix2pix demo](https://affinelayer.com/pixsrv/)
-->

<!--
### <a name="week7.1"></a>Week 7 (10/26) - After break check-in
- AI in films
- Course feedback
- Project check-in
- Lab computers
-->

### <a name="week7.1"></a>Week 7.1 (10/12) - Visual Project presentations
- In-class presentations of Visual Project

#### Homework (due before start of next class)
- **Find** an inspirational work using AI for sound/text generation
- **Find** a tool or technique that you would like to use / learn more about / find interesting
- **Write** 2-3 paragraphs about the inspirational work and tool in the [Readings Doc](https://docs.google.com/document/d/1MWwb1x4ylSdiikkB_WQlyuZd_ytVueZV2hIFopOc5_w/edit?usp=sharing)
- Next class you will show the work and technique that you found to the rest of the class

### <a name="week7.2"></a>Week 7.2 (10/14) - Sound / Text Project Discussion

- Discuss Project 3 - Sound / Text


- **Sound / Text Project (due 11/18)**
  - **Create** sound / music, or text using a machine learning algorithm
  - **Put** your project URL and documentation URL into the [Projects Doc](https://docs.google.com/spreadsheets/d/1_eyQ4XfzGKpqMIW7FatoDbHBJSAqyPfrkKcyCI66gbI/edit?usp=sharing)
  - You can incorporate the sound / text output into a larger work, e.g. your earlier visual project, website, printed image, interactive
    program or use the output of the machine learning algorithm as source material for
    your creative process (e.g. generate sound / text and then further manipulate them)
  - The idea is to see how you can use the tools we've looked at in class (or any tool you can find)
    to express your creativity or make a comment on machine learning / AI
  - The work or documentation of it should be accessible on the web (e.g. for a printed work post photos)

  - Required documentation (include on project site or separate page):
    - Name of your project
    - What inspired you to make this work?
    - How does the content of your work related to some of the concepts we've covered in class?
    - What tools did you use? How did the tools affect your creative process? (If you found the
      tools limiting you can also comment on that.)


- Machine learning techniques for text
  - "Vanilla" Neural Networks
    - [Looking inside neural nets](https://ml4a.github.io/ml4a/looking_inside_neural_nets/)
  - Recurrent Neural Networks
    - [3 minute explanation video](https://www.youtube.com/watch?v=C0xoB8L8ms0)
    - [The unreasonable effectiveness of Recurrent Neural Networks](https://karpathy.github.io/2015/05/21/rnn-effectiveness/)
  - Long Short-Term Memory Neural Networks (LSTM)
    - [Understanding LSTMs](https://colah.github.io/posts/2015-08-Understanding-LSTMs/)
  - GPT-2 / 3
    - [GPT explained - multiple difficulty levels](https://towardsdatascience.com/you-can-understand-gpt-3-with-these-youtube-videos-6a30887c928b)
    - [How transformers work](https://towardsdatascience.com/transformers-141e32e69591)
    - [Talk to transformer](https://app.inferkit.com/demo)
    - [GPT-2 Colab - train your own text](https://colab.research.google.com/drive/1uKXS6a9q5qrcU3UdSRpCjYnKHbC-N4pb?usp=sharing)


- **Homework** (due before start of next class):
  - **Review** the [Sound / Text Project requirements](https://github.com/NYUAD-IM/artintel/blob/master/Projects.md#project-3-sound--text-due-1118)
  - **Sign up** for Project 3 groups in the [Projects Doc](https://docs.google.com/spreadsheets/d/1_eyQ4XfzGKpqMIW7FatoDbHBJSAqyPfrkKcyCI66gbI/edit?usp=sharing)
  - **Prepare** to share your project idea next class


## FALL BREAK

### No class (10/19)

### No class (10/21)

## <a name="week8"></a>Week 8 - Sound and Text Tools / Ethics and Bias

### <a name="week8.1"></a>Week 8.1 Sound and Text Tools (10/26)
- Look at inspirational sound/text works and tools

- Machine learning techniques for sound
  - [Magenta](https://magenta.tensorflow.org/)
    - [MusicVAE: A tool for creating music with neural networks](https://medium.com/@wvsharber/musicvae-a-tool-for-creating-music-with-neural-networks-db0f4b84a698)
    - [Piano transcription](https://magenta.tensorflow.org/onsets-frames)
      - [Piano Scribe (In-browser using Magenta.js)](https://piano-scribe.glitch.me/)
    - [Magenta Demos](https://magenta.tensorflow.org/demos)
    - [Melody Mixer](https://experiments.withgoogle.com/ai/melody-mixer/view/)
    - [Magenta Studio lets you use AI tools for inspiration in Ableton Live](https://cdm.link/2019/02/magenta-studio-ai-ableton-live/)
  - [WaveNet A generative model for raw audio](https://deepmind.com/blog/article/wavenet-generative-model-raw-audio)
  - [Generating Audio Using Recurrent Neural Networks](https://apfalz.github.io/rnn/rnn_demo.html)
  - [SampleRNN examples](https://soundcloud.com/samplernn)
  - [SampleRRN code](https://github.com/Unisound/SampleRNN)
  - [Training notes for WaveNet and RNN](https://karlhiner.com/music_generation/wavenet_and_samplernn/)
  - [Technical: Architecture of Speech Recognition](http://slazebni.cs.illinois.edu/spring17/lec26_audio.pdf)
  - Audio deepfakes
    - [This is what a deepfake voice clone used in a failed fraud attempt sounds like](https://www.theverge.com/2020/7/27/21339898/deepfake-audio-voice-clone-scam-attempt-nisos)
    - [Resemble.ai - TTS and cloing](https://www.resemble.ai/)


#### Homework ####
- **Read** [We read the paper that forced Timnit Gebru out of Google](https://www.technologyreview.com/2020/12/04/1013294/google-ai-ethics-research-paper-forced-out-timnit-gebru/) and be prepared to discuss in class

- **Read** an article about GPT-3 and write a 2-3 paragraph response in the [Readings Doc](https://docs.google.com/document/d/1MWwb1x4ylSdiikkB_WQlyuZd_ytVueZV2hIFopOc5_w/edit?usp=sharing)
  - Some suggested articles
    - [Philosophers On GPT-3](https://dailynous.com/2020/07/30/philosophers-gpt-3/)
      - [Responses on Hacker News](https://news.ycombinator.com/item?id=24003384)
    - [Someone let a GPT-3 bot loose on Reddit — it didn’t end well](https://thenextweb.com/neural/2020/10/07/someone-let-a-gpt-3-bot-loose-on-reddit-it-didnt-end-well/)
    - [GPT-3 Creative Fiction](https://www.gwern.net/GPT-3)
    - [OPENAI’S LATEST BREAKTHROUGH IS ASTONISHINGLY POWERFUL, BUT STILL FIGHTING ITS FLAWS](https://www.theverge.com/21346343/gpt-3-explainer-openai-examples-errors-agi-potential)
    - [Here Are A Few Ways GPT-3 Can Go Wrong](https://techcrunch.com/2020/08/07/here-are-a-few-ways-gpt-3-can-go-wrong/)
    - [GPT Crush (look through some examples)](http://gptcrush.com/)

- **Create** a short text by prompting GPT-2/3 and **add** it to the [Google doc](https://docs.google.com/document/d/1w8jeIuuJKWnsXEtVGnN12yoCLtXhg_nX-Q1M7Ld6OuI/edit?usp=sharing). Put the prompted parts of the text you wrote in **bold**.
  - e.g. use [Talk to Transformer](https://app.inferkit.com/demo) or [GPT-2 Colab](https://colab.research.google.com/drive/1uKXS6a9q5qrcU3UdSRpCjYnKHbC-N4pb?usp=sharing)
  - What does your text show about how the model works?
  - How does the response match with what you expected?
  - What do you think of future applications of GPT-3?





### <a name="week8.2"></a>Week 8.2 (10/28) Ethics and Bias
- Discuss social implications and ethics of AI and bias in Machine Learning

<!-- $$$ add homework -->
### Homework (due next class)
- **Work** on your Sound / Text Project idea and be ready to present your idea in class

## <a name="week9"></a>Week 9 - Sound / Text

### <a name="week9.1"></a>Week 9.1 Present Project Ideas for Sound and Text (11/02)
- Present project ideas for Sound and Text

### <a name="week9.2"></a>Week 9.2 - OpenAI and recent developments in AI(11/04)
- Discuss the latest and greatest developments in machine learning / AI

## <a name="week10"></a>Week 10

### <a name="week10.1"></a>Week 10 (11/09) - Other techniques
- Other techniques

### <a name="week10.2"></a>Week 10 (11/11) - Autoencoders (tentative)
- Autoencoders
  - [Autoencoder explained](https://youtu.be/9zKuYvjFFS8?t=56)

## <a name="week11"></a>Week 11 - Sound / Text Project Due

### <a name="week11.1"></a>Week 11.1 - Sound / Text Project Presentations (11/16)

- **Project 3 - Sound / Text Due (11/16)**
- **Present** your Sound / Text project

#### Homework (due before start of next class)
- **Watch** [A Beginner's Guide to Machine Learning with ml5.js](https://www.youtube.com/watch?v=jmznx0Q1fP0) (until 19:00, then it's just credits)
- **Watch** [ml5.js: Image Classification with MobileNet](https://www.youtube.com/watch?v=yNkAuWz5lnY)
- **Read** [Hello ml5.js - A gentle introduction to ml5](https://learn.ml5js.org/#/tutorials/hello-ml5)


### <a name="week11.2"></a>Week 11.2 Final Project Introduction (11/18)

- Chat bots
  - [Eliza](https://web.njit.edu/~ronkowit/eliza.html)
  - [Building an AI-based Chatbot in Python](https://blog.datasciencedojo.com/building-an-ai-based-chatbot-in-python/)
  - [I tricked GPT2 into working like a chatbot. (Reddit)](https://www.reddit.com/r/artificial/comments/cfgpvh/i_tricked_gpt2_into_working_like_a_chatbot_here/)
  - [Talk to Transformer](https://app.inferkit.com/demo)
- [avatars4all](https://github.com/eyaler/avatars4all)
  - Live real-time avatars from your webcam in the browser (multiple Colabs)
- [Use web camera in real-time on google colaboratory](https://github.com/a2kiti/webCamGoogleColab)
  - [Web Cam Demo Colab](https://colab.research.google.com/github/a2kiti/webCamGoogleColab/blob/master/webCamGoogleColab_callbackVersion.ipynb)

- [OpenAI API Access (has link to join waitlist)](https://beta.openai.com/)
- [ml5js Getting Started](https://learn.ml5js.org/#/)
  - [Image Classifier Demo](https://editor.p5js.org/ml5/sketches/ImageClassification)
- [Too big to deploy: How GPT-2 is breaking servers](https://towardsdatascience.com/too-big-to-deploy-how-gpt-2-is-breaking-production-63ab29f0897c)

#### Homework (due before start of next class)
- **Create** An interactive ml5.js sketch (using the p5 editor or your own editor) that uses the webcam, uploaded image from the user, user-entered text, or other user interaction to do something interesting. You can start from one of the ml5.js examples and modify it for your own use.
- **Write** a paragraph of text explaining your sketch and add the link to your sketch and description to the [Readings Doc](https://docs.google.com/document/d/1MWwb1x4ylSdiikkB_WQlyuZd_ytVueZV2hIFopOc5_w/edit?usp=sharing)

## <a name="week12"></a>Week 12 - Interactive Applications

### <a name="week12.1"></a>Week 12 (11/23)
- Review homework
- Techniques for interactive machine learning

#### Homework ####
- **Sign up** for your Final Project group in the [Projects Doc](https://docs.google.com/spreadsheets/d/1_eyQ4XfzGKpqMIW7FatoDbHBJSAqyPfrkKcyCI66gbI/edit?usp=sharing)
- **Develop** the rough idea for your final project and add it to the [Projects Doc](https://docs.google.com/spreadsheets/d/1_eyQ4XfzGKpqMIW7FatoDbHBJSAqyPfrkKcyCI66gbI/edit?usp=sharing)

### <a name="week12.2"></a>Week 12 (11/25) - Final Project Check-in / Work Session
- Final project check-in
- Final project work session

## <a name="week13"></a>Week 13 - LEGISLATIVE DAY - Class meets Monday 11/29

### <a name="week13.1"></a>Week 13.1 (MONDAY 11/29) - Present project ideas
- Short class 10:25-11:40AM
- Present Final Project ideas

### No class (11/30)

### No class (12/02)

## <a name="week14"></a>Week 14

### <a name="week14.1"></a>Week 14.1 (12/07) - Final Project Check-in
- Final project check-in
- Other topics TBD

### <a name="week14.2"></a>Week 14.2 (12/09) - Other topics / TBD
- Other topics TBD

## <a name="week15"></a>Week 15

### <a name="week15.1"></a>Week 15.1 (12/14) - Final project presentations
- **Final project due (12/14)**
- Present final Projects
- Wrap up discussion
- Course evaluations
- Goodbyes for now!
