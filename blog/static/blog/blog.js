function temp_test(data){
    var alt_str = ''
    for(key in data){
        console.log(key + ':' + data[key] )
        alt_str += key + ':' + data[key] + '\n'
    }
    //alert(alt_str)
}

function create_div_from_data(data){
    var div = document.createElement('div')
    div.id = data.post_id
    div.class = 'post_abstract'
    var post_link = document.createElement('a')
    var topic_tag = document.createElement('h3')
    post_link.href = '/blog/' + data.post_id
    post_link.innerText = data.topic
    topic_tag.appendChild(post_link)
    var date_text = document.createElement('I')
    date_text.innerText = "Posted on "+ data.date
    div.appendChild(topic_tag)
    div.appendChild(date_text)
    div.appendChild(document.createElement('br'))
    return div
}