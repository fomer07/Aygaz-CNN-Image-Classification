# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.16.5
#   kernelspec:
#     display_name: Python 3
#     name: python3
# ---

# + [markdown] id="wgmEV3UYwrEG"
# Google Colab already comes pre-installed with many libraries, but let's double-check. Use --upgrade to ensure you’re running the latest versions of these packages.

# + id="eI54XaaNwbDq"
# Core libraries
# !pip install --upgrade tensorflow keras matplotlib pandas numpy scikit-learn opencv-python

# + [markdown] id="H6pXqZu2w0D5"
# Here to work directly with GitHub repo in Colab, we are cloning it.

# + id="H12h2H4fw0tJ"
from google.colab import drive
drive.mount('/content/drive')  # Mount Google Drive

# !git clone https://github.com/fomer07/Aygaz-CNN-Image-Classification.git

# + [markdown] id="tSOlGjYI7YlI"
# Environment Logging: Track the library versions used for reproducibility:

# + id="NEdb4XRb7ZIj"
# !pip freeze > requirements.txt

# + [markdown] id="wQMoByRX7db0"
# This generates a **requirements.txt** file, which can be useful for newcomers.

# + id="Bw3FgAbQ7bGl"
# !pip install jupytext

# + id="LxwR-9qC7hol"
# !jupytext --set-formats ipynb,py /content/drive/MyDrive/Colab\ Notebooks/Aygaz-CNN-Image-Classification/01_Environment_Setup.ipynb


# + id="2mhKJ4j77rtW"

