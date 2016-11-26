#!/usr/bin/env python
# -*- coding: utf-8 -*-

from requests.packages.urllib3.exceptions import InsecureRequestWarning
import requests
import sys


if len(sys.argv) != 3:
    print "fake_user_agent.py <url> <content-lenght>"
    sys.exit(1)

# Disable warning for SSL insecure/invalid certificates
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


url = sys.argv[1]
expected_cl = int(sys.argv[2])
f = open("user_agents.txt", "r")
responses = []
for ua in f:
    ua = ua.strip()
    headers = {'User-Agent': ua}
    response = requests.get(url, headers=headers, verify=False)
    content_length = response.headers['Content-Length']

    responses.append((ua, content_length))
    if int(content_length) != expected_cl:
        print "User-Agent: {0} [{1} bytes]".format(ua, content_length)
f.close()
