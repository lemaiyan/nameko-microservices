#!/usr/bin/env bash

echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
echo  "     Start Trek Service         "
echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

# Run service

nameko run --config config.yml services.http