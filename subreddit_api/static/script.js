// subreddit_api/static/script.js
/*const threadsContainer = document.getElementById('threads-container');

fetch('/subreddit_api/threads/')
    .then(response => response.json())
    .then(data => {
        data.forEach(thread => {
            const threadDiv = document.createElement('div');
            threadDiv.innerHTML = `
                <h2>${thread.title}</h2>
                <p>Author: ${thread.author}</p>
                <p>Creation Date: ${new Date(thread.creation_date * 1000).toLocaleString()}</p>
                <a href="${thread.link}" target="_blank">Original Thread</a>
                <hr>
            `;
            threadsContainer.appendChild(threadDiv);
        });
    })
    .catch(error => console.error('Error fetching data:', error));*/
