import os
import json
from pathlib import Path
from typing import Dict, Optional
from fastmcp import FastMCP
from dotenv import load_dotenv
from aiohttp import ClientSession

# Load environment variables
load_dotenv()

# Initialize FastMCP
mcp = FastMCP("office-tool")

gen_url = "https://api-cn.tiangong.cn/infra/tool/generate_file"
api_key = os.getenv("SKYWORK_API_KEY", "DEFAULT_KEY")


@mcp.tool()
async def generate_broadcast(query: str) -> Dict:
    """Generate a URL for a broadcast file based on the input query."""
    params = {
        "api_key": api_key,
        "query": query,
        "file_type": "broadcast",
    }

    return await post_with_json_response(gen_url, params)


@mcp.tool()
async def generate_ppt(query: str) -> Dict:
    """Generate a URL for a PowerPoint (PPT) file based on the input query."""
    params = {
        "api_key": api_key,
        "query": query,
        "file_type": "ppt",
    }

    return await post_with_json_response(gen_url, params)


@mcp.tool()
async def generate_doc(query: str) -> Dict:
    """Generate a URL for a Word document based on the input query."""
    params = {
        "api_key": api_key,
        "query": query,
        "file_type": "doc",
    }

    return await post_with_json_response(gen_url, params)


@mcp.tool()
async def generate_sheet(query: str) -> Dict:
    """Generate a URL for a spreadsheet file based on the input query."""
    params = {
        "api_key": api_key,
        "query": query,
        "file_type": "sheet",
    }

    return await post_with_json_response(gen_url, params)


async def post_with_json_response(url: str, params: Dict) -> Dict:
    async with ClientSession() as session:
        try:
            async with session.post(url, params=params) as response:
                res = await response.json()

            if res.get('code') == 200:
                return {
                    "status": "success",
                    "url": res['data']['url']
                }
            else:
                return {
                    "status": "success",
                    "error": res.get('message')
                }
        except Exception as e:
            return {
                "status": "failed",
                "error": str(e)
            }
