import os 
from getpass import getpass

username = "mateusoliv-felipe"
os.environ["GITHUB_USER"] = username

usermail = getpass()
os.environ["GITHUB_MAIL"] = usermail

usertoken = getpass()
os.environ["GITHUB_TOKEN"] = usertoken