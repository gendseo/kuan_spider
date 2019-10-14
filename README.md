# 项目说明

酷安-应用数据大分析 [原页面](https://www.coolapk.com/apk/)

## 特性

- 轻量级
- 解析相对较快
- 不依赖数据库
- 快速展示可视化数据

## 截图

![image](https://user-images.githubusercontent.com/27917862/66763221-0f63f100-eeda-11e9-920f-366a7215ebaf.png)
![image](https://user-images.githubusercontent.com/27917862/66763327-3f12f900-eeda-11e9-85e7-c9c5d2d2a94c.png)
![image](https://user-images.githubusercontent.com/27917862/66763305-31f60a00-eeda-11e9-8978-3c157a2990d7.png)

## 目录结构

``` md
.
├── README.md          // 项目说明
├── api.py             // 提供网页 API
├── db.py              // 数据库配置、模型
├── service.py         // API 业务逻辑
├── spider.py          // 爬虫主体
├── static             // 静态资源文件夹
│   ├── echarts.min.js // 图表库依赖
│   ├── fetch.js       // 获取评分统计接口数据
│   └── style.css      // 样式表
├── templates          // 模板文件夹
    └── index.html     // 主页
```

## Python 模块依赖

``` md
Flask              1.1.1
Flask-SQLAlchemy   2.4.1
requests           2.22.0
bs4                0.0.1
lxml               4.4.1
```

安装所有依赖：

``` shell
pip3 install Flask Flask-SQLAlchemy requests bs4 lxml
```

## 如何运行

1. **运行 `spider.py` 爬虫主体文件获取数据**
    1. 自动在当前目录下建 `sqlite3` 数据库
    2. 为节省对应站点的资源，默认只爬十页（一页10条数据）
2. **运行 `api.py` 文件运行 `web` 服务**
    1. 通过 `http://localhost:5000` 访问主页
    2. 完成（enjoy；

**数据是流向是异步的，第1步开启爬虫主体后就可以运行第2步的 web 服务，不断刷新查看数据变化（新姿势；**

## 进度

- [x] 基本功能

## 更新日志

``` md
2019-10-14 : v1.00
1.全新的灵魂重构
2.重写部分函数和方法
3.精简不必要的逻辑
4.增加了许多 App 字段
5.更改图表样式
6.修复了一堆 BUG

如无必要，不会增加新功能，只修 BUG。
有需求请提 Issues
```

``` md
2019-10-12 : v0.01
1.完成基本功能
```

## 版权声明

请保护对应站点的数据隐私，您可以将该项目作为学习 Python 爬虫的 Demo，但请不要作为商业使用。

请查看 [对应站点的版权声明](https://www.coolapk.com/about/copyright.html)
