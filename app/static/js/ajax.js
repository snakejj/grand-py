

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

            let answer = document.createElement("p"); // <p></p>
            answer.classList.add("answer"); // <p class="answer"></p>
            answer.textContent = `${response.grandpyanswer}`;
            answers.appendChild(answer);


            let mapElt = document.createElement("div"); // <div></div>
            mapElt.classList.add("map"); // <div class="map"></div>
            answers.appendChild(mapElt);

            
            // ------HERE API MARKER ON THE MAP JS -----

            function addMarkersToMap(map) {
                let placeMarker = new H.map.Marker({lat:`${response.latitude}`, lng:`${response.longitude}`});
                map.addObject(placeMarker);
            }
            
            /**
             * Boilerplate map initialization code starts below:
             */
            
            //Step 1: initialize communication with the platform
            // In your own code, replace variable window.apikey with your own apikey
            let platform = new H.service.Platform({
              apikey: `${response.mapapi}`
            });
            let defaultLayers = platform.createDefaultLayers();
            
            //Step 2: initialize a map - this map is centered over Europe
            let map = new H.Map(mapElt,
              defaultLayers.vector.normal.map,{
              center: {lat:`${response.latitude}`, lng:`${response.longitude}`},
              zoom: 14,
              pixelRatio: window.devicePixelRatio || 1
            });

            // add a resize listener to make sure that the map occupies the whole container
            window.addEventListener('resize', () => map.getViewPort().resize());

            addMarkersToMap(map);
            
            // -----------------------------------------

            let anecdote = document.createElement("p"); // <p></p>
            anecdote.classList.add("anecdote"); // <p class="anecdote"></p>
            anecdote.textContent = `${response.grandpyanecdote} ${response.articleextract}`;
            answers.appendChild(anecdote);

            let link = document.createElement('a'); // <a></a>
            link.setAttribute('href',`${response.urlarticle}`); // <a href:"`${response.urlarticle}`"></a>
            link.innerHTML = "En savoir plus"; // <a href:"`${response.urlarticle}`"> En savoir plus</a>
            answers.appendChild(link);

            let line = document.createElement("hr"); // <hr />
            answers.appendChild(line);

            anecdote.scrollIntoView({behavior: "smooth"});

        } else if (response.grandpyerror) {
            let errorSentence = document.createElement("p"); // <p></p>
            errorSentence.classList.add("error"); // <p class="error"></p>
            errorSentence.textContent = `${response.grandpyerror}`;
            let answers = document.querySelector("#answers");
            answers.appendChild(errorSentence);
            errorSentence.scrollIntoView({behavior: "smooth"});
        }
      
        
    });
});