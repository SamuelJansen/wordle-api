from flask import render_template
from python_framework import ResourceManager
import ModelAssociation


app = ResourceManager.initialize(__name__, ModelAssociation.MODEL)
