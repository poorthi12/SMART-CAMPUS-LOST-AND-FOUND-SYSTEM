const API = "http://127.0.0.1:8000";

async function reportLost() {
    let data = {
        item_name: document.getElementById("lost_name").value,
        description: document.getElementById("lost_desc").value,
        location: document.getElementById("lost_loc").value,
        owner_name: document.getElementById("lost_owner").value
    };

    let res = await fetch(API + "/lost", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data)
    });

    let result = await res.json();
    alert(result.message);
}

async function reportFound() {
    let data = {
        item_name: document.getElementById("found_name").value,
        description: document.getElementById("found_desc").value,
        location: document.getElementById("found_loc").value,
        finder_name: document.getElementById("found_finder").value
    };

    let res = await fetch(API + "/found", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data)
    });

    let result = await res.json();
    alert(JSON.stringify(result));
}