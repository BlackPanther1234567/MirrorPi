function updateTime() {
  document.getElementById("time").innerText = new Date().toLocaleTimeString();
}
setInterval(updateTime, 1000);

async function fetchData(endpoint, id) {
  try {
    const res = await fetch(endpoint);
    const data = await res.json();
    document.getElementById(id).innerText = JSON.stringify(data, null, 2);
  } catch (err) {
    document.getElementById(id).innerText = "Error loading " + id;
  }
}

fetchData("/api/weather", "weather");
fetchData("/api/timetable", "timetable");
fetchData("/api/exams", "exams");
