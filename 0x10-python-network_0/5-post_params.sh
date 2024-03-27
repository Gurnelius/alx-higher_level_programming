#!/bin/bash
# Send POST request with variables email and subject, display response body
curl -sSL -d "email=test@gmail.com&subject=I%20will%20always%20be%20here%20for%20PLD" "$1"
