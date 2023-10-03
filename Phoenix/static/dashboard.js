console.log("pink");

var ctx = document.getElementById("line-graph").getContext("2d");
var myChart = new Chart(ctx, {
  type: "line",
  data: {
    labels: [
      "January",
      "February",
      "March",
      "April",
      "May",
      "June",
      "July",
      "August",
      "September",
      "October",
      "November",
      "December",
    ],
    datasets: [
      {
        label: "Dataset 1",
        data: [12, 19, 3, 5, 2, 3, 10, 15, 8, 5, 6, 7],
        backgroundColor: "rgba(255, 99, 132, 0.2)",
        borderColor: "rgba(255, 99, 132, 1)",
        borderWidth: 1,
        fill: false,
        tension: 0.4,
        pointBackgroundColor: "rgba(255, 99, 132, 1)",
        pointBorderColor: "rgba(255, 99, 132, 1)",
        pointRadius: 5,
      },
      {
        label: "Dataset 2",
        data: [5, 10, 15, 10, 20, 15, 25, 20, 15, 10, 5, 10],
        backgroundColor: "rgba(54, 162, 235, 0.2)",
        borderColor: "rgba(54, 162, 235, 1)",
        borderWidth: 1,
        fill: false,
        tension: 0.4,
        pointBackgroundColor: "rgba(54, 162, 235, 1)",
        pointBorderColor: "rgba(54, 162, 235, 1)",
        pointRadius: 5,
      },
      {
        label: "Dataset 3",
        data: [25, 20, 15, 20, 10, 15, 5, 10, 15, 20, 25, 20],
        backgroundColor: "rgba(255, 206, 86, 0.2)",
        borderColor: "rgba(255, 206, 86, 1)",
        borderWidth: 1,
        fill: false,
        tension: 0.4,
        pointBackgroundColor: "rgba(255, 206, 86, 1)",
        pointBorderColor: "rgba(255, 206, 86, 1)",
        pointRadius: 5,
      },
    ],
  },
  options: {
    responsive: true,
    maintainAspectRatio: false,
    scales: {
      y: {
        beginAtZero: true,
      },
    },
    plugins: {
      legend: {
        position: "bottom",
        labels: {
          usePointStyle: true,
        },
      },
    },
  },
});
