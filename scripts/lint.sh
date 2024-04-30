#!/usr/bin/env bash

set -e
set -x

mypy readyapi
ruff readyapi tests docs_src scripts
ruff format readyapi tests --check
