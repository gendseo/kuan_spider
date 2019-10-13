# 项目说明

酷安-应用数据大分析 [原页面](https://www.coolapk.com/apk/)

## 特性

- 轻量级
- 解析快
- 不依赖数据库
- 快速展示可视化数据
- 启动方便（相对）

## 截图

![image](https://user-images.githubusercontent.com/27917862/66711611-a8531900-edc1-11e9-8bf8-6472f1aa901a.png)

![image](https://user-images.githubusercontent.com/27917862/66711619-d0427c80-edc1-11e9-8745-a728afc498a5.png)

![image](https://user-images.githubusercontent.com/27917862/66711729-0ed93680-edc4-11e9-883b-cfcbad18e6b2.png)

## 目录结构

``` md
.
├── README.md          // 项目说明
├── api.py             // 提供网页 API
├── db.py              // 数据库配置、模型
├── service.py         // API 业务逻辑
├── spider.py          // 爬虫主体
├── static             // 静态资源文件夹
│   ├── echarts.min.js // 图表依赖
│   ├── fetch.js       // 获取评分统计接口数据
│   └── style.css      // 样式表
├── templates          // 模板文件夹
    └── index.html     // 主页
```

## Python 模块依赖

``` md
Flask 1.1.1
Flask-SQLAlchemy 2.4.1
requests 2.22.0
bs4 0.0.1
lxml 4.4.1
```

安装所有依赖：

``` shell
pip3 install Flask Flask-SQLAlchemy requests bs4 lxml
```

## 如何运行

1. 运行 spider.py 文件获取数据
    1. 会自动在当前目录下建 sqlite3 数据库
    2. 为节省对应站点的资源，默认只爬十页（一页10条数据）
2. 运行 api.py 文件运行 web 服务
    1. 通过 `http://localhost:5000` 访问主页
    2. 完成（enjoy；

## 进度

- [x] 基本功能
- [ ] 打包自动化运行

## 更新日志

``` md
2019-10-12 : v0.01
完成基本功能
```
