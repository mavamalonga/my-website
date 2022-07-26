
function fetch_api(request_url){
    return fetch(request_url).then(function(response) {
      return response.json();
    }).then(function(json) {
      return json;
    });
}
  

function get_projects(){
    const url = 'https://alpha-mavamalonga.herokuapp.com/api/project/'
    const work_card = document.querySelectorAll(".work__card");

    fetch_api(url).then(function(result) {
        for (let i = 0; i < result.length; i++){
            work_card[i].setAttribute('class', `work__card mix ${result[i]['framework']}`)
            work_card[i].querySelector('.work__img').setAttribute('src', result[i]['image']);
            work_card[i].querySelector('.work__title').innerHTML = result[i]['title'];
            work_card[i].querySelector('.home__social-link').setAttribute('href', result[i]['github']);
            for (let x = 0; x < result[i]['badges'].length; x++){
                work_card[i].querySelectorAll('.badge.badge-info')[x].innerHTML = result[i]['badges'][x]['name'];
            }
            work_card[i].querySelector('.works__modal-title').innerHTML = result[i]['title'];
            work_card[i].querySelector('.works__modal-description').innerHTML = result[i]['description'];
            for (let z = 0; z < result[i]['tasks'].length; z++){
              try {
                work_card[i].querySelectorAll('.works__modal-info')[z].innerHTML = result[i]['tasks'][z]['description'];
              } catch (error) {
                console.log(error);
              }
          }
        }
    })
}


window.onload = get_projects();
