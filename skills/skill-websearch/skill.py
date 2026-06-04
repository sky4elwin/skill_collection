from typing import Any, Dict, List, Optional
import requests

class WebSearchSkill:
    def __init__(self):
        self.name = "web_search"
        self.description = "执行网络搜索，获取实时信息"
        self.version = "1.0.0"
    
    def get_info(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "description": self.description,
            "version": self.version,
            "parameters": {
                "query": {
                    "type": "string",
                    "required": True,
                    "description": "搜索查询词"
                },
                "num_results": {
                    "type": "integer",
                    "required": False,
                    "description": "返回结果数量，默认5",
                    "default": 5
                }
            }
        }
    
    def execute(self, query: str, num_results: int = 5) -> Dict[str, Any]:
        try:
            search_url = "https://api.search.bing.com/v7.0/search"
            headers = {"Ocp-Apim-Subscription-Key": "YOUR_API_KEY"}
            params = {"q": query, "count": num_results}
            
            response = requests.get(search_url, headers=headers, params=params)
            response.raise_for_status()
            
            results = response.json()
            return {
                "success": True,
                "data": results.get("webPages", {}).get("value", []),
                "total": results.get("webPages", {}).get("totalEstimatedMatches", 0)
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }

def create_skill():
    return WebSearchSkill()
