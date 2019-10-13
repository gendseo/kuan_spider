# 项目说明

酷安-应用数据大分析 [原页面](https://www.coolapk.com/apk/)

## 截图

![image](https://user-images.githubusercontent.com/27917862/66711611-a8531900-edc1-11e9-8bf8-6472f1aa901a.png)

![image](https://user-images.githubusercontent.com/27917862/66711619-d0427c80-edc1-11e9-8745-a728afc498a5.png)

![image](https://user-images.githubusercontent.com/27917862/66711658-9de54f00-edc2-11e9-8048-82cccf0f11cb.png)

## 目录结构

```
.
├── README.md          // 项目说明
├── api.py             // 提供网页 API
├── db.py              // 数据库配置、模型
├── service.py         // API 业务逻辑
├── spider.py          // 爬虫主体
├── static             // 静态资源文件夹
│   ├── echarts.min.js // 图标依赖
│   ├── fetch.js       // 获取评分统计接口的数据
│   └── style.css      // 样式表
├── templates          // 模板文件夹
    └── index.html     // 主页
```

## 如何运行

1. 运行 spider.py 文件获取数据
    1. 会自动在当前目录下建 sqlite3 数据库
    2. 为节省对应站点的资源，默认只爬十页（一页10条数据）
    3. 完成（enjoy；
2. 运行 api.py 文件运行 web 服务
    1. 通过 http://localhost:5000 访问主页
    2. 完成（enjoy；

# 更新日志

```
2019-10-12 : v0.01
完成基本功能
```