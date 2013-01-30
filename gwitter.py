import argparse
import re
from getpass import getpass
from github import Github

parser = argparse.ArgumentParser(description="Print a GitHub user's commit"
    " message history.")
parser.add_argument('user', help='the user whose commit history you want to'
                                 ' search')
parser.add_argument('-l', '--login', metavar='GITHUB_USERNAME',
    help='authenticate to GitHub as GITHUB_USERNAME for up to 5000 API requests'
         ' per hour')
parser.add_argument('-n', '--num-reqs', metavar='REQUESTS', default=10,
    type=int, help='the number of event bundles to read (defaults to 10): if'
                   ' this is set too high, you\'ll run out of API requests')

args = parser.parse_args()

USER_TO_INSPECT = args.user
EVENT_BUNDLES_TO_READ = args.num_reqs

if args.login != None:
    GITHUB_USERNAME = args.login
    GITHUB_PASSWORD = getpass('GitHub password for ' + GITHUB_USERNAME +': ')
    gh = Github(GITHUB_USERNAME, GITHUB_PASSWORD)
else:
    gh = Github()

user = gh.get_user(USER_TO_INSPECT)
public_events = user.get_public_events()

commit_messages = []
for event_bundle in public_events[0:(EVENT_BUNDLES_TO_READ-1)]:
    payload = event_bundle.payload
    if 'commits' in payload:
        commits = payload['commits']
        for commit in commits:
            if 'message' in commit:
                raw_text = commit['message']
                clean_text = ' '.join(raw_text.split())
                commit_messages.append(clean_text)

print 'Last commit messages from ' + USER_TO_INSPECT + ':'
for message in commit_messages:
    print '    "' + message + '"'

REQUESTS_REMAINING, REQUSTS_TOTAL = gh.rate_limiting
if GITHUB_USERNAME != None:
    PRETTY_USERNAME = GITHUB_USERNAME
else:
    PRETTY_USERNAME = 'anonymous'
print (str(REQUESTS_REMAINING) + ' of ' + str(REQUSTS_TOTAL) + 
    ' API requests remaining for user ' + PRETTY_USERNAME + '.')