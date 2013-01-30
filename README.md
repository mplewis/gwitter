Usage
=====
````
usage: gwitter.py [-h] [-l GITHUB_USERNAME] [-n REQUESTS] user

Print a GitHub user's commit message history.

positional arguments:
  user                  the user whose commit history you want to search

optional arguments:
  -h, --help            show this help message and exit
  -l GITHUB_USERNAME, --login GITHUB_USERNAME
                        authenticate to GitHub as GITHUB_USERNAME for up to
                        5000 API requests per hour
  -n REQUESTS, --num-reqs REQUESTS
                        the number of event bundles to read (defaults to 10):
                        if this is set too high, you'll run out of API
                        requests
````

Try it out right now!
=====================

Clone the repo, then try out `python gwitter.py mplewis` to check out my commit history. It's that easy.