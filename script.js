async function uploadData() {
    const fileInput = document.getElementById("dataFile");
    const file = fileInput.files[0];
    
    if (!file) {
        alert("Please select a CSV file to upload.");
        return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {
        const response = await fetch("http://127.0.0.1:5000/upload", {
            method: "POST",
            body: formData
        });
        
        const result = await response.json();

        if (response.ok) {
            document.getElementById("statusText").textContent = "File uploaded successfully!";
            console.log("Upload success:", result);
        } else {
            document.getElementById("statusText").textContent = `Upload failed: ${result.error}`;
            console.error("Upload failed:", result.error);
        }
    } catch (error) {
        document.getElementById("statusText").textContent = "An error occurred during upload.";
        console.error("Upload error:", error);
    }
}

async function sendEmails() {
    const emailSubject = document.getElementById("emailSubject").value;
    const emailBody = document.getElementById("emailBody").value;
    const emailPrompt = document.getElementById("emailPrompt").value;

    if (!emailSubject || !emailBody || !emailPrompt) {
        alert("Please complete all fields in the email customization section.");
        return;
    }

    const emailData = {
        subject: emailSubject,
        body: emailBody,
        prompt: emailPrompt
    };

    try {
        const response = await fetch("http://127.0.0.1:5000/send_emails", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(emailData)
        });

        const result = await response.json();

        if (response.ok) {
            document.getElementById("statusText").textContent = "Emails sent successfully!";
            console.log("Emails sent:", result);
        } else {
            document.getElementById("statusText").textContent = `Sending failed: ${result.error}`;
            console.error("Sending failed:", result.error);
        }
    } catch (error) {
        document.getElementById("statusText").textContent = "An error occurred while sending emails.";
        console.error("Send error:", error);
    }
}
