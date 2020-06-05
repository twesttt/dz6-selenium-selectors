#!/bin/bash

export DISPLAY=:20
Xvfb :20 -screen 0 1366x768x16 &
echo "-----Show directory-----"
pwd
ls
echo "----Start pytest----"
pytest
