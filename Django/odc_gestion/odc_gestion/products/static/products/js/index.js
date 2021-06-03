$(document).ready(function () {
});
detailBtn = document.querySelector('#row_table');
detailBtn.onclick = () => {
    console.log("d");
    httpRequest = new XMLHttpRequest();
    httpRequest.onreadystatechange = () => {
        if (httpRequest.readyState === XMLHttpRequest.DONE) {
            if (httpRequest.status === 200) {
                response = httpRequest.responseText
                tbody = document.getElementById("resultDetail")
                console.log(response);
                tbody.innerHTML = "dd";
            } else {
                alert('There was a problem with the request.');
            }
        }
    }
    httpRequest.open('GET', 'http://127.0.0.1:8000/products/1');
    httpRequest.send();
}
