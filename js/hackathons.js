// console.log(hackathons)

addNearby();

function addNearby(){

  var sponsordivs = document.getElementsByClassName("nearby-section");

  var str = "";
  for(item in hackathons){
    item = hackathons[item];
    item = JSON.parse(item);
    var month = moment( item["date"].substring(0, item["date"].indexOf(" ") ), "MMM").format("M");
    if(month < 8){
      m = moment( item["date"].substring(0, item["date"].indexOf("-") ) + "-2018", "MMM Do-YYYY");
    }
    else{
      m = moment( item["date"].substring(0, item["date"].indexOf("-") ) + "-2017", "MMM Do-YYYY");
    }

    if( moment().isBefore(m.format("M-D-Y")) ){
      
      
      str += "<div class='action-section'>";
      str += "<img src='"+item["img"]+ "'/>";
      str += "<div class='info-container'>";
      str += "<h3 class='section-title'>" + item["name"] + "</h3>";
      str += "<h4 class='section-year'>" + item["date"] + "</h4>";
      str += "<h4 class='section-year'>" + item["city"] + ", " + item["state"]  + "</h4>";
      str += "<a class='button' href='" + item["link"] + "'target='_blank'> Sign Up </a>";
      str += "</div></div>"
      
    }

    sponsordivs[0].innerHTML = str;
  }
}