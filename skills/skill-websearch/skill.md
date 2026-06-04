# Web Search Skill

## 概述

网络搜索技能，使用 **TRAE 内置工具**执行网络搜索和网页获取。无需 API Key，直接利用 TRAE 平台的网络搜索能力。

## 技能信息

| 属性 | 值 |
|------|-----|
| 名称 | web_search |
| 显示名称 | 网络搜索 |
| 版本 | 2.0.0 |
| 作者 | Skill Developer |
| 分类 | information |
| 使用工具 | WebSearch, WebFetch |

## 参数说明

### execute 方法

| 参数名 | 类型 | 必填 | 默认值 | 说明 |
|--------|------|------|--------|------|
| query | string | 否 | - | 搜索查询词（与 url 二选一） |
| url | string | 否 | - | 网页URL（与 query 二选一） |
| num_results | integer | 否 | 5 | 返回结果数量 |

### search 方法

| 参数名 | 类型 | 必填 | 默认值 | 说明 |
|--------|------|------|--------|------|
| query | string | 是 | - | 搜索查询词 |
| num_results | integer | 否 | 5 | 返回结果数量 |

### fetch 方法

| 参数名 | 类型 | 必填 | 默认值 | 说明 |
|--------|------|------|--------|------|
| url | string | 是 | - | 网页URL |

## 使用示例

### 基本搜索

```python
from skills.skill_websearch import create_skill

# 创建技能实例
skill = create_skill()

# 执行搜索
result = skill.execute(query="Python 教程", num_results=10)

# 处理结果
if result["success"]:
    for item in result["data"]:
        print(f"标题: {item['name']}")
        print(f"链接: {item['url']}")
        print(f"摘要: {item['snippet']}")
        print("---")
else:
    print(f"搜索失败: {result['error']}")
```

### 使用 search 方法

```python
# 创建技能实例
skill = create_skill()

# 执行搜索
result = skill.search("人工智能发展趋势", num_results=5)
```

### 获取网页内容

```python
# 创建技能实例
skill = create_skill()

# 获取网页内容
result = skill.execute(url="https://docs.python.org/3/")
# 或者使用 fetch 方法
result = skill.fetch("https://docs.python.org/3/")

if result["success"]:
    print(f"标题: {result['data']['title']}")
    print(f"内容: {result['data']['content']}")
```

## 返回值结构

### search 返回值

```json
{
    "success": true,
    "data": [
        {
            "name": "搜索结果标题",
            "url": "https://example.com",
            "snippet": "结果摘要..."
        }
    ],
    "total": 10
}
```

### fetch 返回值

```json
{
    "success": true,
    "data": {
        "url": "https://example.com",
        "title": "页面标题",
        "content": "页面完整内容...",
        "snippets": ["关键片段1", "关键片段2"]
    }
}
```

## 与 TRAE 内置工具的对应关系

| Skill 方法 | TRAE 内置工具 | 说明 |
|------------|--------------|------|
| search() | WebSearch | 执行网络搜索 |
| fetch() | WebFetch | 获取网页内容 |
| execute(query=...) | WebSearch | 执行搜索 |
| execute(url=...) | WebFetch | 获取网页内容 |

## 优势

- ✅ **无需 API Key**：直接使用 TRAE 平台的内置搜索能力
- ✅ **简单易用**：统一的接口，同时支持搜索和网页获取
- ✅ **稳定可靠**：依托 TRAE 平台的网络服务
- ✅ **免费使用**：无需付费即可享受高质量搜索服务

## 依赖

- trae_core >= 1.0.0

## 版本历史

- **2.0.0**: 重构为使用 TRAE 内置工具，移除外部 API 依赖
- **1.0.0**: 初始版本，使用 Bing Search API
