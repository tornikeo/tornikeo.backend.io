import os
import subprocess
from dotenv import load_dotenv

if __name__ == "__main__":
    load_dotenv(".env")
    subprocess.run(
        f"""gcloud run deploy backend --source=$(pwd) --allow-unauthenticated \
        --update-secrets=
        --region=us-central1 \
        --quiet""")