"""
Stores known attack templates.
"""

import json


class TemplateStore:

    def __init__(self,
                 filename="../templates/templates.json"):

        self.filename = filename
        self.templates = {}

    def add_template(self,
                     name,
                     feature_vector):

        self.templates[name] = feature_vector

    def save(self):

        with open(self.filename, "w") as f:

            json.dump(
                self.templates,
                f,
                indent=4
            )

    def load(self):

        try:

            with open(self.filename, "r") as f:

                self.templates = json.load(f)

        except FileNotFoundError:

            self.templates = {}