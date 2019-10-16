// encoding: utf-8
// author: gendseo
// date: 2019-10-12
// updated: 2019-10-16

// 使用了 Echarts 图表框架
// 如何配置请查看 https://www.echartsjs.com/zh/tutorial.html

// 评分接口: /count/ranks
// 获取评分统计接口数据
new Promise((resolve, reject) => {
    const req = new XMLHttpRequest()
    req.open("GET", "/count/ranks", true)
    req.send()
    req.onreadystatechange = () => {
        if (req.readyState === 4 && req.status === 200) {
            resolve(JSON.parse(req.responseText))
        }
    }
    req.onerror = (err) => {
        reject(err)
    }
}).then((res) => {
    // 初始化第一个图表
    const echarts1 = echarts.init(document.getElementById('echarts1'), 'macarons')
    // 改造数据使其变成图表需要的格式
    let data = []
    for (let key in res) {
        data.push({
            'name': key,
            'value': res[key]
        })
    }
    // 构造图表配置项
    const option = {
        title: {
            text: '评分情况统计图',
            left: 'center'
        },
        tooltip: {
            trigger: 'item',
            formatter: "{b} : {c} ({d}%)"
        },
        legend: {
            bottom: 0,
            left: 'center',
            data: Object.keys(res)
        },
        series: [{
            type: 'pie',
            radius: '75%',
            center: ['50%', '50%'],
            roseType: 'radius',
            data: data
        }]
    };
    // 设置图表配置
    echarts1.setOption(option)
}).catch((err) => {
    console.log(`err:`, err)
})

// 评分和评分次数统计接口: /count/rank_rank_num
// 获取评分和评分次数统计接口数据
new Promise((resolve, reject) => {
    const req = new XMLHttpRequest()
    req.open("GET", "/count/rank_rank_num", true)
    req.send()
    req.onreadystatechange = () => {
        if (req.readyState === 4 && req.status === 200) {
            resolve(JSON.parse(req.responseText))
        }
    }
    req.onerror = (err) => {
        reject(err)
    }
}).then((res) => {
    // 获取所有名称
    const name = res['name']
    // 获取所有评分与评分次数
    const data = res['data']
    // 初始化第二个图表
    const echarts2 = echarts.init(document.getElementById('echarts2'), 'macarons')
    // 构造图表配置项
    const option = {
        title: {
            text: '评分与评分次数散点图',
            left: 'center'
        },
        tooltip: {
            show: true,
            showDelay: 0,
            // 格式化鼠标移入所触发的 tooltip 提示信息
            formatter: params => {
                return name[params.dataIndex] + '<br/>' + params.value[0] + ' 次评论' + '<br/>' + params.value[1] + ' 分'
            },
            axisPointer: {
                type: 'cross'
            }
        },
        xAxis: {},
        yAxis: {},
        series: [{
            // 点大小
            symbolSize: 5,
            data: data,
            type: 'scatter'
        }]
    };
    // 设置图表配置
    echarts2.setOption(option)
    // 设置图表点击事件
    echarts2.on('click', (params) => {

        // 为了找到 dom 中 id 匹配的元素，需要提前在页面中构造 tr 的 id (行 id)
        const domStr = 'app-' + params.dataIndex
        let dom = document.getElementById(domStr)

        // 因为元素可能已经出现在屏幕中，所以不会触发滚动事件
        // 所以需要手动触发
        window.scrollTo({
            top: dom.offsetTop - 200,
            behavior: 'instant' // 'instant' 瞬间滚动 | 'smooth' 平滑滚动
        })
        // 高亮显示被点击事件找到的 dom 元素
        dom.style.backgroundColor = '#f4d3b5'
        setTimeout(() => {
            dom.style.backgroundColor = '#fff'
        }, 1000)

    })
}).catch((err) => {
    console.log(`err:`, err)
})