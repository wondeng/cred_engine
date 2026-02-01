# Credibility Engine

An AI system that:
- Collects tweets from key users
- Detects predictions
- Verifies them using Amazon Bedrock
- Tracks historical credibility

## Architecture
Twikit → Amazon Bedrock → S3 → SQLite

## Setup
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
