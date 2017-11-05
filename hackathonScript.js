var page = require('webpage').create();
var fs = require('fs');

address = "https://mlh.io/seasons/na-2017/events";
page.open(address, function(status) {
    console.log("\n");

    // if (status !== 'success') {
    //     console.log('FAIL to load the address');
    // } else {
    //     console.log('Loading ' + address);

    //     var title = page.evaluate(function() {
    //         return document.getElementsByClassName("event");
    //     });
    //     for(x = 0; x<title.length; x++){
    //         var data = title[x].childNodes[1].textContent.trim().split(/\s+/);
    //         var i = data.indexOf("-");
    //         var name = data.slice(0, i-2).join(" ");
    //         var date = data.slice(i-2, i+2).join(" ");
    //         var loc = data.slice(i+2).join(" ");
    //     }

    //     console.log('Page title is ' + title);
    // }
    // console.log("\n");

    fs.writeFile("nearbyHackathons.txt", "Hey there!", function(err) {
        if(err) {
            return console.log(err);
        }
    
        console.log("The file was saved!");
    }); 

    phantom.exit();
});