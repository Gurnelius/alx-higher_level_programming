#!/bin/bash
# Send request to URL and display only status code
curl -s -o /dev/null -w "%{http_code}" "$1"
