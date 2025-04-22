#!/bin/bash
echo "🔍 Running Unit, Integration, and System Tests..."
pytest tests/ --disable-warnings -v
