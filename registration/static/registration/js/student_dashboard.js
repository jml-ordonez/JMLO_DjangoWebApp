async function loadStudents() {
    const loadingMessage =
        document.getElementById("loading-message");

    const errorMessage =
        document.getElementById("error-message");

    const studentCount =
        document.getElementById("student-count");

    const tableBody =
        document.getElementById("student-table-body");

    try {
        loadingMessage.textContent =
            "Loading students...";

        errorMessage.textContent = "";

        const response =
            await fetch("/api/students/");

        if (!response.ok) {
            throw new Error(
                `HTTP error: ${response.status}`
            );
        }

        const data =
            await response.json();

        studentCount.textContent =
            data.count;

        tableBody.innerHTML = "";

        data.students.forEach(student => {

            const row =
                document.createElement("tr");

            row.innerHTML = `
                <td>${student.id}</td>
                <td>${student.student_name}</td>
                <td>${student.program}</td>
                <td>${student.year_level}</td>
                <td>${student.email}</td>
            `;

            tableBody.appendChild(row);
        });

        loadingMessage.textContent = "";

    } catch (error) {

        loadingMessage.textContent = "";

        errorMessage.textContent =
            error.message;

        console.error(
            "Student loading error:",
            error
        );
    }
}

loadStudents();

document
    .getElementById("refresh-students")
    .addEventListener("click", loadStudents);