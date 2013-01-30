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