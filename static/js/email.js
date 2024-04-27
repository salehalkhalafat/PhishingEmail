let phinsingemail = document.getElementById("hint-phishingemail");
//function addEmailDetails(email, subject, body) {
//  const url = "http://localhost:8000/add_email/";
//  const data = { email, subject, body };
//
//  fetch(url, {
//    method: "POST",
//    headers: {
//      "Content-Type": "application/json",
//      'Authorization', 'Bearer yourAccessToken',
//    },
//    body: JSON.stringify(data),
//  })
//    .then((response) => response.json())
//    .then((data) => {
//      console.log("Success:", data);
//    })
//    .catch((error) => {
//      console.error("Error:", error);
//    });
//}

function fetchEmail() {
  fetch("http://127.0.0.1:8000/fetchem/")
    .then((response) => {
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      return response.json();
    })
    .then((data) => {
      if (data.status) {
        phinsingemail.style.display = "block";
        let senderelemnt = document.getElementById("sender");
        let subjectelemt = document.getElementById("Subject");
        let HTMLELEM = document.getElementById("Plain_HTML");

        senderelemnt.textContent = data.data.sender;
        subjectelemt.textContent = data.data.Subject;
        HTMLELEM.innerHTML = data.data.Plain_HTML;
//        addEmailDetails(
//          data.data.sender,
//          data.data.Subject,
//          data.data.Plain_HTML
//        );
      }
    })
    .catch((error) => {
      console.error("There was a problem with the fetch operation:", error);
    });
}

setInterval(fetchEmail, 1000);
