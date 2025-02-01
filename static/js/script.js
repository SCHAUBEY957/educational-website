document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("registrationForm");

    form.addEventListener("submit", function (event) {
        // Get form values
        let name = document.getElementById("name").value.trim();
        let email = document.getElementById("email").value.trim();
        let mobile = document.getElementById("mobile").value.trim();
        let address = document.getElementById("address").value.trim();
        let college = document.getElementById("college").value.trim();
        let classOption = document.getElementById("class").value;

        // Regex Patterns
        let emailPattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
        let mobilePattern = /^[6-9]\d{9}$/;

        // Validation
        if (name === "" || email === "" || mobile === "" || address === "" || college === "" || classOption === "") {
            alert("⚠️ All fields are required!");
            event.preventDefault();
            return;
        }

        if (!emailPattern.test(email)) {
            alert("⚠️ Enter a valid email address!");
            event.preventDefault();
            return;
        }

        if (!mobilePattern.test(mobile)) {
            alert("⚠️ Enter a valid 10-digit mobile number!");
            event.preventDefault();
            return;
        }

        if (address.length > 100) {
            alert("⚠️ Address must be under 100 characters!");
            event.preventDefault();
            return;
        }

        // Confirmation before submitting
        if (!confirm("Are you sure you want to submit?")) {
            event.preventDefault();
        }
    });

    // Live character count for address field
    document.getElementById("address").addEventListener("input", function () {
        let charCount = this.value.length;
        document.getElementById("charCount").textContent = `${charCount}/100`;
    });
});
