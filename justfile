# Project Justfile utility

# Print list of available recipe (this)
default:
    @just --list --unsorted

# Setup Python dependencies
setup:
    poetry install
    poetry shell

python *ARGS:
    poetry run python {{ ARGS }}
