document.querySelectorAll('.nested-lists a').forEach(link => {
    link.addEventListener('click', function (event) {
        event.preventDefault(); // Prevent default link behavior
        const iframe = document.getElementById('iframe');
        const message = document.getElementById('message');
        const href = this.getAttribute('href');

        // Display loading message
        message.textContent = 'Please wait, page is loading...';
        iframe.style.display = 'none';
        message.style.display = 'block';

        // Try to load the link in the iframe
        iframe.src = href;

        iframe.onload = function () {
            message.style.display = 'none';
            iframe.style.display = 'block';
        };

        iframe.onerror = function () {
            message.textContent = 'Link broken.';
            iframe.style.display = 'none';
        };
    });
});
