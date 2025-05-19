document.addEventListener("DOMContentLoaded", () => {
    const userList = document.getElementById("userList");
    const userForm = document.getElementById("userForm");

    // Функция загрузки списка пользователей
    function loadUsers() {
        fetch("/api/users")
            .then(response => response.json())
            .then(users => {
                userList.innerHTML = "";
                users.forEach(user => {
                    const li = document.createElement("li");
                    li.innerHTML = `${user.game} (${user.year}) 
                        <button onclick="deleteUser(${user.id})">❌</button>`;
                    userList.appendChild(li);
                });
            });
    }

    // Добавление пользователя
    userForm.addEventListener("submit", event => {
        event.preventDefault();
        const game = document.getElementById("game").value;
        const year = document.getElementById("year").value;

        fetch("/api/users", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ game, year })
        }).then(response => response.json())
          .then(() => {
              userForm.reset();
              loadUsers();
          });
    });

    // Удаление пользователя
    window.deleteUser = (id) => {
        fetch(`/api/users/${id}`, { method: "DELETE" })
            .then(() => loadUsers());
    };

    // Загрузка пользователей при загрузке страницы
    loadUsers();
});
