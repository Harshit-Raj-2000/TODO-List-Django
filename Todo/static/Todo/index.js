

document.querySelector('.addform').onsubmit = (e) => {
    e.preventDefault()
    var csrf_token = document.querySelector('input[name="csrfmiddlewaretoken"]').value
    var url = e.target.dataset.task_url
    var xhr = new XMLHttpRequest()
 
    xhr.open('POST', url , true)
    xhr.setRequestHeader('content-type', 'application/json')
    xhr.setRequestHeader('X-CSRFToken', csrf_token )

    data = JSON.stringify({
        task : document.querySelector('#id_task').value
    })
    xhr.onload = function(){
        if(this.status == 200){
            console.log('Added the task')
        }
        else{
            console.log('Some error occurred..Try again.')
        } 
    }
    xhr.send(data)

}