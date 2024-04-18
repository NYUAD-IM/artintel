# Weekly Schedule / Lecture Notes - Spring 2024

[Schedule Overview / Dates](https://docs.google.com/spreadsheets/d/1kMoCvW7T05H2LyPIRy9KwfkOGXIJbhbk2xHkNOD9AYw/edit?usp=sharing)

* [Week 1 - Introduction / What is Machine Learning?](#week1)
* [Week 2 - Speculative Design / Neural Networks](#week2)
* [Week 3 - More Neural Networks / Speculative Design Project Due](#week3)
* [Week 4 - Visual Project Introduction / Convolutional Neural Networks & Neural Network Training](#week4)
* [Week 5 - Neural Network Training / Politics in AI](#week5)
* [Week 6 - Visual Project Check-in / Bias in Datasets](#week6)
* [Week 7 - Visual Project Due / Sound / Text Project Introduction](#week7)
* SPRING BREAK
* [Week 8 - SPRING BREAK / Sound / Text Tools / Ethics and Bias](#week8)
* [Week 9 - Sound / Text](#week9)
* [Week 10 - Other Techniques Sound](#week10)
* [Week 11 - Sound / Text Project Due / Final Project Introduction](#week11)
* [Week 12 - Interactive Applications / ml5.js](#week12)
* [Week 13 - Present Final Project ideas / NO CLASS](#week13)
* [Week 14 - Final Project check-in / Other topics](#week14)
* [Week 15 - Final Project Due / Course wrap-up and IM Show](#week15)


[Projects Description](https://github.com/NYUAD-IM/artintel/blob/master/Projects.md) - [Projects Spreadsheet](https://docs.google.com/spreadsheets/d/1_eyQ4XfzGKpqMIW7FatoDbHBJSAqyPfrkKcyCI66gbI/edit?usp=sharing) 

## <a name="week1"></a>Week 1 - Introduction / What is Machine Learning?

### <a name="week1.1"></a>Week 1.1 Introduction
- Introductions
  - What is your coding background? Are you familiar with Python? p5js? Linux?
  - Mac / Windows?
- Course overview
  - Balance between creative, conceptual, technical, discussions
  - [Schedule Overview / Dates](https://docs.google.com/spreadsheets/d/1kMoCvW7T05H2LyPIRy9KwfkOGXIJbhbk2xHkNOD9AYw/edit?usp=sharing)
  - Technical tools are rapidly changing - we need to "learn how to learn"
    - We prefer open source tools / data
  - Add programming with AI?
  - Attendance
    - Need to be present at start of class  
  - Lab machines
    - 3x Linux PC with 1080 graphics card
- In-class discussion
  - What do you think about AI?
    - Current capabilities
    - How it's changing society
    - Future capabilities
    - Should we be worried? Excited? Both?
    - How do you want to use AI now, and in the future?
  - Synthetic faces
    - [This Person Does Not Exist](https://thispersondoesnotexist.com/)
    - “Unique, worry-free model photos” https://generated.photos/
    - [Progression in the capabilities of face generation](https://machinelearningmastery.com/wp-content/uploads/2019/06/Example-of-the-Progression-in-the-Capabilities-of-GANs-from-2014-to-2017.png)
  - Deep Fakes
    - [Making a political figure deliver a new speech](https://www.theverge.com/tldr/2018/4/17/17247334/ai-fake-news-video-barack-obama-jordan-peele-buzzfeed)
    - ["AI is destabilizing ‘the concept of truth itself’ in 2024 election" (Washington Post)](https://www.washingtonpost.com/technology/2024/01/22/ai-deepfake-elections-politicians/)
      - [Biden Robocall Deepfake (TikTok)](https://www.tiktok.com/@sineadbovell/video/7326992653684346155)
    - [AI-powered misinformation is the world’s biggest short-term threat, Davos report says (AP)](https://apnews.com/article/artificial-intelligence-davos-misinformation-disinformation-climate-change-106a1347ca9f987bf71da1f86a141968)
  - Text generation
    - [Fake-News-Generating AI Deemed Too Dangerous for Public Release](https://www.extremetech.com/extreme/285857-fake-news-generating-ai-deemed-too-dangerous-for-public-release)
    - [OpenAI Releases Fake News Bot It Previously Deemed Too Dangerous](https://www.extremetech.com/extreme/301662-openai-releases-fake-news-bot-it-previously-deemed-too-dangerous)
    - [Faking the News with Natural Language Processing and GPT-2](https://medium.com/@ageitgey/deepfaking-the-news-with-nlp-and-transformer-models-5e057ebd697d)
    - [ChatGPT](https://openai.com/blog/chatgpt/)
      - [ChatGPT interactive](https://chat.openai.com/chat)
    - [Perplexity](https://www.perplexity.ai/)
      - Large language model combined with web search
  - Speech Synthesis
    - [Val Kilmer reclaims his voice through AI technology after throat cancer](https://www.thenationalnews.com/arts-culture/film/2021/08/21/val-kilmer-reclaims-his-voice-through-ai-technology-after-throat-cancer/)
    - [Ultra-realistic voice cloning / text to speech (TTS)](https://www.descript.com/overdub)
  - Code generation
    - [GitHub Copilot](https://copilot.github.com/)
  - Text to image
    - [OpenAI DALL-E](https://openai.com/blog/dall-e/)
    - [Mindblowing AI pixel art](https://boingboing.net/2021/08/19/mindblowing-ai-pixel-art.html)
      - [CLIPIT PixelDraw Colab](https://colab.research.google.com/drive/1uya2CzekydPASALHtgrwxOekBMlaWGON?usp=sharing)
    - [OpenAI DALL-E 2](https://openai.com/dall-e-2/)
    - [Midjourney](https://midjourney.com/)
    - [Stable Diffusion examples](https://neuroflash.com/blog/stable-diffusion-examples-3/)
  - [Florida cops use AI to target people for a new "enhanced scrutiny" program](https://boingboing.net/2021/07/27/florida-cops-use-ai-to-target-people-for-a-new-enhanced-scrutiny-program.html)
  - [Moral Machine](https://www.moralmachine.net/) - A platform for public participation in and discussion of the human perspective on machine-made moral decisions
 
<!-- Down, alas  - [B0na F1de Artist Collective](https://www.b0naf1de.com/) - Jonghyun Jee's final project -->

  #### Homework (due before start of next class)
  - **Sign up** for Discord using the [Discord invite]([https://brightspace.nyu.edu/d2l/le/lessons/110671/units/5693439](https://brightspace.nyu.edu/d2l/le/lessons/351324/units/9729132)) on Brightspace  (optional, recommended)
    - Discord is a third-party service. Use of Discord is optional (non-NYU service), please consider anything you post there to be public.
  - **Read**
    - Creative AI:  [https://medium.com/@creativeai/creativeai-9d4b2346faf3](https://medium.com/@creativeai/creativeai-9d4b2346faf3)  
<!-- Down    - What is AI &amp; History (Optional/Recommended): [Chapter 1 - Introduction - Artificial Intelligence a Modern Approach](http://web.cecs.pdx.edu/~mperkows/CLASS_479/2017_ZZ_00/02__GOOD_Russel=Norvig=Artificial%20Intelligence%20A%20Modern%20Approach%20(3rd%20Edition).pdf) -->

<!--
  - **Find** an interesting article about AI / machine learning published within the last year. The article could show a creative application of AI, recent developments in machine learning, controversy over AI ethics, explain how a particular model / algorithm works, etc. Try to find something that will provoke disussion with the class
    - **Post** article to Discord #artintel or email it to the professor before the start of next class
    - **Be prepared to discuss** your article with the class
-->

<!--
  - **Create** a pixel art image using CLIPIT PixelDraw **OR** a face using StyleGAN2
    - **Create** a pixel art image using the [CLIPIT PixelDraw example](https://colab.research.google.com/drive/1uya2CzekydPASALHtgrwxOekBMlaWGON?usp=sharing) and post it in the Discord (or send via email). If you have problems, ask for help! Make sure to save the example to your Google Drive before making edits. Why did you choose your prompt and what do you think the result reveals about how the image generation algorithm works? You can uncheck ```use_pixeldraw``` to see the generated image without pixelation.
    - **Create** a face using the [StyleGAN2 Colab example](https://colab.research.google.com/gist/mangtronix/e19e0c4025fb20e26b7f83990780f0a0/stylegan2-google-colab-example.ipynb) and post it in the Discord (or send via email). If you have problems, ask for help! Make sure to save the example to your Google Drive before making edits.
      - (Optional) Post your generated face or video on social media (or through email, etc) and see what the response is. It's up to you to decide how to communicate your post (you can make it clear it's a generated face or not).
-->




### <a name="week1.1"></a>Week 1.2
- Discussion - Creative AI

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

  - **Find** a creative tool that uses AI and **create** a post on the [Brightspace Discussion]([https://brightspace.nyu.edu/d2l/le/110671/discussions/topics/261633/View](https://brightspace.nyu.edu/d2l/le/265669/discussions/topics/374245/View)) with a link and short explanation (2-3 paragraphs) of what's interesting about it
    - Include something you made with the tool (e.g. image, sound, text)
  - (Optional) Deep Dream details (we’ll look at this again later when we talk about Convolutional Neural Networks) https://ai.googleblog.com/2015/06/inceptionism-going-deeper-into-neural.html

<!--
- **Read** Looking Inside Neural Networks https://ml4a.github.io/ml4a/looking_inside_neural_nets/

-->

## <a name="week2"></a>Week 2 - Speculative Design / Neural Networks

### <a name="week2.1"></a>Week 2.1 Introduction to Speculative Design
- Review homework (new image, interesting applications)
- Talk about Speculative Design project
  - <a href="https://github.com/NYUAD-IM/artintel/blob/master/Projects.md#project-1-speculative-design-due-921">Speculative Design Project requirements<a/>
- Form groups for Speculative Design Project
- AI in the news
  - [Deepfake images of Taylor Swift went viral on X, evading moderation and sparking outrage (NBC News)](https://www.nbcnews.com/tech/misinformation/taylor-swift-nude-deepfake-goes-viral-x-platform-rules-rcna135669) (Jan 2024)
  - [Deepfakes and the History of Faked Photography](https://blogs.cardiff.ac.uk/openfordebate/deepfakes-and-the-history-of-faked-photography/)
  - [Ad for generating LinkedIn content into your own account using GPT (YouTube)](https://youtu.be/LAa76dwAHZo?si=1eQUmFeHLOAAXYHX&t=441) (Jan 2024)
  - [AI needs energy breakthroughs including fusion, says OpenAI's Sam Altman](https://www.datacenterdynamics.com/en/news/ai-needs-energy-breakthroughs-including-fusion-says-openais-sam-altman/)
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
    - [Elon Musk's Neuralink 'shows monkey playing Pong with mind' (BBC)](https://www.bbc.com/news/technology-56688812)
  - [A Facebook-scale simulator to detect harmful behaviors (Facebook AI)](https://ai.facebook.com/blog/a-facebook-scale-simulator-to-detect-harmful-behaviors/)

#### Homework (due before start of next class)
- **Read**
  - [Speculative Everything](https://readings.design/PDF/speculative-everything.pdf)
    - Read Chapter 1, Chapter 2 (pages 11-16), Chapter 3
- **Review** the [Speculative Design Project requirements](https://github.com/NYUAD-IM/artintel/blob/master/Projects.md#project-1-speculative-design-due-921)
<!--
- **Make your group** for the Speculative Design project in the [Projects Doc](https://docs.google.com/spreadsheets/d/1_eyQ4XfzGKpqMIW7FatoDbHBJSAqyPfrkKcyCI66gbI/edit?usp=sharing)
- **Start** developing ideas for a speculative design project about future applications of AI and be prepared to share your idea next class
- **Update** your idea in the [Projects Doc](https://docs.google.com/spreadsheets/d/1_eyQ4XfzGKpqMIW7FatoDbHBJSAqyPfrkKcyCI66gbI/edit?usp=sharing) before class.
-->

### <a name="week2.2"></a>Week 2.2 Neural Networks
- Lab etiquette
  - Clean after yourselves
  - Food waste goes outside (there ain't no flies on us!)
- Neural Networks
  - [Professor’s perceptron paved the way for AI – 60 years too soon](https://news.cornell.edu/stories/2019/09/professors-perceptron-paved-way-ai-60-years-too-soon)
  - [Perceptron (Wikipedia)](https://en.wikipedia.org/wiki/Perceptron)
  - [Neural Networks (ml4a)](https://ml4a.github.io/ml4a/neural_networks/)
  - [What’s the Difference Between Supervised, Unsupervised, Semi-Supervised and Reinforcement Learning?](https://blogs.nvidia.com/blog/2018/08/02/supervised-unsupervised-learning/)
- Classification Using Neural Networks
  - [Classification of Rock, Paper, Scissors ](https://www.youtube.com/watch?v=KNAWp2S3w94&feature=youtu.be&t=50)
<!-- - Introduction to neural network training -->
- [Positive AI experiments (Instagram / Whichlight)](https://www.instagram.com/whichlight/)
- Speculative Desing Project
  - [Slumber by NightShift Ltd](https://docs.google.com/presentation/d/1BqHRZHUzuFWQbPOYvL0Jp42iB-kpd77nB1zNZLZ7KEg/edit?usp=sharing) - Speculative design project by Katie Ferreol	and Michael Leo
    - "Being a satirical call-out the toxic "hustle" culture haunting Generation Z, our project is a robotic hand-machine/AI that helps you complete tasks while you are in REM sleep. This is a haunting message to humans slowly becoming slaves to capitalism, reaching the point sacrificing self-care in order to succeed."


#### Homework (due before start of next class)
- Work on your Speculative Design Project


## <a name="week3"></a>Week 3 - More Neural Networks / Speculative Design Presentations

### <a name="week3.1"></a>Week 3.1 - More Neural Networks  
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
  - [ConvNetJS digit classification demo](https://cs.stanford.edu/people/karpathy/convnetjs/demo/mnist.html)
  - [WaveNet audio generation](https://deepmind.com/blog/article/wavenet-generative-model-raw-audio)
  - [StyleGAN explanation](https://towardsdatascience.com/explained-a-style-based-generator-architecture-for-gans-generating-and-tuning-realistic-6cb2be0f431)
  - [Convolutional Neural Network Colab](https://colab.research.google.com/github/NYUAD-IM/artintel/blob/master/Code/Week_04/Convolutional_Neural_Network.ipynb#scrollTo=Iv1SLDu_bYXh)
  - [OpenAI Microscope](https://openai.com/blog/microscope/)
    - [Inception 1 - Deep Dream](https://microscope.openai.com/models/inceptionv1?models.technique=deep_dream)


#### Homework (due before start of next class)
- Work on your Speculative Design Project
  - Update the projects spreadsheet with your group and one sentence description

<!--
- Read [Excavating AI - Politics in AI Datasets](https://excavating.ai/) and be prepared to discuss in class
-->

### <a name="week3.2"></a>Week 3.2 - More neural networks, politics of AI
<!--
### <a name="week3.2"></a>Week 3.2 - Speculative Design Workshop (9/16)
- Review speculative design ideas
- Start working on the design ideas

-->

<!--
#### Homework (due before start of next class)
- **Create** a new image or other output using one of these Colab notebooks (use your own input images / text / etc rather than the built-in ones)
  - [Useful Colabs (A.rt I.ntel)](https://github.com/NYUAD-IM/artintel/blob/master/UsefulColabs.md) - includes links to explanations of Google Colab
  - [12 Colab Notebooks that matter](https://towardsdatascience.com/12-colab-notebooks-that-matter-e14ce1e3bdd0)
  - **Post** your image / output to Week 3 Brightspace discussion with a description (2 paragraphs) of how you made it
  - If you have a problem with the Tensorflow version (e.g "AdamOptimizer not found") add [this code](https://colab.research.google.com/notebooks/tensorflow_version.ipynb)
-->

#### Homework (due before start of next class)
- Finish your Speculative Design project
  - Submit via [Projects Spreadsheet](https://docs.google.com/spreadsheets/d/1_eyQ4XfzGKpqMIW7FatoDbHBJSAqyPfrkKcyCI66gbI/edit?usp=sharing)
  - Prepare a 5-10 minute presentation

## <a name="week4"></a>Week 4 - Speculative Design Presentations / Visual tools

### <a name="week4.1"></a>Week 4.1 - Speculative Design Presentations / Introduction to Visual tools
Speculative Design Project Presentations
- Speculative Design Project Presentations
  - Give a 5-10 minute presentation of your project and be prepared for feedback from the class

- Review homework (issues)
  - Use of "free" commercial tools
  - Learning how to learn

- Discuss Visual Project
  - [Visual Project requirements](https://github.com/NYUAD-IM/artintel/blob/master/Projects.md#project-2-visual-due-last-class-before-spring-break-1014")
    - Create an *artwork* that is an image, series of images or video using a machine learning algorithm (e.g. using Colab, Midjourney, Stable Diffusion, other online tools)
    - The work should somehow address one of the concepts we’ve covered in class (e.g. extending creativity, who is the author?, real/fake, AI revolution, bias, etc)
    - The work must make a creative or critical statement (simple use of the tools is not enough)

- Introduction to Visual tools  
  
- Discussion - Authorship and AI Tools
  - ChatGPT
    - [Introductory slides on what the technology is by NYU Prof. Habash](https://docs.google.com/presentation/d/1W8o1FQmWlQ8g9cPFHpxMQUFJvXTwAybU/edit#slide=id.p1)
    - [Advice provided by NYU Office of the Provost](https://t.e2ma.net/click/ax6aexc/inkp93f/qh1cpfg)
    - [Some Colleges Cautiously Embrace Wikipedia](https://www.chronicle.com/article/some-colleges-cautiously-embrace-wikipedia/)
  - Stable Diffusion / Midjourney
  - Class policy
  - Crediting / referencing AI tools
    - Disclose prompt

- Class tools
  - [Easy Diffusion](https://easydiffusion.github.io/)
  - [ComfyUI](https://github.com/comfyanonymous/ComfyUI)
  - [Shiffbot - Daniel Shiffman AI bot in p5js](https://shiffbot.withgoogle.com/)
 
- Obsolete-ish tools   
  - Colab / Neural Network Introduction
    - [Colab Introduction (Colab](https://colab.research.google.com/notebooks/intro.ipynb)
    - [Deep Learning Basics (Colab)](https://colab.research.google.com/github/lexfridman/mit-deep-learning/blob/master/tutorial_deep_learning_basics/deep_learning_basics.ipynb)
    - [Python Tutorial With Google Colab (Colab)](https://colab.research.google.com/drive/1sLkLW3H3PbSC1kyeNNt5WpQivcYqBg69?usp=sharing)

    - [VQGAN+Clip with WikiArt GAN - DALL-E alternative (Colab)](https://colab.research.google.com/drive/1kUVn_pkm83nCWFNAQxNzSS9glxHkZi1Z?usp=sharing)
      - There are English versions of this Colab available, the version above is working with the model from WikiArt. See [Generating AI “Art” with VQGAN+CLIP](https://learn.adafruit.com/generating-ai-art-with-vqgan-clip) for instructions
      - Inspired by [OpenAI DALL-E text to image](https://openai.com/blog/dall-e/)


- ["Learning to be me" by Greg Egan](https://philosophy.williams.edu/files/Egan-Learning-to-Be-Me.pdf) - short story about uploading consciousness into digital implant written in 1990

### <a name="week4.2"></a>Week 4.2 - Visual Tools Continued
- Announcements
  - Talk by Yann LeCun Feb 19 5pm [RSVP](https://forms.gle/Z6mYyLGy9DZSdZKt5)
  - [Class / project schedule](https://docs.google.com/spreadsheets/d/1kMoCvW7T05H2LyPIRy9KwfkOGXIJbhbk2xHkNOD9AYw/edit?usp=sharing)
    - [Visual Project](https://github.com/NYUAD-IM/artintel/blob/master/Projects.md) is **due Tuesday March 5**
    - IM End of Semester Showcase is Thursday May 9 5-8pm (same day as our last class)


- Creative work examples
  - Rafik Anadol
    - [Art in the age of machine intelligence | Refik Anadol (YouTube / TED)](https://www.youtube.com/watch?v=UxQDG6WQT5s)
    - [On GPS: The art of artificial intelligence (CNN)](https://edition.cnn.com/videos/tech/2023/09/08/exp-gps-0903-the-art-of-artificial-intelligence.cnn)
  - [Real-time Generation of Panoramic scenes from Voice using a custom Stable Diffusion pipeline (2023)
](https://bmolab.artsci.utoronto.ca/?page_id=250)
  - [aiartists.org](https://aiartists.org/)
    - [Sofia Crespo](https://aiartists.org/sofia-crespo)
    - [Alexander Rubin](https://aiartists.org/alexander-reben)
    - [Refik Anadol](https://aiartists.org/refik-anadol)
    - [Joy Buolamwini](https://aiartists.org/joy-buolamwini)
    - [Mario Klingeman](https://aiartists.org/mario-klingemann)

- Neural Network Training References
  - [How Neural Networks are Trained](https://ml4a.github.io/ml4a/how_neural_networks_are_trained/)
  - [Classification Colab](https://colab.research.google.com/github/tensorflow/docs/blob/master/site/en/tutorials/keras/classification.ipynb#scrollTo=yWfgsmVXCaXG)
  - [ml4a Demos](https://ml4a.github.io/demos/)
  - [ml5js Webcam Classification Demo](https://editor.p5js.org/AndreasRef/sketches/BJkaHBMYm)
  - [MobileNet details](https://towardsdatascience.com/review-mobilenetv1-depthwise-separable-convolution-light-weight-model-a382df364b69)
  - [How to Train StyleGAN to Generate Realistic Faces](https://towardsdatascience.com/how-to-train-stylegan-to-generate-realistic-faces-d4afca48e705)
    - (Advanced)[Training a GAN from your Own Images: StyleGAN2 ADA (YouTube)](https://www.youtube.com/watch?v=kbDd5lW6rkM)

- Generative Adversarial Networks (GANs)
  - [Supervised vs Unsupervised Learning: Difference Between Them](https://www.guru99.com/supervised-vs-unsupervised-learning.html)
    - Supervised
      - labelled input and output data (known inputs to known outputs / answers)
      - model maps new input to predicted output
      - typically used for classification and regression (prediction)
    - Unsupervised
      - unlabelled data (raw inputs, no outputs)
      - model finds patterns in input data
      - model maps new input to found pattern in training data
      - typcially used for clustering and association
  - [A Gentle Introduction to Generative Adversarial Networks (GANs)](https://machinelearningmastery.com/what-are-generative-adversarial-networks-gans/)
  - [Deep Convolutional Generative Adversarial Network (Tensorflow docs)](https://www.tensorflow.org/tutorials/generative/dcgan)
    - [Run in Colab](https://colab.research.google.com/github/tensorflow/docs/blob/master/site/en/tutorials/generative/dcgan.ipynb)

  - [The Illustrated VQGAN](https://ljvmiranda921.github.io/notebook/2021/08/08/clip-vqgan/)
  - [Explained: A Style-Based Generator Architecture for GANs - Generating and Tuning Realistic Artificial Faces](https://towardsdatascience.com/explained-a-style-based-generator-architecture-for-gans-generating-and-tuning-realistic-6cb2be0f431)

  - [Stable Diffusion](https://stability.ai/blog/stable-diffusion-v2-release) 
    - [Stable Diffusion lab access (Brightspace)](https://brightspace.nyu.edu/d2l/le/lessons/351324/units/9729133)
    - [Stable Diffusion litigation](https://stablediffusionlitigation.com/) - includes simple (biased) description of how Stable Diffusion works
    - [Do AI images violate copyright? A lawyer explains the Stable Diffusion lawsuit](https://boingboing.net/2023/01/23/do-ai-images-violate-copyright-a-lawyer-explains-the-stable-diffusion-lawsuit.html)
    - Prompt ideas
      - [OpenArt Prompt Book](https://openart.ai/promptbook)
      - [Prompt Hero](https://prompthero.com/) - (note some outputs are questionable - common to many prompt sites)
  - [Generative AI for Makers (Makezine)](https://makezine.com/article/craft/fine-art/generative-ai-for-makers-ai-has-truly-arrived-and-its-here-to-help-you-make-and-craft/)

  - Machine learning on our lab computers
    - [Lab Computer access](LabComputers.md)
    - [Stable Diffusion UI (Easy Diffusion)](https://github.com/cmdr2/stable-diffusion-ui)

  - Machine learning in the browser
    - [ml5.js](https://ml5js.org/)
    - [ml5.js Webcam Classification Demo](https://editor.p5js.org/AndreasRef/sketches/BJkaHBMYm)  


- AI in the news (2023)
  - [Experts say she will end humanity. Here's the fix, w Elon Musk, ChatGPT, AI robots.
](https://www.youtube.com/watch?v=zpRM25pUD8w)
    - [DeepMind’s AI Trained For 5 Years... But Why? - cooperative machine learning (2 Minute Papers)](https://www.youtube.com/watch?v=HTON7odbW0o)
  - [Bing: “I will not harm you unless you harm me first”](https://simonwillison.net/2023/Feb/15/bing/)

  - Older news (from 2021, almost ancient history)
    - [Police to Deploy Snitch Bots That Search for 'Undesirable Social Behaviors'](https://gizmodo.com/singapore-police-to-deploy-snitch-bots-that-search-for-1847629866)
    - [Pandemic Robots Deployed in Parks to Remind Humans of Their Own Mortality](https://gizmodo.com/pandemic-robots-deployed-in-singapore-parks-to-remind-h-1843335679)
    - [Police use Tesla's autopilot to stop the car after drunk driver passes out](https://boingboing.net/2021/09/20/police-use-teslas-autopilot-to-stop-the-car-after-drunk-driver-passes-out.html)



#### Homework (due before start of next class)

- **Try** to get Easy Diffusion and ComfyUI working on your laptop before the visual tools workshop on Tuesday
  - Don't worry if your machine is not capable of running the software, we will work in groups and have our lab machines available for use

- **Watch** [How AI Image Generators Work (Stable Diffusion / Dall-E) - Computerphile](https://youtu.be/1CIpzeNxIhU)
 
Reading:
- **Read** [The AI Revolution - Part 1](https://waitbutwhy.com/2015/01/artificial-intelligence-revolution-1.html)
and AI develops more capabilities? How will the relationship between humans and machines change?
- **Write** 3-4 paragraphs of response in the [Brightspace Readings Discussion](https://brightspace.nyu.edu/d2l/le/351324/discussions/topics/450522/View)
  - How far do you think we are towards Artificial General Intelligence? What are some of the changes (positive and negative) you see coming as machine learning  

## <a name="week5"></a>Week 5 - Visual Neural Networks

### <a name="week5.1"></a>Week 5.1 - Discussion / Project Ideas / Generative Networks
- Discuss reading
- AI in the news (2024)
  - [OpenAI’s Video Generator Sora Is Breathtaking, Yet Terrifying (Gizmodo)](https://gizmodo.com/openai-video-generator-sora-is-breathtaking-terrifying-1851261593)
  - [OpenAI Sora video generator (OpenAI)](https://openai.com/research/video-generation-models-as-world-simulators)
    
- Visual tools in-class workshop
  - Using [Easy Diffusion](EasyDiffusion.md)
  - Settings
    - Use [Realistic Vision](https://civitai.com/models/4201/realistic-vision-v60-b1) model based on SD 1.5
    - Enable 'blur NSFW'
  - Prompt challenge
    - Make a realistic image
    - Change the image to have a specific artistic style - try different artists
    - Make portraits of different professions - how are they biased?
    - Make a self portrait
    - Use Img2Img to stylize an existing image
      - Try this on an image of yourself
    - Use PoseNet to create a scene from utopia / dystopia
      - Can make a PoseNet pose using [PoseMy.art](https://app.posemy.art/)
     
- Share project ideas
  - Discuss use of tools

#### Homework
- Start thinking about Visual Project

### <a name="week5.2"></a>Week 5.2 - More Visual Tools
- Lab machine access
  - Easy Diffusion is available remotely using [IM Lab computers](https://brightspace.nyu.edu/d2l/le/lessons/351324/units/9729133) while on VPN

- Uncanny Valley
  - [What Is the Uncanny Valley?](https://spectrum.ieee.org/what-is-the-uncanny-valley)
    - [The Uncanny Valley: The Original Essay by Masahiro Mori](https://spectrum.ieee.org/the-uncanny-valley)
  - [Honda's new ASIMO robot, more human-like than ever](https://phys.org/news/2014-04-honda-asimo-robot-human-like.html) 2014
  - [Sophia, Hanson Robotics’ most advanced human-like robot](https://www.hansonrobotics.com/sophia/)
    - [The agony of Sophia, the world's first robot citizen condemned to a lifeless career in marketing (Wired)](https://www.wired.co.uk/article/sophia-robot-citizen-womens-rights-detriot-become-human-hanson-robotics)

- AI in the news (2023)
  - [Imagining new Indian sci-fi stories through the power of AI (2023)](https://wepresent.wetransfer.com/stories/prateek-arora-midjourney-indian-cinema)
    - Imagining Indian Sci-Fi
  - [How People with Disabilities Are Using AI to Improve Their Lives (2019)](https://www.pbs.org/wgbh/nova/article/people-with-disabilities-use-ai-to-improve-their-lives/)
  - [Hikvision Markets Uyghur Ethnicity Analytics, Now Covers Up](https://ipvm.com/reports/hikvision-uyghur)
  - [Facebook apology as AI labels black men 'primates'](https://www.bbc.com/news/technology-58462511)
  - [Lying to the ghost in the machine](http://www.antipope.org/charlie/blog-static/2021/03/lying-to-the-ghost-in-the-mach.html)
  - [Meet the Artist Using Ritual Magic to Trap Self-Driving Cars (Vice, 2017)](https://www.vice.com/en/article/ywwba5/meet-the-artist-using-ritual-magic-to-trap-self-driving-cars)
 
- AI in the news (2024)
  - [This Tech Exec Quit His Job to Fight Generative AI's Original Sin (Wired)](https://www.wired.com/story/ai-executive-ed-newton-rex-turns-crusader-stand-up-for-artists/)
    - [Fairly Trained](https://www.fairlytrained.org/) - company that certifies training data was fairly obtained
  - [Spawning AI](https://spawning.ai/) - "Data Governance for Generative AI"
 
- Realtime generative AI demo (TouchDesigner / ComfyUI / Stable Diffusion) - time permitting
 
<!--
  
- Stable Diffusion Workshop
  - [Stable Diffusion Guide (artintel)](StableDiffusion.md)

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
-->

<!-- add training exercise -->

#### Homework (due before start of next class)

- [Make a post in the Brightspace Week 5 Discussion](https://brightspace.nyu.edu/d2l/le/351324/discussions/topics/460852/View)
  - Create an image from one of your own photographs combined with a prompt that provokes a reaction about AI
  - Must use Easy Diffusion, either own machine or on a [lab machine](https://brightspace.nyu.edu/d2l/le/lessons/351324/units/9729133)
  - See Discussion topic for details

Visual project initial idea:
- **Make your group** for the Visual Design project in the [Projects Doc](https://docs.google.com/spreadsheets/d/1_eyQ4XfzGKpqMIW7FatoDbHBJSAqyPfrkKcyCI66gbI/edit?usp=sharing)
- **Start** developing ideas for the Visual Project
  and be prepared to share your idea next class
- **Update** your idea in the [Projects Doc](https://docs.google.com/spreadsheets/d/1_eyQ4XfzGKpqMIW7FatoDbHBJSAqyPfrkKcyCI66gbI/edit?usp=sharing) before class.
  
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

### <a name="week6.1"></a>Visual Project / Stable Diffusion
- Look at generative image homework
  
- Project idea discussion and feedback

- AI in the news
  - [OpenAI Gives ChatGPT a Better ‘Memory’ (New York Times)](https://www.nytimes.com/2024/02/13/technology/openai-gives-chatgpt-a-better-memory.html) (2024)

  - [Netflix Made an Anime Using AI Due to a 'Labor Shortage,' and Fans Are Pissed (Vice)](https://www.vice.com/en/article/bvmqkv/netflix-anime-dog-and-the-boy-ai-generated-art)
  - [Thousands of People Can’t Stop Watching AI-Generated Sitcom ‘Nothing, Forever’ (Vice)](https://www.vice.com/en/article/88qy3p/thousands-of-people-cant-stop-watching-ai-tv-show-nothing-forever)
  - [AI-Created Images Aren’t Protected By Copyright Law According To U.S. Copyright Office - 2023-02-23](https://www.forbes.com/sites/mattnovak/2023/02/22/ai-created-images-in-new-comic-book-arent-protected-by-copyright-law-according-to-us-copyright-office/?sh=467fd5e27ce4) (2023)
  
> “We conclude that Ms. Kashtanova is the author of the Work’s text as well as the selection, coordination, and arrangement of the Work’s written and visual elements. That authorship is protected by copyright. However, as discussed below, the images in the Work that were generated by the Midjourney technology are not the product of human authorship”
  
> Kashtanova tried to argue her textual prompts into Midjourney were a type of creation or authorship, a claim the Copyright Office rejected.

> “A person who provides text prompts to Midjourney does not ‘actually form’ the generated images and is not the ‘master mind’ behind them. [...] The information in the prompt may ‘influence’ generated image, but prompt text does not dictate a specific result,” the Copyright Office explained.
  
> “The Office does not question Ms. Kashtanova’s contention that she expended significant time and effort working with Midjourney. But that effort does not make her the ‘author’ of Midjourney images under copyright law,” the Copyright Office wrote.

  - [Tesla Autopilot Duped By ‘Phantom’ Images (2020)](https://threatpost.com/tesla-autopilot-duped-by-phantom-images/152491/)

Stable Diffusion training
- Stable Diffusion 2 was trained on ~2.3 billion image / text pairs from a subset of images from [LAION-5B](https://laion.ai/blog/laion-5b/)
  - [LAION-5B CLIP Search Demo](https://rom1504.github.io/clip-retrieval/?back=https%3A%2F%2Fknn.laion.ai&index=laion5B-H-14&useMclip=false) search for images in the LAION-5B dataset from text description (not working in 2024)
- [Exploring 12 Million of the 2.3 Billion Images Used to Train Stable Diffusion’s Image Generator](https://waxy.org/2022/08/exploring-12-million-of-the-images-used-to-train-stable-diffusions-image-generator/)
  - [laion-aesthetic-6pls search](https://laion-aesthetic.datasette.io/laion-aesthetic-6pls/images) (not working in 2024)
- [Multimodal datasets: misogyny, pornography, and malignant stereotypes (arXiv)](https://arxiv.org/abs/2110.01963) [(pdf)](https://arxiv.org/pdf/2110.01963.pdf)
- [AI image training dataset found to include child sexual abuse imagery](https://www.theverge.com/2023/12/20/24009418/generative-ai-image-laion-csam-google-stability-stanford)

- Stable Diffusion demo in ComfyUI

- [Dreambooth](https://dreambooth.github.io/)
  - Inject your own characters into Stable Diffusion (outdated as of 2024, new technique is to use a Lora model)

<!--
#### Homework (due before start of next class)
  - **Read** [Excavating AI: The Politics of Images in Machine Learning Training Sets](https://www.biennial.com/journal/issue-9/excavating-ai-the-politics-of-images-in-machine-learning-training-sets)
and AI develops more capabilities? How will the relationship between humans and machines change?
  - **Write** 3-4 paragraphs of response in the [Brightspace Readings Discussion](https://brightspace.nyu.edu/d2l/le/265669/discussions/topics/371625/View)
-->

### <a name="week6.2"></a>Week 6.2 - Bias in Datasets
<!-- - Reading discussion - The Politics of Images in Machine Learning Training Sets -->
- AI in the news
  - [AI screw-up results in man being fined $400 for scratching his head
(BoingBoing)](https://boingboing.net/2024/02/15/man-fined-for-scratching-his-head.html) (2024)

Bias in datasets, limits of models
- [AI colorization (Twitter)](https://twitter.com/gwenckatz/status/1381652071695351810)
- [Joy Buolamwini - How I'm fighting bias in algorithms](https://www.ted.com/talks/joy_buolamwini_how_i_m_fighting_bias_in_algorithms)
- [Hidden Bias](https://pair.withgoogle.com/explorables/hidden-bias/)

AI for medical screening
  - [AI outperforms doctors at spotting breast cancer, say NYUAD researchers (2021)](https://www.thenationalnews.com/uae/2021/10/06/ai-outperforms-doctors-at-spotting-breast-cancer-say-researchers/)
  - [Improving Breast Cancer Detection in Ultrasound Imaging Using AI (tech details)](https://developer.nvidia.com/blog/improving-breast-cancer-detection-in-ultrasound-imaging-using-ai/)
  - [Artificial intelligence system reduces false-positive findings in the interpretation of breast ultrasound exams
(paper)](https://www.nature.com/articles/s41467-021-26023-2)
    
- Project checkin / work session

#### Homework (due before start of next class)
- **Finish** your Visual Project
- **Add** the links to your project and documentation to the [Projects Doc](https://docs.google.com/spreadsheets/d/1_eyQ4XfzGKpqMIW7FatoDbHBJSAqyPfrkKcyCI66gbI/edit?usp=sharing)
- **Prepare** a 5 minute presentation of your project and be ready to receive and give feedback
  - Do not exceed 5 minutes! Practice your presentation to check the timing
  - Share your most important ideas / concepts / statements and leave time for dicussion

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
### <a name="week7.1"></a>Week 7 (/26) - Autoencoders, other forms of neural networks (or guest lecture)
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

### <a name="week7.1"></a>Week 7.1 - Visual Project Presentations
- In-class presentations of Visual Project

- Midterm course review
  - How is the course going for you?
  - What's working well?
  - Any changes / suggestions?
  - Project feedback
    - Make an artistic / creative statement as well as using the tools
    - Can you make something that provokes emotions and questions in the audience?
  - Reading feedback
    - Write your own opinion / response to the article
    - Don't summarize the article (we have tools for that)

#### Homework (due before start of next class - Thursday Mar 7)
- **Find** an inspirational work using AI for sound/text/code generation
- **Find** a tool or technique that you would like to use / learn more about / find interesting
- **Write** 2-3 paragraphs about the inspirational work and tool in the [Brightspace Discussion](https://brightspace.nyu.edu/d2l/le/351324/discussions/topics/450524/View)

  
### <a name="week7.2"></a>Week 7.2 - Introduction to Sound / Text
- Look at inspirational sound/text works and tools

- Perplexity.ai examples
  - [System administration (perplexity.ai)](https://www.perplexity.ai/search/tmux-create-session-jetHgQbfQ0GX2W921QKRyw?s=c)
  - [Code generation (perplexity.ai)](https://www.perplexity.ai/search/give-me-a-sVNpPMXjQz6liz2JqLnKkQ?s=c)

- [What Is ChatGPT Doing and Why Does It Work?](https://writings.stephenwolfram.com/2023/02/what-is-chatgpt-doing-and-why-does-it-work/) (2023)
  - Amazing technical deep dive
 
- Class references
  - [Sharing deepfake intimate images to be criminalised in England and Wales (The Guardian)](https://www.theguardian.com/society/2023/jun/27/sharing-deepfake-intimate-images-to-be-criminalised-in-england-and-wales)
  - [EMO: Emote Portrait Alive](https://humanaigc.github.io/emote-portrait-alive/)
  - [SHEEN AI](https://www.sheen-ai.com/) - audio to visuals

- **Sound / Text Project (due Tuesday April 2)**
  - [Sound / Text Project requirements](https://github.com/NYUAD-IM/artintel/blob/master/Projects.md#project-3-sound--text-due-tuesday-42)

#### Homework (for the break)
- No homework! Have a great break!

## SPRING BREAK / SPRING BREAK / SPRING BREAK

## <a name="week8"></a>Week 8 - SPRING BREAK / Sound and Text Tools / Ethics and Bias
### <a name="week8.1"></a>Week 8.1 NO CLASS - Spring Break

### <a name="week8.2"></a>Week 8.2 Text Models / Tools

- Introduce [Project 3 - Sound / Text / Code](Projects.md)

<!--
- Markov chains for text generation
  - [ML Basics: Markov Models Write Fairy Tales](https://thagomizer.com/blog/2017/11/07/markov-models.html)
  - [Markov chain example (p5editor)](https://editor.p5js.org/mangtronix/sketches/fIDj9rhjC)
-->

- Machine learning techniques for text
  - Review of "Vanilla" Neural Networks
    - [Looking inside neural nets](https://ml4a.github.io/ml4a/looking_inside_neural_nets/)

  - Sequence to Sequence Models
    - [Sequence to Sequence model diagrams](https://towardsdatascience.com/transformers-141e32e69591)
    - [Visualizing A Neural Machine Translation Model](https://jalammar.github.io/visualizing-neural-machine-translation-mechanics-of-seq2seq-models-with-attention/)


  - Recurrent Neural Networks
    - [3 minute explanation video](https://www.youtube.com/watch?v=C0xoB8L8ms0)
    - [The unreasonable effectiveness of Recurrent Neural Networks](https://karpathy.github.io/2015/05/21/rnn-effectiveness/)

<img src="Assets/transformer_architecture.jpg" width="300px" />

Transformer architecture diagram from ["Attention Is All You Need"](https://arxiv.org/abs/1706.03762)

GPT
- [Illustrated GPT-2](https://jalammar.github.io/illustrated-gpt2/)
- [How GPT3 works](https://jalammar.github.io/how-gpt3-works-visualizations-animations/)



- Embeddings
  - [Image t-SNE viewer](https://ml4a.github.io/guides/ImageTSNEViewer/)
    - Demonstrates how to visualize a high dimensional embedded space in 2D/3D so we can make sense of it
  - [Glossary of Deep Learning: Word Embedding](https://medium.com/deeper-learning/glossary-of-deep-learning-word-embedding-f90c3cec34ca)

<!--
- Artist examples
  - [Stranger Visions - Heather Dewey-Hagborg](https://deweyhagborg.com/projects/stranger-visions)
-->

#### Homework ####
- **Post** your homework in [Brightspace->Discussions->Reading Responses->Week 8](https://brightspace.nyu.edu/d2l/le/351324/discussions/topics/450525/View)
  - Reading response
  - Generated text
  - p5js sketch
- **Start** developing your Project 3 Sound / Text idea

## <a name="week9"></a>Week 9 - Sound / Text

### <a name="week9.1"></a>Week 9.1 Sound and Text

<!--
- Musical Interlude
  - [Bremer/McCoy - Højt At Flyve (audio)](https://www.youtube.com/watch?v=BKwkd8dzPF4)
  - [Bremer/McCoy interview / behind the scenes (YouTube)](https://www.youtube.com/watch?v=kF8Rxsw2eYk)
    - "The inspiration for the album comes from a lot of different places. It comes from all the music we listen to and also the life we are living."
-->

- Review GPT responses / sketches

Stephen Wolfram on ChatGPT
- [What Is ChatGPT Doing and Why Does It Work?](https://writings.stephenwolfram.com/2023/02/what-is-chatgpt-doing-and-why-does-it-work/) (2023)
- [ChatGPT Gets Its “Wolfram Superpowers”!](https://writings.stephenwolfram.com/2023/03/chatgpt-gets-its-wolfram-superpowers/) (2023)
  - ChatGPT is now able to access an extremely powerful calculator to do math
  - First of many plugins for ChatGPT
- [Can AI Solve Science?](https://writings.stephenwolfram.com/2024/03/can-ai-solve-science/) (2024)
  
<!--
More links
https://openai.com/blog/planning-for-agi-and-beyond
-->

- AI in the news
  - [Noam Chomsky: The False Promise of ChatGPT (NYT Opinions, 2023)](https://www.nytimes.com/2023/03/08/opinion/noam-chomsky-chatgpt-ai.html) (2023)
  - [Stephen Fry reads Nick Cave’s words about ChatGPT: 'We are fighting for the very soul of the world'](https://www.euronews.com/culture/2023/11/23/stephen-fry-reads-nick-caves-words-about-chatgpt-we-are-fighting-for-the-very-soul-of-the-) (2023)
  - [ChatGPT can now access the internet and run the code it writes](https://newatlas.com/technology/chatgpt-plugin-internet-access/)
  - [Beyond text: GPT has evolved, and AI is now flexing new powers](https://newatlas.com/technology/gpt-4-multimodal-ai/?itm_source=newatlas&itm_medium=article-body)
    - [Be My Eyes (Guardian)](https://www.theguardian.com/lifeandstyle/2019/jul/12/be-my-eyes-app-blind-people-helpers) - Volunteer human-based image to text

- Long Short-Term Memory Neural Networks (LSTM)
  - [Understanding LSTMs](https://colah.github.io/posts/2015-08-Understanding-LSTMs/)
- Transformers
  - [How transformers work](https://towardsdatascience.com/transformers-141e32e69591)
  - [Talk to transformer](https://app.inferkit.com/demo)

- Generative Pre-Trained Transformers (GPT)
  - [How transformers work](https://towardsdatascience.com/transformers-141e32e69591)
  - [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/)
    - Transformer model low level explanation
  - GPT-2 / 3 
    - [GPT explained - multiple difficulty levels](https://towardsdatascience.com/you-can-understand-gpt-3-with-these-youtube-videos-6a30887c928b)
  <!-- Old customized version - [GPT-2 Colab - train your own text](https://colab.research.google.com/drive/1uKXS6a9q5qrcU3UdSRpCjYnKHbC-N4pb?usp=sharing) -->
    - [GPT-2 Colab - train your own text (2021-10-26)](https://colab.research.google.com/drive/1E44LTs0eBUJ2BXz3xa64002qvYla7Tl2?usp=sharing)
  - ChatGPT
    - GPT-3.5 with additional training using reinforcement from human feedback
    - GPT-3.5 is best suited for text completions
      - How do we get it to answer our questions?
    - [Introducing ChatGPT (OpenAI blog)](https://openai.com/blog/chatgpt)
    - [How ChatGPT Works: The Model Behind The Bot (Medium)](https://towardsdatascience.com/how-chatgpt-works-the-models-behind-the-bot-1ce5fca96286)
    - [Aligning language models to follow instructions (OpenAI blog)](https://openai.com/research/instruction-following)
    - [Learning from human preferences
(OpenAI blog)](https://openai.com/research/learning-from-human-preferences)
      - reinforcement learning from human feedback (RLHF)
      - Does human feedback always lead to better results?
        - Biases / lack of knowledge of evaluators can become embedded
        - Reinforcement learning tries to optimize the reward
          - Easier for system to learn tricks / cheats rather than solving the general problem

- Why running machine learning models is hard
  - Training models requires huge resources
  - Need powerful GPU (parallel processing)
  - Large model size makes hosting difficult
    - Multi-gigabyte checkpoint files need to be loaded
  - SOTA (State of the Art) models are often too large to be run with consumer GPUs
  - Trend is for models to be hosted / closed source / closed data
    - Notable exception is Stable Diffusion
      - Open source
      - Open data
      - Optimized to run locally on reasonable hardware
  - Lab machines are available (Linux / nVidia 1080ti GPU)

- Suggested tools (2024):
  - GPT4 ([ChatGPT](https://chat.openai.com/), [Perplexity.ai](https://www.perplexity.ai/), Bing Copilot)
  - [ElevenLabs](https://elevenlabs.io/) - voice cloning
  - [Stable Audio](https://www.stableaudio.com/) - music generation
  - [MusicGen](https://replicate.com/meta/musicgen) - music generation
    - [MusicGen HuggingFace](https://huggingface.co/spaces/facebook/MusicGen)

- Machine learning techniques for sound
  - [Magenta](https://magenta.tensorflow.org/)
    - [MusicVAE: A tool for creating music with neural networks](https://medium.com/@wvsharber/musicvae-a-tool-for-creating-music-with-neural-networks-db0f4b84a698)
    - [Piano transcription](https://magenta.tensorflow.org/onsets-frames)
      - [Piano Scribe (In-browser using Magenta.js)](https://piano-scribe.glitch.me/)
    - [Magenta Demos](https://magenta.tensorflow.org/demos)
    - [Melody Mixer](https://experiments.withgoogle.com/ai/melody-mixer/view/)
    - [Magenta Studio lets you use AI tools for inspiration in Ableton Live](https://cdm.link/2019/02/magenta-studio-ai-ableton-live/)
    - [Performance RNN (Magenta)](https://magenta.tensorflow.org/performance-rnn)
      - An LSTM-based recurrent neural network designed to model polyphonic music with expressive timing and dynamics
      - Browser demos
    - [Piano Genie (Magenta)](https://magenta.tensorflow.org/pianogenie)
      - Maps simple button presses to 88 keys of piano using LSTM
      - [Piano Genie demo](http://piano-genie.glitch.me/)
  - [WaveNet A generative model for raw audio](https://deepmind.com/blog/article/wavenet-generative-model-raw-audio)
  - [Generating Audio Using Recurrent Neural Networks](https://apfalz.github.io/rnn/rnn_demo.html)
  - [SampleRNN examples](https://soundcloud.com/samplernn)
  - [SampleRRN code](https://github.com/Unisound/SampleRNN)
  - [Training notes for WaveNet and RNN](https://karlhiner.com/music_generation/wavenet_and_samplernn/)
  - [Technical: Architecture of Speech Recognition](http://slazebni.cs.illinois.edu/spring17/lec26_audio.pdf)
  - Audio deepfakes
    - [This is what a deepfake voice clone used in a failed fraud attempt sounds like](https://www.theverge.com/2020/7/27/21339898/deepfake-audio-voice-clone-scam-attempt-nisos)
    - [Resemble.ai - TTS (text to speech) and voice cloning](https://www.resemble.ai/)

  - [AudioLM](https://google-research.github.io/seanet/audiolm/examples/)
    - Does very good continuations of speech and music (apparently)
    - No trained model available


- Sound / Text Tools
  - [ml5.js Sound Classifier](https://learn.ml5js.org/#/reference/sound-classifier)
    - [ml5.js speech commands demo (p5js Web Editor)](https://editor.p5js.org/codingtrain/sketches/yjtv-rAxF)
    - [Train a custom sound classifier](https://teachablemachine.withgoogle.com/train/audio) model using [Teachable Machine](https://teachablemachine.withgoogle.com/)
    - [ml5.js: Sound Classification (The Coding Train / YouTube)](https://www.youtube.com/watch?v=cO4UP2dX944)
  - [AIVA - The Artificial Intelligence composing emotional soundtrack music](https://aiva.ai/)
  - [How to Build a Twitter Text-Generating AI Bot With GPT-2 (Max Woolf)](https://minimaxir.com/2020/01/twitter-gpt2-bot/)
  - [GPT-J-6B live demo](https://6b.eleuther.ai/)
    - [GPT-J-6B details](https://arankomatsuzaki.wordpress.com/2021/06/04/gpt-j/)
    - [Fun and Dystopia With AI-Based Code Generation Using GPT-J-6B (Max Woolf)](https://minimaxir.com/2021/06/gpt-j-6b/)
  - [Generating Piano Music with Transformer](https://magenta.tensorflow.org/piano-transformer)
  - [Lip Syncing Videos - Wav2Lip](http://cvit.iiit.ac.in/research/projects/cvit-projects/a-lip-sync-expert-is-all-you-need-for-speech-to-lip-generation-in-the-wild/)
    - [Wav2Lip interactive demo](https://bhaasha.iiit.ac.in/lipsync/)
    - [Wav2Lip Colab (ml4a)](https://colab.research.google.com/github/ml4a/ml4a/blob/master/examples/models/Wav2Lip.ipynb)

  - [AI generated death metal](https://www.sciencealert.com/new-24-7-ai-generated-death-metal-youtube-stream-is-giving-us-anxiety)
    - [Relentless Doppelgänger (YouTube) - generated by SampleRNN](https://www.youtube.com/watch?v=MwtVkPKx3RA)
    - [Death Metal Lofi (YouTube) - generated by OpenAI Jukebox
    - [DEATH DECLINE - Useless Sacrifice [Brutal Death Metal | Thrash Metal] (YouTube)](https://www.youtube.com/watch?v=IaJ2UHiTa0o) - human band! First result for "death metal" on YouTube

  - [OpenAI Jukebox](https://openai.com/blog/jukebox/)
    - [Jukebox Explorer](https://jukebox.openai.com/) pre-generated examples
    - [Command-line code](https://github.com/openai/jukebox/)
    - [OpenAI Jukebox - Mangtronix Edition](https://github.com/mangtronix/jukebox)
      - Downloadable version of OpenAI Jukebox with simpler usage with config files
      - Has example of generating a continuation of a song using first 5 seconds of audio, with artist, genre, and lyrics
    - [Jukebox Colab](https://colab.research.google.com/github/openai/jukebox/blob/master/jukebox/Interacting_with_Jukebox.ipynb) - only runs on Colab Pro
    - [Jukebox with audio priming, artist, genre, and lyrics (Colab)](https://colab.research.google.com/drive/1zk-FqAHHmytbSSyJp0pYx1L-UVT_ffNq?usp=sharing)

  - [Do Electric Songwriters Dream Of Human Muses?](https://www.stereogum.com/2084173/openai-jukebox-artificial-intelligence-songs/columns/sounding-board/)
  - ["openai jukebox" (Twitter)](https://twitter.com/search?q=openai%20jukebox&src=typed_query)
    - Do we see any *awesome* examples?
  - [Installing software on lab machines (Video)](https://brightspace.nyu.edu/d2l/le/lessons/110671/units/6064230)


#### Homework ####
- **Sign up** for Project 3 groups in the [Projects Spreadsheet](https://docs.google.com/spreadsheets/d/1_eyQ4XfzGKpqMIW7FatoDbHBJSAqyPfrkKcyCI66gbI/edit?usp=sharing)
- **Prepare** to share your project idea next class


### <a name="week9.2"></a>Week 9.2 - Present project ideas
- Present your project idea for feedback (5 minute presentation)
- ChatGPT continued
  - [Prompt Engineering (Open AI)](https://platform.openai.com/docs/guides/prompt-engineering/prompt-engineering)
- [Unleashing developer productivity with generative AI (McKinsey)](https://www.mckinsey.com/capabilities/mckinsey-digital/our-insights/unleashing-developer-productivity-with-generative-ai)


- Discuss the latest and greatest developments in machine learning / AI
  - Deepfakes
    - [Baltimore County principal’s racist comments faked by AI, experts say](https://www.thebaltimorebanner.com/education/k-12-schools/eric-eiswert-ai-deepfake-YUNO6ITYM5FWZPQAE24RIBV5CQ/)
    - [A UPenn student started a YouTube channel. In weeks, her face was stolen on China's social media. (Business Insider)](https://www.businessinsider.com/upenn-student-olga-loiek-youtube-china-social-media-stole-face-2024-3)
      - [Somebody Cloned Me in China... (YouTube)](https://youtu.be/3FQSFnZpsqw?si=4FGo893tqLHO5bgQ)
  - [A ChatGPT for Music Is Here. Inside Suno, the Startup Changing Everything (Rolling Stone, 2024](https://www.rollingstone.com/music/music-features/suno-ai-chatgpt-for-music-1234982307/)
  - [Sal Khan explains why GPT-4 is ready to be a tutor (2023)](https://www.axios.com/2023/04/07/sal-khan-chatgpt-gpt4-tutor)
  - [How AI Could Save (Not Destroy) Education | Sal Khan | TED (YouTube, 2023)](https://www.youtube.com/watch?v=hJP5GqnTrNo)
    - "We're going to give every student an AI tutor and every teacher an AI assistant"
   
  - [Open sourcing AudioCraft: Generative AI for audio (Meta)](https://ai.meta.com/blog/audiocraft-musicgen-audiogen-encodec-generative-ai-audio/)
  ![image](https://github.com/NYUAD-IM/artintel/assets/35246/f0835f6c-fdaa-4165-88f5-52e69fba25e8)


<!-- Outdated
- Work example
  - [These historical artefacts are totally faked
 (Wired UK)](https://www.wired.co.uk/article/fake-artefacts-ai)
  - [How Artificial Intelligence Sees Art History (The Met)](https://www.metmuseum.org/perspectives/articles/2019/2/artificial-intelligence-machine-learning-art-authorship)
-->

<!--
- **Read** [We read the paper that forced Timnit Gebru out of Google (Technology Review, 2020)](https://www.technologyreview.com/2020/12/04/1013294/google-ai-ethics-research-paper-forced-out-timnit-gebru/) and be prepared to discuss in class (no written response)
  
- **Read** [AI Image Generators Routinely Display Gender and Cultural Bias (Gizmodo)](https://gizmodo.com/ai-dall-e-stability-ai-stable-diffusion-1849728302) (no written response but post an image made using the tool below)
  - [Diffusion Bias Explorer
 (Huggingface Space)](https://huggingface.co/spaces/society-ethics/DiffusionBiasExplorer) Online tool for trying different prompt variations
  - **Post** an image pair that you feel reveals gender or cultural bias in one of the models. Why do you think the model gives that result?
-->

<!--
- **Read** [Why Timnit Gebru Isn’t Waiting for Big Tech to Fix AI's Problems (Time, 2022)](https://time.com/6132399/timnit-gebru-ai-google/)
- **Read** [‘Yeah, we’re spooked’: AI starting to have big real-world impact, says expert (The Guardian)](https://www.theguardian.com/technology/2021/oct/29/yeah-were-spooked-ai-starting-to-have-big-real-world-impact-says-expert)
  - No write up required, but let's have a lively discussion!
-->


<!--
- **Find** an artwork that deals with artificial intelligence / machine learning
  - **Post** a 3 paragraph response to the Brightspace discussion
  - What is your response to the artwork? What drew you to the piece?
  - How is the artist making use of artificial intelligence?
  - What is the concept, question, or statement of the piece? How does using AI support the concept?
  - Example list from [AI Artists](https://aiartists.org/ai-artist-founding-members)
    - [Wayne McGregor](https://aiartists.org/wayne-mcgregor) - generative dance gestures
    - [Sofia Crespo](https://aiartists.org/sofia-crespo) - Neural Zoo
    - [Memo Atken](https://aiartists.org/memo-akten) - Learning to See
    - [Mario Klingemann](https://aiartists.org/mario-klingemann) - Memories of Passersby I
-->

#### Homework
- *Finish* your Sound / Text / Code project
- *Submit* your project and documentation on the [Projects Spreadsheet](https://docs.google.com/spreadsheets/d/1_eyQ4XfzGKpqMIW7FatoDbHBJSAqyPfrkKcyCI66gbI/edit?usp=sharing)
- *Prepare* your in-class presentation

## <a name="week10"></a>Week 10

### <a name="week10.1"></a>Week 10.1 - AI Ethics / AI Artists
- Announcements
  - Eid breaaaaaaaaak Mon-Fri April 8-12
  - Legislative days to follow (Sunday April 21 and Sunday April 28)

- Project presentations

- Introduction to [Final Project](Projects.md)

- ml5js
  - [ml5js Getting Started](https://learn.ml5js.org/#/)
  - [Image Classifier Demo](https://editor.p5js.org/ml5/sketches/ImageClassification)
  - [ml5.js: Image Classification with MobileNet (YouTube)](https://www.youtube.com/watch?v=yNkAuWz5lnY)
  - [Local Server, Text Editor, JavaScript Console - p5.js Tutorial](https://www.youtube.com/watch?v=UCHzlUiDD10)
  - [PoseNet example using p5.js](https://editor.p5js.org/ml5/sketches/PoseNet_webcam)
  - [PoseNet dots (p5 Web Editor)](https://editor.p5js.org/mangtronix/sketches/olqXXWx4p)
  
- [AI Art: How artists are using and confronting machine learning (MoMA / YouTube)](https://youtu.be/G2XdZIC3AM8)
  
- Discuss social implications and ethics of AI and bias in Machine Learning

- AI in the news (2023)
  - [Pause Giant AI Experiments: An Open Letter](https://futureoflife.org/open-letter/pause-giant-ai-experiments/)
    - "We call on all AI labs to immediately pause for at least 6 months the training of AI systems more powerful than GPT-4."
governance principles" (self-stated)
  - [Statement from the listed authors of Stochastic Parrots on the “AI pause” letter](https://www.dair-institute.org/blog/letter-statement-March2023) - Timnit Gebru responds to Musk et al.
  - [Petition for Keeping Up the Progress Tempo on AI Research While Securing Its Transparency and Safety (LAION)](https://laion.ai/blog/petition/)
    - "Calling [an] international organization to transparently coordinate and progress on large-scale AI research and its safety"
    - "The recent proposition of decelerating AI research as a means to ensure safety and progress presents an understandable but untenable approach that will be detrimental to both objectives. Corporate or state actors will make advancements in the dark while simultaneously curtailing the public research community's ability to scrutinize the safety aspects of advanced AI systems thoroughly."
  - More background - AlphaGo (2019)
    - [Why DeepMind AlphaGo Zero is a game changer for AI research](https://hub.packtpub.com/deepmind-alphago-zero-game-changer-for-ai-research/)
    - AlphaGo Zero started with only the rules of Go and played millions of games against itself (in a few days), becoming the world's strongest Go player
  - (Time permitting) [
Computer-generated inclusivity: fashion turns to ‘diverse’ AI models (The Guardian)](https://www.theguardian.com/fashion/2023/apr/03/ai-virtual-models-fashion-brands)
- Discuss AI artworks
  
#### Homework
- **Read** [Asilomar AI Principles](https://futureoflife.org/open-letter/ai-principles/)
    - "one of the earliest and most influential sets of AI 
- **Watch** [A Beginner's Guide to Machine Learning with ml5.js](https://www.youtube.com/watch?v=jmznx0Q1fP0) (until 19:00, then it's just credits)
- **Read** [Hello ml5.js - A gentle introduction to ml5](https://learn.ml5js.org/#/tutorials/hello-ml5)



### <a name="week10.2"></a>Week 10.2 - Requested topics
- AI in the news (2023)
  - [Sparks of Artificial General Intelligence: Early experiments with GPT-4 (arXiv)](https://arxiv.org/abs/2303.12712)
  - [OpenAI's GPT-4: A Spark Of Intelligence! (Two Minute Papers / YouTube)](https://www.youtube.com/watch?v=wHiOKDlA8Ac)
  - [Presentation discussing examples from the paper (YouTube)](https://www.youtube.com/watch?v=qbIk7-JPB2c)
  
- [ChatGPT example prompts](https://prompts.chat/)
  - Making ChatGPT act in a certain role
  
- AI artists discussion
- Project check-in

<!--
- Lab machine access
  - Lab machine logins
  - Lab access
  - TeamViewer access
  - ssh access
  - Installing software
  - Running software
  - Transferring files
-->

<!--
- Autoencoders
  - [Autoencoder explained](https://youtu.be/9zKuYvjFFS8?t=56)
-->
  
#### Homework
- Work on your projects

## <a name="week11"></a>Week 11 - NO CLASS - Sound / Text Project Due

### <a name="week11.1"></a>Week 11.1 - NO CLASS (EID)
  
### <a name="week11.2"></a>Week 11.2 - NO CLASS (EID)
#### Homework (due before start of next class)



## <a name="week12"></a>Week 12 - Interactive Applications

### <a name="week12.1"></a>Week 12.1 Final Project Introduction / ml5js

- Announcements
  - IM End of Semester show
  
- Introduction to [Final Project](Projects.md)

- AI in the news (2020)
  - [Much ‘Artificial Intelligence’ Is Still People Behind a Screen](https://www.bloomberg.com/opinion/articles/2021-10-13/how-good-is-ai-much-artificial-intelligence-is-still-people-behind-a-screen)
- AI in the news (2023)
  - [Can GPT 4 Prompt Itself? MemoryGPT, AutoGPT, Jarvis, Claude-Next (AI Explained / YouTube)](https://www.youtube.com/watch?v=6NoTuqDAkfg)
  - [Someone Asked an Autonomous AI to 'Destroy Humanity': This Is What Happened (Vice)](https://www.vice.com/en/article/93kw7p/someone-asked-an-autonomous-ai-to-destroy-humanity-this-is-what-happened) - ChaosGPT


- ml5js
  - [ml5js Getting Started](https://learn.ml5js.org/#/)
  - [Image Classifier Demo](https://editor.p5js.org/ml5/sketches/ImageClassification)
  - [ml5.js: Image Classification with MobileNet (YouTube)](https://www.youtube.com/watch?v=yNkAuWz5lnY)
  - [Local Server, Text Editor, JavaScript Console - p5.js Tutorial](https://www.youtube.com/watch?v=UCHzlUiDD10)
  - [PoseNet example using p5.js](https://editor.p5js.org/ml5/sketches/PoseNet_webcam)
  - [PoseNet dots (p5 Web Editor)](https://editor.p5js.org/mangtronix/sketches/olqXXWx4p)


<!--
- [OpenAI API Access (has link to join waitlist)](https://beta.openai.com/)
- [Too big to deploy: How GPT-2 is breaking servers](https://towardsdatascience.com/too-big-to-deploy-how-gpt-2-is-breaking-production-63ab29f0897c)
-->

#### Homework (due before start of next class)
- **Create** An interactive ml5.js sketch (using the p5 editor or your own editor) that uses the webcam, uploaded image from the user, user-entered text, or other user interaction to do something interesting. You can start from one of the [ml5.js examples](https://editor.p5js.org/ml5/sketches) and modify it for your own use.
- **Write** a paragraph of text explaining your sketch
- **Post** the link to your sketch and description to the [Brightspace->Discussion](https://brightspace.nyu.edu/d2l/le/265669/discussions/topics/381012/View)
- **Sign up** for your Final Project group on the [Projects Spreadsheet](https://docs.google.com/spreadsheets/u/1/d/1_eyQ4XfzGKpqMIW7FatoDbHBJSAqyPfrkKcyCI66gbI/edit?usp=sharing)
- **Develop** the rough idea for your final project and add it your group description in the [Projects Spreadsheet](https://docs.google.com/spreadsheets/u/1/d/1_eyQ4XfzGKpqMIW7FatoDbHBJSAqyPfrkKcyCI66gbI/edit?usp=sharing)

### <a name="week12.2"></a>Week 12.2 - Interactive Systems
- Review project ideas

- Interactive systems
  - [p5.js / OpenAI Simple Example (p5 editor)](https://editor.p5js.org/mangtronix/sketches/XO533PMtA)
    - Chatbot completion using only client-side JavaScript
    - Requires an OpenAI API key that will be saved locally in your browser
  - [Latent Letters](https://github.com/NYUAD-IM/artintel/tree/master/LatentLetters)
    - Stable Diffusion / ComfyUI inside TouchDesigner
  - [p5js fullscreen](https://editor.p5js.org/mangtronix/sketches/t4G0erH1B)

- AI in the news
  - [Adobe Firefly product teaser](https://mashable.com/video/adobe-generative-ai-video) (2024)
    - Product demonstration of using generative video inside existing video editing tool
  - [Transcript: Ezra Klein Interviews Dario Amodei (NY Times](https://www.nytimes.com/2024/04/12/podcasts/transcript-ezra-klein-interviews-dario-amodei.html)
    - Interview with CEO of Anthropic
   
>[W]e’re going to have to make bigger models that use more compute per iteration. We’re going to have to run them for longer by feeding more data into them. And that number of chips times the amount of time that we run things on chips is essentially dollar value because these chips are — you rent them by the hour. That’s the most common model for it. And so, today’s models cost of order $100 million to train, plus or minus factor two or three. The models that are in training now and that will come out at various times later this year or early next year are closer in cost to $1 billion. So that’s already happening. And then I think in 2025 and 2026, we’ll get more towards $5 or $10 billion.


## <a name="week13"></a>Week 13 - ml5js / Final project


### <a name="week13.1"></a>Week 13.1 - Interactive Machine Learning
- More ml5js
  - [Image Classification with Teachable Machine, ml5.js and p5.js](https://nishanc.medium.com/image-classification-with-teachable-machine-ml5-js-and-p5-js-233fbdf48fe7)
  - [CharRNN (ml5js)](https://learn.ml5js.org/#/reference/charrnn)
    - [Training a charRNN and using the model in ml5js (GitHub)](https://github.com/ml5js/training-charRNN)
  - [ml5.js Serial](https://makeabilitylab.github.io/physcomp/communication/ml5js-serial.html)

- Chat bots
  - [Eliza](https://web.njit.edu/~ronkowit/eliza.html)
  - [Building an AI-based Chatbot in Python](https://blog.datasciencedojo.com/building-an-ai-based-chatbot-in-python/)
  - [I tricked GPT2 into working like a chatbot. (Reddit)](https://www.reddit.com/r/artificial/comments/cfgpvh/i_tricked_gpt2_into_working_like_a_chatbot_here/)
  - [Talk to Transformer](https://app.inferkit.com/demo)
  - [GPT-J-6B live demo](https://6b.eleuther.ai/)
  - [GPT-J 6B (huggingface)](https://huggingface.co/EleutherAI/gpt-j-6B)
  - [avatars4all](https://github.com/eyaler/avatars4all)
    - Live real-time avatars from your webcam in the browser (multiple Colabs)
  - [Use web camera in real-time on google colaboratory](https://github.com/a2kiti/webCamGoogleColab)
    - [Web Cam Demo Colab](https://colab.research.google.com/github/a2kiti/webCamGoogleColab/blob/master/webCamGoogleColab_callbackVersion.ipynb)

- Project feedback

- Work on final project

#### Homework ####
- **Work** on the idea for your final project

### <a name="week13.1"></a>Week 13.1 - Final Project Check-in / Work Session
- Final project check-in
- Final project work session


## <a name="week14"></a>Week 14

### <a name="week14.1"></a>Week 14.1 - Ethics + Future Applications / Final Project Check-in
- Ethics and future of machine learning / AI
  - [Two AIs talk about becoming human. (GPT-3) (YouTube)](https://youtu.be/jz78fSnBG0s)
  - [This Robot would let 5 People die | AI on Moral Questions | Sophia answers the Trolley Problem
 (YouTube)](https://www.youtube.com/watch?v=8MjIU4eq__A)
  - [Isaac Asimov's Three Laws of Robotics (Wikipedia)](https://en.wikipedia.org/wiki/Three_Laws_of_Robotics)
  - [A Robot That Harms: When Machines Make Life Or Death Decisions (NPR)](https://www.npr.org/sections/alltechconsidered/2016/08/29/490775247/a-robot-that-hurts-confronts-future-when-machines-make-life-death-decisions)
  - [Scientists Built an AI to Give Ethical Advice, But It Turned Out Super Racist (Futurism)](https://futurism.com/delphi-ai-ethics-racist)
  - [Ask Delphi (Allen Institue for AI)](https://delphi.allenai.org/)
- Final project check-in
- Final project work session
- IM Show signup
  - [A.rt I.ntel IM Show Projects (Spreadsheet)](https://docs.google.com/spreadsheets/d/1vjzsUmbCZBT_rYO6Hp5zAyONpEflRrew_XZhl4tPW8I/edit?usp=sharing)

### <a name="week14.2"></a>Week 14.2 - Final project work session
- IM End of Semester Show
- Sign up for Show and make equipment requests -> [AI - IM Show S2023](https://docs.google.com/spreadsheets/d/1vjzsUmbCZBT_rYO6Hp5zAyONpEflRrew_XZhl4tPW8I/edit?usp=sharing)
  - You can check out equipment now via [NYUAD Arts Booking (VPN required)](https://nyuad-artsbooking.nyu.edu/)
  - Special requests such as LCD monitors or large TVs will be considered across all classes
- Project check in
- Work session

#### Homework ####
- **Submit** your Final Project URL via Brightspace->Assignments->Final Project
- **Prepare** a **5 minute** presentation of your project


## <a name="week15"></a>Week 15

### <a name="week15.1"></a>Week 15.1 - Final project presentations
- **Final project due (must be submitted May 6 midnight)**
- Present Final Projects
  - Presentation of 5-7 minutes only! Share the best and most important results / reflection
  
### IM Show Setup - TBD - Arts Center Lobby
- Bring your project to the Arts Center Lobby
- Collect any equipment such as LCD monitor, TV
- Set up project and check working
- Can leave basic equipment, take laptops

### <a name="week15.2"></a>Week 15.2 - Course wrap-up / IM Show
- Course feedback
  - Please fill out A.rt I.ntel Course Feedback Questionnaire
- Goodbyes for now!

**IM Show - Thursday May 9 - 5-8pm in Arts Center lobby**
- All IM students need to attend and show a project
- Arrive 4:30pm (or as early as possible if in class), make sure project is setup and working
- Show our projects 5-7pm
- See great projects from your fellow students!
- Group photo 7:30pm
- Cleanup starts after group photo
  - All equipment back to IM Lab, checkin with Lab Assistant
