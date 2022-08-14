#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 03:42:07 2022

@author: jajayu
"""

import matplotlib.pyplot as plt
from wordcloud import WordCloud
from PIL import Image
import numpy as np

f = open('eduheadlines.txt','r', encoding='utf-8').read()
mask = np.array(Image.open('star.jpg'))
wordcloud = WordCloud(background_color="white",
                      width=1000, height=860, 
                      margin=2, font_path="simhei.ttf", 
                      mask=mask).generate(f)
plt.figure(figsize=(10,10))
plt.imshow(wordcloud)
plt.axis("off")
plt.savefig('demo00.png')
plt.show()