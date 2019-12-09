
function ajaxPost(url, data, callback, isJson) {
    var req = new XMLHttpRequest();
    req.open("POST", url);
    req.addEventListener("load", function () {
        if (req.status >= 200 && req.status < 400) {
            // call the function callback 
            callback(req.responseText);
        } else {
            console.error(req.status + " " + req.statusText + " " + url);
        }
    });
    req.addEventListener("error", function () {
        console.error("Erreur réseau avec l'URL " + url);
    });
    if (isJson) {
        // define content as JSON
        req.setRequestHeader("Content-Type", "application/json");
        // Transform JSON data to texte before sending
        data = JSON.stringify(data);
    }
    req.send(data);
}


let form = document.querySelector("#question-form");
form.addEventListener("submit", function (event) {
    event.preventDefault();
    let data = new FormData(form);
    ajaxPost("/answer", data, function (response) {
        response = JSON.parse(response);
        
        if (response.grandpyanswer) {
            let answers = document.querySelector("#answers");

            function removeElementsByClass(className){
                var elements = document.getElementsByClassName(className);
                while(elements.length > 0){
                    elements[0].parentNode.removeChild(elements[0]);
                }
            }

            removeElementsByClass("answer");
            removeElementsByClass("map");
            removeElementsByClass("anecdote");

            let answer = document.createElement("p"); // <p></p>
            answer.classList.add("answer"); // <p class="answer"></p>
            answer.textContent = `${response.grandpyanswer}`;
            answers.appendChild(answer);

            let map = document.createElement("div"); // <div></div>
            map.classList.add("map"); // <div class="map"></div>
            answers.appendChild(map);

            let anecdote = document.createElement("p"); // <p></p>
            anecdote.classList.add("anecdote"); // <p class="anecdote"></p>
            anecdote.textContent = `${response.grandpyanecdote} ${response.articleextract} ${response.urlarticle}`;
            answers.appendChild(anecdote);

            anecdote.scrollIntoView();

        } else if (response.grandpyerror) {
            let errorSentence = document.createElement("p"); // <p></p>
            errorSentence.classList.add("error"); // <p class="error"></p>
            errorSentence.textContent = `${response.grandpyerror}`;
            let answers = document.querySelector("#answers");
            answers.appendChild(errorSentence);
            errorSentence.scrollIntoView();
        }
      
        
    });
});