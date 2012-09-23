"""
" * ShakyText.py
" * Copyright (C) 2009 Joshua Skelton
" *                    joshua.skelton@gmail.com
" *
" * This program is free software; you can redistribute it and/or
" * modify it as you see fit.
" *
" * This program is distributed in the hope that it will be useful,
" * but WITHOUT ANY WARRANTY; without even the implied warranty of
" * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
"""

import wrapper
import random

class ShakyText(wrapper.Wrapper):
    def __init__(self, internal):
        wrapper.Wrapper.__init__(self, internal)
        self.scale = 0.1
        
        random.seed()
        
    def update(self, time = 16):
        self.internal.update(time)
        self.charList = self.internal.charList
        
        for (_, rect) in self.charList:
            rect.top += rect.height * random.random() * self.scale
            rect.left += rect.width * random.random() * self.scale