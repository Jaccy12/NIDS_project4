"""
template_store.py

Stores and manages attack templates for DTW matching.
"""

import json
import os


class TemplateStore:

    def __init__(self, filename=None):
        """
        Initialize template storage with safe path handling.
        """

        base_dir = os.path.dirname(__file__)

        if filename is None:
            self.filename = os.path.join(
                base_dir, "..", "templates", "templates.json"
            )
        else:
            self.filename = filename

        self.templates = {}

    # ==========================================================
    # ADD TEMPLATE (FIXED: STORE SEQUENCES)
    # ==========================================================

    def add_template(self, name, feature_vector):
        """
        Add feature vector to a template sequence.
        """

        if name not in self.templates:
            self.templates[name] = []

        self.templates[name].append(feature_vector)

    # ==========================================================
    # SAVE
    # ==========================================================

    def save(self):
        """
        Save templates to JSON file.
        """

        # Ensure directory exists
        os.makedirs(os.path.dirname(self.filename), exist_ok=True)

        with open(self.filename, "w") as f:
            json.dump(self.templates, f, indent=4)

        print("Templates saved successfully.")

    # ==========================================================
    # LOAD
    # ==========================================================

    def load(self):
        """
        Load templates from file.
        """

        try:
            with open(self.filename, "r") as f:
                self.templates = json.load(f)

        except FileNotFoundError:
            self.templates = {}