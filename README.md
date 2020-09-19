# Pod Bot

Discord Bot that adds Pods to the Fellowship Server

## Setup

```
virtualenv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp example.env > .env
```

Fill out `.env` with your token.

## Usage

The bot does 2 things:

1. Creates Pod category based on command
2. Creates Pod category based on file

### Running

To run the bot in the background

```
python -m pod --file <file>
```