
<a name="readme-top"></a>

<div align="center">

<!-- [![Contributors][contributors-shield]][contributors-url] -->
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

</div>
<!-- [![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url] -->



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/dr413677671/PromptGallery-stable-diffusion-webui">
    <img src="images/logo.png" alt="Logo" width="206.25" height="131.25">
  </a>

  <h3 align="center">Prompt Gallery</h3>
  <p align="center">
    A prompt cookbook worked as <a href="https://github.com/AUTOMATIC1111/stable-diffusion-webui">stable-diffusion-webui</a> extenstions.
    <br />
    <a href="https://www.youtube.com/watch?v=9U6-moIJUkk"><strong>Watch Demo »</strong></a>
    <br />
    <br />
    <a href="https://github.com/dr413677671/PromptGallery-stable-diffusion-webui/README.md">Explore the docs</a>
    ·
    <a href="https://github.com/dr413677671/PromptGallery-stable-diffusion-webui/issues">Report Bug</a>
    ·
    <a href="https://github.com/dr413677671/PromptGallery-stable-diffusion-webui/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#Prerequisites-&-Installation">Prerequisites&Installation</a></li>
      </ul>
    </li>
    <li>
      <a href="#usage">Usage</a>
      <ul>
        <li><a href="#build-library">Build Library</a></li>
        <li><a href="#start-stable-diffusion-webui">Start stable-diffusion-webui</a></li>
        <li><a href="#build-library">Build Library</a></li>
        <li><a href="#start-prompt-gallery">Start Prompt Gallery</a></li>
        <li><a href="#populate-previews-and-qc">Populate previews </a></li>
        <li><a href="#populate-previews-and-qc">Quality Contorl</a></li>
      </ul>
    </li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->

<div align=center>
<img src='./images/front.JPG'>
</div>

## About The Project

> Please star the repo if you likes it :>

> 🐘 Good news: the extension now support webui dark theme.

Prompt Gallery works as a prompt-set library extension of [stable-diffusion-webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui). Stable-diffusion is an AI model which can generate illustration based on text-based prompts

The extension combined with four features:
1. prompt-set library management
2. preview pictures management
3. select a combination of prompt-sets and generate illustration in webui
4. avatar/character system


<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started


### Prerequisites & Installation
 
1. Install [stable-diffusion-webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui)

2. Edit webui-user.bat (Win) or webui-user.sh (Linux) with these arguments "--api --listen --cors-allow-origins http://localhost:5173"

>> ![install](./images/0-1.JPG)


3. Start webui

4. Install Prompt-gallery extension in Web-UI

>> 4.1 Inout https://github.com/dr413677671/PromptGallery-stable-diffusion-webui.git in "URL for extension's git repository"

>> 4.2 Input "Prompt Gallery" in Local directory name

 >> ![install](./images/install.JPG)


Please refer to section <a href="###Customized extension ip and port (optional)">Customized extension ip and port (optional)</a> if you are using customized webui ip/port.


## Usage

Restart webui. You should see a initial frontpage like this.

![preset](./images/0-0.png)

There is no preview pictures. Prompt Gallery works like a framework. You need to create your own prompt-set library folloting by two steps:
1. edit your prompt-set dictionary
2. generate preview pictures for prompt-sets

Please follow the instructions below to build your own prompt-set library: Alternatively you could watch the video tutorial:
<a href="https://www.youtube.com/watch?v=9U6-moIJUkk">View Demo</a>


### Build prompt-set library

Definition of avatars.yaml:

| value | negative | param |
| :-----| ----: | :----: |
| Positive prompts | Negative prompts | Other params for webui image generation |

#### Build Avatar library

> Avatars is the charater displayed on the top of the extension. Defined your own character by editing <stable-diffusion-webui-path>/extensions/your-prompt-gallery-extension-name/assets/avatars.yaml

> The field "value" is the prompt-set for each characters.

Teamplate: 
   ```yaml
    whiteHair: 
      value: "1 girl,  blush, White hair, Red eyes, animal ears,  looking at viewer, gothic lolita, dramatic angle, very beautiful, beautiful eyes, "
      negative: ""
    pinkGirl: 
      value: "petite, 1girl, solo, pink hair, very long hair, school uniform, happy,outdoors, flower field, excited"
   ```

#### Build prompt-set library

> Prompt-sets are prompts displayed as cart boxes below. 

> Customized your own prompt-set by editing <stable-diffusion-webui-path>/extensions/your-prompt-gallery-extension-name/assets/tags.yaml

```yaml
    category-tier-1:
      category-tier-1-1:
        "prompt-set-name-1":
          value: "prompt1, prompt2"
          negative: "neg-prompt1, neg-prompt2"
        "prompt-set-name-2"
          value: "prompt1"
          negative: "neg-prompt1"
      category-tier-1-2:
        "prompt-set-name-3":
          value: "prompts"
```


> The prompt-set are managed hierarchyly (e.g. the config below defined a tier 1 category "Figure" containes two tier two categories "Hair" and "Face")

   ```yaml
    Figure:
      Hair:
        "ponny-tail":
          value: "ponny-tail"
          negative: "lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, "
        "short_hair"
          value: "short_hair"
          negative: "long_hair，lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, "
      Face:
        "smile":
          value: "smile"

    Background:
      '':
        simple background:
          value: simple background
        sunburst background:
          value: sunburst background
      Nature:
        Space:
          value: "space background, space,"
        Startrails:
          value: colorful startrails
        Woods:
          value: "Woods background, fantacy background,"
   ```

> Additionally you could edit field "param" to customized AI model parameters (or switch models using the webui model selection tab.):

   ```yaml
    Style:
      General Effect:
        "General_ice_high_res":
          value: "flowing ice, portrait, focus on face, complex, extremely detailed , elegant, CG, (an extremely delicate and beautiful girl), incredibly absurdres, best quality,concept art"
          negative: "lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, "
          param: "Steps: 30, Sampler: Euler, CFG scale: 11.5, Seed: 1058629707, Size: 512x768, Variation seed: 1692844643, Variation seed strength: 0.27, Seed resize from: 1088x512"
    Background:
      '':
        simple background:
          value: simple background
        sunburst background:
          value: sunburst background
      Nature:
        Space:
          value: "space background, space,"
        Startrails:
          value: colorful startrails
   ```

> Useful links for anime prompts:
>> [sd-danbooru-tags](https://github.com/Vetchems/sd-danbooru-tags) or [DeepDanbooru](https://github.com/KichangKim/DeepDanbooru).


### Using Prompt Gallery

1. Slect tab "Prompt Gallery" on top navigation bar. You should see your dined prompt-sets in prompt-gallery.

2. Select the avatar (model for demo)

3. Select multiple prompt-sets 
 
4. Click "send WebUI"

  ![2-1](./images/2-1.JPG)

5. In a few minutes, Images geneated with teh selected prompt-sets will be downloaded in your browser

  ![2-2](./images/2-2.JPG)

6. The preview picture is missing. To add preview picture for each prompt-set, please refer to the next section.

### Populate previews and QC

1. For newly installed exteantion, there will be no preview pictures for each prompt-set.

  ![3-1](./images/3-1.JPG)

2. Goto tab "txt2img" in webui and Select "Prompt Gallery" in "scripts"

  ![3-2](./images/3-2.JPG)

3. Upload the avatar yaml library mentioned in section "Build Avatar library".

  ![3-3](./images/3-3.JPG)

4. Add default prompts or default negative (optional), default prompts are additional prompts that applied for each prompt-set preview picture generation

5. Select "skip exists" if you wish to skip generating preview if preview picture exists for a prompt-set

  ![3-4](./images/3-4.JPG)

6. Wait for stable-diffusion-webui generate previews automatically.

  ![3-5](./images/3-5.JPG)

7. Pick the best image for preview picture of each prompt-set.

  ![3-6](./images/3-6.JPG)

8. Reflesh the browser. You should see the preview pictures in Prompt Gallery.

  ![3-7](./images/3-7.JPG)

9. The preview pictures are stored in prompt-gallery-directory/assets/preview/. You could always inspect the pictures manually.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


### Cutomize default image generation parameters

Sometimes you need to defined the default values for the AI model parameters.

1. Change the params  at the top of webui-directory/extension/prompt-gallery-extension-name/paste_this_to_webui_scripts_folder/prompt_gallery.py


```python
BATCH_SIZE = 4
N_ITER = 2
STEPS = 30
CFG_SCALE = 11.5
WIDTH = 512
HEIGHT = 768
SAMPLER_INDEX = 1
RESTORE_FACE = 'true'
TILING = 'false'
DO_NOT_SAVE_GRID = 'false'
```

### Customized extension ip and port (optional)

If you are using customized ip for webui and the extension fail to automatically detected your customized ip. Please try:

1. Search %extension-path%\assets\index.*.js, change "127.0.0.1" to your customized webui ip

2. Search %extension-path%\scripts\prompt_gallery.py change 

```python
pg_ip = "%your_webui_ip%" if shared.cmd_opts.listen else 'localhost'
pg_port = %your_webui_port%--
```
3. Change the ip address in webui-user.bat (Win) or webui-user.sh (Linux)

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.


<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

* [![Vue][Vue.js]][Vue-url]
* [![JavaScript][JSP]][JSP-url]
* Gradio
* [![Pytorch][Pytorch]][Pytorch-url]
* [![React][fastapi-img]][fastapi-url]

<!-- CONTACT -->
## Talk with me

* dr413677671 - [@zhihu-Calcifer](https://www.zhihu.com/people/kumonoue) - 413677671@qq.com
* Project Link: [https://github.com/dr413677671/PromptGallery-stable-diffusion-webui](https://github.com/dr413677671/PromptGallery-stable-diffusion-webui)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments
* [stable-diffusion-webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui)
* [novelai-tag](https://github.com/blacktunes/novelai-tag)
* [Gradio](https://github.com/gradio-app/gradio)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/dr413677671/PromptGallery-stable-diffusion-webui.svg?style=for-the-badge
[contributors-url]: https://github.com/dr413677671/PromptGallery-stable-diffusion-webui/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/dr413677671/PromptGallery-stable-diffusion-webui.svg?style=for-the-badge
[forks-url]: https://github.com/dr413677671/PromptGallery-stable-diffusion-webui/network/members
[stars-shield]: https://img.shields.io/github/stars/dr413677671/PromptGallery-stable-diffusion-webui.svg?style=for-the-badge
[stars-url]: https://github.com/dr413677671/PromptGallery-stable-diffusion-webui/stargazers
[issues-shield]: https://img.shields.io/github/issues/dr413677671/PromptGallery-stable-diffusion-webui.svg?style=for-the-badge
[issues-url]: https://github.com/dr413677671/PromptGallery-stable-diffusion-webui/issues

[product-screenshot]: images/screenshot.png
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[JSP]: https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E
[JSP-url]: https://github.com/TheAlgorithms/JavaScript
[python-img]: https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue
[python-url]: https://www.python.org/
[fastapi-img]: https://img.shields.io/badge/fastapi-109989?style=for-the-badge&logo=FASTAPI&logoColor=white
[fastapi-url]: https://fastapi.tiangolo.com/
[Pytorch]: https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=PyTorch&logoColor=white
[Pytorch-url]: https://github.com/pytorch/pytorch
