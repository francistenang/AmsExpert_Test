async function getExpertTotalPerMonth () {
        const URL = 'https://bo.amexpert.pro:4443/dashboard/expertencashpermonth'
        const response = await fetch(URL)
        const datapoints = await response.json()
        return datapoints
    }

    getExpertTotalPerMonth().then(amountPerMonth => {
        const months = amountPerMonth.data.map(
            function (index) {
                return index.month
            })
        const total = amountPerMonth.data.map(
            function (index) {
                return index.total
            })
        expertTotalPerMonth.config.data.labels = months
        expertTotalPerMonth.config.data.datasets[0].data  = total
        expertTotalPerMonth.config.data.datasets[0].label = 'Chiffre d\'affaire (€) par mois sur l\'année en cours'
        expertTotalPerMonth.update()
    })


    async function getExpertTotalPerYear () {
        const URL = 'https://bo.amexpert.pro:4443/dashboard/expertencashperyear'
        const response = await fetch(URL)
        const datapoints = await response.json()
        return datapoints
    }

    getExpertTotalPerYear().then(amountPerMonth => {
        const year = amountPerMonth.data.map(
            function (index) {
                return index.year
            })
        const total = amountPerMonth.data.map(
            function (index) {
                return index.total
            })
        expertTotalPerYear.config.data.labels = year
        expertTotalPerYear.config.data.datasets[0].data  = total
        expertTotalPerYear.config.data.datasets[0].label = 'Chiffre d\'affaire (€) par An'
        expertTotalPerYear.update()
    })
    const data = {
    type:'',
    labels: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
    datasets: [{
    label: '',
    data: [18, 12, 6, 9, 12, 3, 9],
    backgroundColor: [
        'rgba(255, 26, 104, 0.2)',
        'rgba(54, 162, 235, 0.2)',
        'rgba(255, 206, 86, 0.2)',
        'rgba(75, 192, 192, 0.2)',
        'rgba(153, 102, 255, 0.2)',
        'rgba(255, 159, 64, 0.2)',
        'rgba(0, 0, 0, 0.2)'
    ],
    borderColor: [
        'rgba(255, 26, 104, 1)',
        'rgba(54, 162, 235, 1)',
        'rgba(255, 206, 86, 1)',
        'rgba(75, 192, 192, 1)',
        'rgba(153, 102, 255, 1)',
        'rgba(255, 159, 64, 1)',
        'rgba(0, 0, 0, 1)'
    ],
    borderWidth: .5
    }]
};

// config 
const config = {
    type: 'bar',
    data,
    options: {
        plugins:{
            legend: {
                display: false
            }
        },
        tooltips: {
            callbacks: {
            label: function(tooltipItem) {
            console.log(tooltipItem)
                return tooltipItem.yLabel;
            }
          }
        },
        responsive: true,
        scales: {
            y: {
                beginAtZero: true,
                maintainAspectRatio: false,
                ticks: {
                    stepSize: 0
                }
            }
        },
    
    }
};
    const expertTotalPerMonth = new Chart(
      document.getElementById('expertTotalPerMonth'),
      config
    );


    const expertTotalPerYear = new Chart(
        document.getElementById('expertTotalPerYear'),
        config
    );