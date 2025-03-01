# WebChatAI

> 基于python和js的chatai简易框架

## 功能介绍：

1. 本地转发到特定端口，生成网页
2. 网页可与deepseek对话

## 待完善

- [x] 一键docker部署
- [ ] 前端界面优化
- [ ] 增加其他可选模型
- [ ] 可指定端口
- [ ] 增加数据库

## 运行

### docker 部署

克隆到本地后，当前目录下输入：

```bash
docker build -t cofallen/webchatai .

docker run -itd \
    -p 5000:5000 \
    -e API_KEY=sk-xxx \
    --name=chatai \
    --restart=always \
    cofallen/webchatai
```

> 目前dockerhub访问不稳定，暂时本地部署调用，所需时间有点长。

### 源码运行

* 将项目克隆到本地
* 将 `key.py` 中的 [`api_key`](./key.py) 替换为你的[deepseek api](https://platform.deepseek.com/api_keys).
* 保存后，键入

```bash
pip install -r  requirements.txt
```
 

```bash
python3 app.py
```

### 访问

端口号为5000，访问
```bash
http://127.0.0.1:5000
```