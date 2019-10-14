// encoding: utf-8
// author: gendseo
// date: 2019-10-12
// updated: 2019-10-14

new Promise((resolve, reject) => {
    const req = new XMLHttpRequest()
    req.open("GET", "/score", true)
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
    let data = []
    for (let key in res) {
        data.push({'name': key, 'value': res[key]})
    }
    const option = {
        title: {
            text: '应用评分情况统计',
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
    echarts.init(document.getElementById('echarts')).setOption(option)
}).catch((err) => {
    console.log(`err:`, err)
})
