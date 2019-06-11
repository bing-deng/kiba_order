// song website https://www.mp3juices.cc/
function sleep(time) {
    return new Promise((resolve) => setTimeout(resolve, time));
}

// 用法
sleep(500).then(() => {
    // 这里写sleep之后需要去做的事情
})
await sleep(1500)
$('input[name="query"]')[0].value = "Perfect"
$('#button').click()
await sleep(1500);
$('.download.1')[0].click()
await sleep(1500)
$('.url')[0].click()