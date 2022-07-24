
function fetch_api(request_url){
    return fetch(request_url).then(function(response) {
      return response.json();
    }).then(function(json) {
      return json;
    });
  }
  
//window.onload = 
function get_projects(path){
    console.log(path)
    const url = "http://localhost:8000/" + path
    const work_card = document.querySelectorAll(".work__card");

    fetch_api(url).then(function(result) {
        for (let i = 0; i < result.length; i++){
            work_card[i].querySelector('.work__img').setAttribute('src', result[i]['image']);
            work_card[i].querySelector('.work__title').innerHTML = result[i]['title'];
        }
    })
}

window.onload = get_projects(url = 'api/project');
