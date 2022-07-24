
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
        for (let i = 0; i < 6; i++){
            work_card[i].querySelector('.work__img').setAttribute('src', result[i]['image']);
            work_card[i].querySelector('.work__title').innerHTML = result[i]['title'];
            for (let x = 0; x < result[i]['badges'].length; x++){
                console.log(result[i]['badges'][x]['name']);
                work_card[i].querySelectorAll('.badge.badge-info')[x].innerHTML = result[i]['badges'][x]['name'];
            }
        }
    })
}

window.onload = get_projects(url = 'api/project');
