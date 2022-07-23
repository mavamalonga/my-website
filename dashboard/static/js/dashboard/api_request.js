const url = 'http://localhost:8000/api/project';

function fetch_api(request_url){
    return fetch(request_url).then(function(response) {
      return response.json();
    }).then(function(json) {
      return json;
    });
  }
  
function get_projects(){
    var work_container = document.querySelector(".work__container");

    fetch_api(url).then(function(result) {
        for (let i = 0; i < result.length; i++){
            console.log(result[i]['title']);

            var work_card = document.createElement('div');
            var att_card = document.createAttribute('class');
            att_card.value = 'work__card mix web';
            work_card.setAttribute('class', 'work__card mix web');

            var img = document.createElement('img');
            var att1_img = document.createAttribute('class');
            var att2_img = document.createAttribute('src');
            att1_img.value = 'work__img';
            att2_img.value = `{% static '${result[i]['image']}' %}`;
            img.setAttribute('class', 'work__img');
            img.setAttribute('src', `${result[i]['image']}`);

            var badge = document.createElement('span');
            var att_badge = document.createAttribute('class');
            att_badge.value = 'badge badge-info';
            badge.setAttribute('class', 'badge badge-info');
            badge.innerHTML = 'Python';

            var work_title = document.createElement('h3');
            var att_title = document.createAttribute('class');
            att_title.value = 'work__title';
            work_title.setAttribute('class', 'work__title');
            work_title.innerHTML = result[i]['title'];

            var work_button = document.createElement('a');
            var att_button = document.createAttribute('class');
            att_button.value = 'work__button';
            work_button.setAttribute('class', 'work__button');
            work_button.innerHTML = 'Demo';

            var bx = document.createElement('i');
            bx.setAttribute('class', 'bx bx-right-arrow-alt work__icon');
            work_button.appendChild(bx);

            work_card.appendChild(img);
            var br = document.createElement('br');
            work_card.appendChild(br);
            work_card.appendChild(badge);
            work_card.appendChild(work_title);
            work_card.appendChild(work_button);

            work_container.appendChild(work_card);





            /*
            OK <div class="work__card mix web">
            <img src="{% static 'img/dashboard/work1.jpg' %}" alt="work 1" class="work__img" /><br>
            <span class="badge badge-info">Python</span>
                      
            <span class="badge badge-info">Pygame</span>

            <h3 class="work__title">Web design</h3>

            <a class="work__button" style="text-decoration: none; cursor: pointer;">
              Demo <i class="bx bx-right-arrow-alt work__icon"></i>
            </a>
            */
        }
    })
}

get_projects();