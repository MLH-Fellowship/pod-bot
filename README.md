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

1. Creates Pod category and role based on command
2. Creates Pod category and role based on file

### Running

To run the bot in the background, for using the command:

```
python -m pod
```

or to use a file

```
python -m pod --file <file_path>
```

File format:

```
Pod 1.0.1
Pod 1.1.1
Pod 1.0.2
Pod 1.1.2
```