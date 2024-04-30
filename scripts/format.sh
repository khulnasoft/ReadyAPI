#!/bin/sh -e
set -x

ruff readyapi tests docs_src scripts --fix
ruff format readyapi tests docs_src scripts
