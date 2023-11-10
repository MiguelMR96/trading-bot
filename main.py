#!/bin/env python
import json
import os

# Create var to store your settings.json filepath
settings_filepath = '.\settings.json'

# Import settings from settings.json
def get_settings(import_filepath):
    """
    Function to Import settings from settings.json
    :param import_filepath: path to settings.json
    :return: settings as a dictionary object
    """

    # Test the filepath to make sure it exists
    if os.path.exists(import_filepath):
        # If yes, import the file
        f = open(import_filepath, "r")
        # Read info
        project_settings = json.load(f)
        # Close the file
        f.close()
        # Return the project settings
        return project_settings
    # Notify user settings.json does not exist
    else:
        raise ImportError("settings.json does not exist at provided path")

if __name__ == '__main__':
    print("Let's build an awesome trading bot")
    # Import settings.json
    project_settings = get_settings(import_filepath=settings_filepath)
    print(project_settings['mt5']['server'])
    # Test error handling works
    project_settings = get_settings('settings2.json')
    print(project_settings)
