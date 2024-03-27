#!/bin/bash
# send a request to URL and get size of the body
curl -sL "$1" | wc -c
