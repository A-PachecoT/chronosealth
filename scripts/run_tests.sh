#!/bin/bash
set -e

echo "Running tests..."

# Change to the project root directory
cd "$(dirname "$0")/.."

# Run all tests
python -m unittest discover tests

echo "All tests completed successfully!"