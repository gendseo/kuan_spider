# Kuan_Spider

>酷安-应用数据分析 [原页面](https://www.coolapk.com/apk/)
>
>理性看待项目的不足之处，它只是一个在校期间的课后作业。

## 特性

- 轻量级
- 解析快
- 友好的提示和界面
- 不依赖数据库
- 使用 Flask 自带 Jinja2 模板，原生 JS 不依赖 JQuery
- 快速展示可视化数据

## 截图

![image1](https://raw.githubusercontent.com/gendseo/kuan_spider/master/screenshots/1.jpg)
![image2](https://raw.githubusercontent.com/gendseo/kuan_spider/master/screenshots/2.jpg)
![image3](https://raw.githubusercontent.com/gendseo/kuan_spider/master/screenshots/3.jpg)
![image4](https://raw.githubusercontent.com/gendseo/kuan_spider/master/screenshots/4.jpg)
![image5](https://raw.githubusercontent.com/gendseo/kuan_spider/master/screenshots/5.jpg)

## 目录结构

``` md
.
├── README.md                // 项目说明
├── api.py                   // 提供网页 API
├── db.py                    // 数据库配置、模型
├── plantuml                 // UML 文件夹
│   ├── data_flow.wsd        // 数据流向图源文件
│   └── sequence_diagram.wsd // 时序图源文件
├── screenshots              // 截图文件夹
├── service.py               // API 业务逻辑
├── spider.py                // 爬虫主体
├── static                   // 静态资源文件夹
│   ├── echarts.min.js       // 图表库依赖
│   ├── fetch.js             // 获取统计接口数据
│   ├── loading.gif          // 加载动画
│   ├── logo.png             // Logo
│   ├── macarons.js          // 图表库主题依赖
│   └── style.css            // 样式表
└── templates                // 模板文件夹
    └── index.html           // 主页
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

时序图：

![时序图](https://raw.githubusercontent.com/gendseo/kuan_spider/master/screenshots/sequence_diagram.png)

**数据的流向是异步的，第1步开启爬虫主体后就可以运行第2步的 web 服务，请不断刷新查看数据变化（新姿势；**
![数据流向](https://raw.githubusercontent.com/gendseo/kuan_spider/master/screenshots/data_flow.png)

## 进度

如无必要，不会增加新功能，只修 BUG。
有需求请提 Issues

- [x] 基本功能

## 更新日志

``` md
2019-10-16 : v1.01
1. 新增 UML 时序图、数据流向图
2. 新增模块说明
3. 增加每个文件详细的注释
4. 增加了更多的截图
5. 解决数据量过多造成的加载卡顿，将图片缓存在本地，而不是存链接
6. 增加了等待加载动画
7. 将大部分需要二次请求的数据缓存到本地
8. 精简不必要的逻辑
9. 删除了许可证，修改版权声明
10. 修复了一些 BUG
```

``` md
2019-10-14 : v1.00
1. 全新的灵魂重构
2. 重写部分函数和方法
3. 精简不必要的逻辑
4. 增加了许多 App 字段
5. 更改图表样式
6. 修复了一堆 BUG
```

``` md
2019-10-12 : v0.01
1. 完成基本功能
```

## 版权声明

![licence](https://cloud.githubusercontent.com/assets/7392658/20011165/a0caabdc-a2e5-11e6-974c-8d4961c7d6d3.png)

请您保护对应站点的数据隐私，您可以将该项目作为学习 Python 爬虫的 Demo，但请不要作为商业目的使用。

请查看 [对应站点的版权声明](https://www.coolapk.com/about/copyright.html)

如有侵权，提 Issues 后立即删除
