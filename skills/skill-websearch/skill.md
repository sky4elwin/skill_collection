# Web Search Skill

## 概述

网络搜索技能，用于执行实时网络搜索，获取最新信息。

## 技能信息

| 属性 | 值 |
|------|-----|
| 名称 | web_search |
| 显示名称 | 网络搜索 |
| 版本 | 1.0.0 |
| 作者 | Skill Developer |
| 分类 | information |

## 参数说明

| 参数名 | 类型 | 必填 | 默认值 | 说明 |
|--------|------|------|--------|------|
| query | string | 是 | - | 搜索查询词 |
| num_results | integer | 否 | 5 | 返回结果数量 |

## 使用示例

```python
from skills.skill_websearch import create_skill

# 创建技能实例
skill = create_skill()

# 执行搜索
result = skill.execute("Python 教程", num_results=10)

# 处理结果
if result["success"]:
    for item in result["data"]:
        print(item["name"])
        print(item["url"])
        print(item["snippet"])
else:
    print(f"搜索失败: {result['error']}")
```

## 返回值结构

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
    "total": 1000
}
```

## 配置说明

在 `config.yaml` 中配置 API 密钥：

```yaml
settings:
  api_key: "your_api_key_here"
  default_results: 5
  timeout: 30
```

## 依赖

- requests >= 2.31.0
- pyyaml >= 6.0
