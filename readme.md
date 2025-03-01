# WebChatAI

> 基于python和js的chatai简易框架

## 功能介绍：

1. 本地转发到特定端口，生成网页
2. 网页可与deepseek对话

## 待完善

- [ ] 一键docker部署
- [ ] 前端界面优化
- [ ] 增加其他可选模型
- [ ] 可指定端口
- [ ] 增加数据库

## 运行

* 将项目克隆到本地
* 将 `key.py` 中的 [`api_key`](./key.py) 替换为你的[deepseek api](https://platform.deepseek.com/api_keys).
* 保存后，键入

```bash
pip install -r  requirements.txt
```
 

```bash
python3 app.py
```

端口号为5000，访问
```bash
http://127.0.0.1:5000
```