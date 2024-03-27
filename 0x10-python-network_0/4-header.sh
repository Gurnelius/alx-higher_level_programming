#!/bin/bash
# Send GET request with custom header and display response body
curl -sSL -H "X-School-User-Id: 98" "$1"
