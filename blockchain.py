#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 21:37:19 2022

@author: sujith
"""

import datetime
import hashlib
import json
from flask import Flask, jsonify


class Blockchain:

    def __init__(self):
        self.chain = []
        self.create_block(proof=1, previous_hash="0")
