from typing import Any, Dict, List, Optional
from trae_core.tools import WebSearch, WebFetch

class WebSearchSkill:
    def __init__(self):
        self.name = "web_search"
        self.description = "使用 TRAE 内置工具执行网络搜索和网页获取"
        self.version = "2.0.0"
        self.web_search = WebSearch()
        self.web_fetch = WebFetch()
    
    def get_info(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "description": self.description,
            "version": self.version,
            "trae_tools": ["WebSearch", "WebFetch"],
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
                },
                "url": {
                    "type": "string",
                    "required": False,
                    "description": "网页URL，用于获取页面内容"
                }
            }
        }
    
    def search(self, query: str, num_results: int = 5) -> Dict[str, Any]:
        """
        执行网络搜索
        
        Args:
            query: 搜索查询词
            num_results: 返回结果数量
        
        Returns:
            Dict包含搜索结果和状态信息
        """
        try:
            result = self.web_search(query=query, num=num_results)
            return {
                "success": True,
                "data": result.get("results", []),
                "total": len(result.get("results", []))
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }
    
    def fetch(self, url: str) -> Dict[str, Any]:
        """
        获取网页内容
        
        Args:
            url: 网页URL
        
        Returns:
            Dict包含网页内容和状态信息
        """
        try:
            result = self.web_fetch(url=url)
            return {
                "success": True,
                "data": {
                    "url": url,
                    "title": result.get("title", ""),
                    "content": result.get("content", ""),
                    "snippets": result.get("snippets", [])
                }
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }
    
    def execute(self, query: str = None, url: str = None, num_results: int = 5) -> Dict[str, Any]:
        """
        执行搜索或获取网页内容
        
        Args:
            query: 搜索查询词（与 url 二选一）
            url: 网页URL（与 query 二选一）
            num_results: 返回结果数量
        
        Returns:
            Dict包含执行结果
        """
        if url:
            return self.fetch(url)
        elif query:
            return self.search(query, num_results)
        else:
            return {
                "success": False,
                "error": "必须提供 query 或 url 参数"
            }

def create_skill():
    return WebSearchSkill()
