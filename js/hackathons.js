// console.log(hackathons)

addNearby();
function addNearby(){
    var sponsordivs = document.getElementsByClassName("nearby-section");
    var str = "";
    for(s in hackathons){
      console.log(s);
    //   str += "<img src='"+ logos + sponsorImages[s] +"'></img>";
    str += "<div class='action-section'>";
    str += "<img src='"+hackathons[s][0]+ "' alt='HackTJ 4.0' />";
    str += "<div class='info-container'>";
    str += "<h3 class='section-title'>" + s + "</h3>";
    str += "<h4 class='section-year'>" + hackathons[s][4] + "</h4>";
    str += "<h4 class='section-year'>" + hackathons[s][1] + " " + hackathons[s][2]  + "</h4>";
    str += "<a class='button' href='" + hackathons[s][3] + "'target='_blank'> Sign Up </a>";
    str += "</div></div>"
    }
    sponsordivs[0].innerHTML = str;
}