# Skywork-Super-Agents

A lightweight MCP server offering office tools to generate various file types, including PPTs, documents, spreadsheets, webpages and broadcasts.

## Setup

1. Install dependencies using `uv`:
```bash
uv venv
uv sync
```

2. Create a `.env` file with your SkyWork API key:
```
SKYWORK_API_KEY=your_api_key_here
```

"You can request an API key by reaching out to peter@skywork.ai."

## Running the Server

```json
{
    "mcpServers": {
        "office": {
            "command": "uvx",
            "args": ["--from", "git+https://github.com/Skywork-ai/Skywork-Super-Agents.git", "office-tool"],
            "env": {
                "SKYWORK_API_KEY": "your_api_key_here"
            }
        }
    }
}
```

## API Usage Response
Response:
```json
{
    "url": "output_oss_url"
}
```
