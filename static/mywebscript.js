let RunEmotionDetection = ()=>{
    textToAnalyze = document.getElementById("textToAnalyze").value;

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status != 0) {
            document.getElementById("system_response").innerHTML = xhttp.responseText;
        }
    };
    
    console.log("UNSENT: ", xhttp.status);
    console.log("RES", xhttp.responseText);

    xhttp.open("GET", "emotionDetector?textToAnalyze"+"="+textToAnalyze, true);
    
    console.log("OPENED: ", xhttp.status);
    console.log("RES", xhttp.responseText);
    
    xhttp.onprogress = () => {
        console.log("LOADING: ", xhttp.status);
        console.log("RES", xhttp.responseText);
    };

    xhttp.onload = () => {
        console.log("DONE: ", xhttp.status);
        console.log("RES", xhttp.responseText);
    };
    
    xhttp.send();
    console.log("RES", xhttp.responseText);

}
