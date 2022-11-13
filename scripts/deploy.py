import os
import subprocess
from dotenv import dotenv_values

if __name__ == "__main__":
    env = dotenv_values(".env")
    env_vars_arg = ','.join([f'{k}="{v}"' for k,v in env.items()])
    os.system('docker compose build')
    os.system(f"""gcloud run deploy backend --source=$(pwd) --allow-unauthenticated --region=us-central1 --quiet""")
        # --update-env-vars={env_vars_arg} \
        # --region=us-central1 \
        # --zone=us-central1-a \