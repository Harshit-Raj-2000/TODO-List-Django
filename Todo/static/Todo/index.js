

document.querySelector('.addform').onsubmit = (e) => {
    e.preventDefault()
    var csrf_token = document.querySelector('input[name="csrfmiddlewaretoken"]').value
    var url = e.target.dataset.task_url
    var xhr = new XMLHttpRequest()
    var task_value =  document.querySelector('#id_task').value
    xhr.open('POST', url , true)
    xhr.setRequestHeader('content-type', 'application/json')
    xhr.setRequestHeader('X-CSRFToken', csrf_token )

    data = JSON.stringify({
        task : task_value
    })
    xhr.onload = function(){
        if(this.status == 200){
            var new_task = `<li class="taskli animateAdd" >${ task_value }
            <i class="fa fa-trash" aria-hidden="true"></i>
            </li>`
            document.querySelector('#id_task').value  = ""
            document.querySelector('ul').innerHTML += new_task
            deleteTaskListener()
            setTimeout(function(){
                document.querySelector('ul').lastChild.classList.remove('animateAdd')
            },1000)
        }
        else{
            console.log('Some error occurred..Try again.')
        } 
    }
    xhr.send(data)

}

function deleteTaskListener(){
document.querySelectorAll('.fa-trash').forEach((i)=>{
    i.onclick = deleteTask
})
}
deleteTaskListener()

function deleteTask(e){
    removeLi = e.target.parentElement
    parentUl = document.querySelector('ul')
    url = parentUl.dataset.delete_url
    csrf_token = document.querySelector('input[name="csrfmiddlewaretoken"]').value

    index_li = Array.prototype.indexOf.call(parentUl.children, removeLi)
    
    var xhr = new XMLHttpRequest()
    xhr.open('POST', url, true)
    xhr.setRequestHeader('content-type', 'application/json')
    xhr.setRequestHeader('X-CSRFToken', csrf_token )

    data = JSON.stringify({
        index : index_li
    })

    xhr.onload = function(){
        if(this.status == 200){
            removeLi.classList.add('animateRemove')
            setTimeout(function(){
                removeLi.remove()
            },1000)
        }
        else{
            console.log("Some error occured.Please Try again!")
        }
    }
    xhr.send(data)
}


