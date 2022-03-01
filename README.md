# Trash Tag
## Climate Change
## Click! Upload! Classify ! Educate!
[![License](https://img.shields.io/badge/License-Apache2-blue.svg)](https://www.apache.org/licenses/LICENSE-2.0)

## Contents

## What's the problem?

 As per UN Material Footprint increased 70% from 2000 to 2017, Currently Urban households and businesses produce lot of substantial amounts of solid waste which affects many ecosystems and species. 

## What it does

Sustainable solid waste management is essential. This implies waste reduction, reuse, recycling and composting, incineration, and disposal in landfills. Waste reduction, recycling, reuse and composting are preferred methods and should be promoted, as they reduce demand on scarce environmental resources, decrease energy use, and minimize the quantity of waste that must eventually be incinerated or disposed of in landfills.

The objective of the TrashTag is based on Sustainable Consumption and Production patterns(SDG Goal) It is computer vision makes a classification model of Solid waste generation based on photos of glass, paper, cardboard, plastic, plastic bags, metal, and trash. A convolution neural network framework is used classify photos of waste generation and also to outputs the proportion of each garbage type that was classified.

## How we built it

Solid Waste(Trash) Generation Classification using Deep Learning:

Sustainable solid waste management is essential. This implies waste reduction, reuse, recycling and composting, incineration, and disposal in landfills. Waste reduction, recycling, reuse and composting are preferred methods and should be promoted, as they reduce demand on scarce environmental resources, decrease energy use, and minimize the quantity of waste that must eventually be incinerated or disposed of in landfills.

Deep Learning Classification model of waste generation based on photos of glass, paper, cardboard, plastic, plasticbags, metal, and trash. A convolutional neural network framework is used classify photos of waste generation and also to outputs the proportion of each garbage type that was classified.

## Key Components:

### Habana® Gaudi® processor
The Habana® Gaudi® processor is designed to maximize training throughput and efficiency, while providing developers with optimized software and tools that scale to many workloads and systems. Habana Gaudi software was developed with the end-user in mind, providing versatility and ease of programming to address the unique needs of users’ proprietary models, while allowing for a simple and seamless transition of their existing models over to Gaudi.

### Data Augmentation
Data Augmentation is a practice that is commonly used in image classification that enlarges the existing image dataset by creating new data sets from the existing data. This augmentation is most commonly seen in operations like shifting the image, mirroring the image horizontally or vertically, zooming in on the image, and so on. These augmentations then create new images and thus enhance the number of images to train on.

### Convolutional Neural Network (CNN)
A convolutional neural network (CNN) is a popular model for image classification. CNNs distinguish characteristics of an image by looping through the pixel values in an image and calculating the dot product of a those pixels with a filter kernel matrix. These kernel matrices accentuate different aspects of the image such as vertical and horizontal lines, curvature, etc. For more information on CNNs, see APMonitor - Computer Vision with Deep Learning.

## Challenges we ran into

Regrettably though, for the sake of time + complexity constraints,  classifying the entire image is faster. the model is good to classify  the garbage type, but still need to improve to have better proportions of each garbage type of the true classification.However, percentage classification is more computationally expensive.That was one challenge.

The other major challenge was collecting datasets of different garbage types. 

## Accomplishments that we're proud of

So, we really do feel proud that we were able to pull it off. Getting familiar with AWS Services(AWS Cloud services, Amazon EC2 instances, Habana Gaudi), frequently deploying and testing to get the hang of it, collecting information, and altogether making things work as a team. We're really proud of that.

## What we learned
It is apt to say that the process, alone, of building a project, whatever it is, holds new knowledge and skills to achieve. We did a lot of that: unlocking new knowledge and skills. This includes:

Setting up with Amazon EC2
Launching DL1 instances using Habana DLAMI
Training and Testing Model in Habana Gaudi
deploying as well as managing config across apps (almost like in a microservice environment)
collecting and cleaning crowd-sourced data

## Project roadmap
The product is only in like v0.0.1. There is so much left to do. We would improve the model, adding large dateset(Satellite Images, Marine Debris, Forest Debris) for achieving Sustainable Consumption and Production patterns and Substanstially Reduce waste generation to save environment for future generations.

All these things and more will go into improving the app.

## Demo video

[![Watch the video](./images/preview_image.jpg)](https://www.youtube.com/watch?v=ps6iUlIUpgw)


## Getting started

## Setup

This code works on Python3+ versions.

## Clone the repository

## With Docker:

$ git clone https://github.com/zero-hunger-cfc-2k21/DHAAN-Plant-Disease-Prediction-Model.git 

$ TrashTag/

## Without Docker:

## Install the required libraries

$ pip3 install -r requirements.txt

## Clone the repository

$ git clone https://github.com/TrashTag-ClimateChange/TrashTag.git

$ TrashTag/

## Run app.py

$ python3 app.py 

or

$ python -m flask run

In Browser run with 127.0.0.1:5000

## Live Demo Url:

https://app-c1.a3bnbtend2e.jp-tok.codeengine.appdomain.cloud/


## Built with

- [IBM Cloud](https://cloud.ibm.com/) - Hosted in IBM Cloud
- [IBM Code Engine](https://cloud.ibm.com/login?redirect=%2Fcodeengine%2Flanding) - Deployment platform
- [IBM Text to Speech](https://cloud.ibm.com/catalog/services/text-to-speech) - For converting results into speech audio in regional languages
- [IBM Language Translator](https://cloud.ibm.com/catalog/services/language-translator) - For converting results from English to regional languages
- [Figma](www.figma.com) - For UI design
- [Keras Framework](https://keras.io) - For AI/ML modelling
- [Densenet121](https://keras.io/api/applications/densenet/) - For prediction
- Trained Model Url : https://drive.google.com/file/d/1WF8kWRRYEUt3zxgRUBJdY93P4KWlfCC2/view?usp=sharing

## Authors
- **Jinka Baji** - Product Lead
- **Suneetha Jonadula** - _Lead Developer_

## License

This project is licensed under the Apache 2 License - see the [LICENSE](LICENSE) file for details.

## References

https://aws.amazon.com/ec2/getting-started/
https://docs.aws.amazon.com/dlami/latest/devguide/tutorial-habana-launching.html
https://developer.habana.ai/category/tutorials/
