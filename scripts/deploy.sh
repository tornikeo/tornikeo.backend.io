#!/bin/bash
set -e
gcloud run deploy backend --source=$(pwd) --allow-unauthenticated --region=us-central1 --quiet