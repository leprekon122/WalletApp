// function for diagram on statistics page
function round_diagram(){
     // get all tag_name  form stat_page
     var keys = document.getElementsByClassName('keys')
     // get all sum from stat_page
     var values = document.getElementsByClassName('values')
     // list for all tag
     var keys_set = []
     // list for all sum values
     var keys_values = []
     for(let el = 0; el < keys.length; el++){
        keys_set.push(keys[el].textContent)
     }
     for (let elem = 0; elem < values.length; elem++){
        keys_values.push(values[elem].innerHTML)
     }

     const ctx = document.getElementById('myChart');
      new Chart(ctx, {
        type: 'bar',
        data: {
          labels: keys_set,
          datasets: [{
            label: '# diagram of total values per period',
            data: keys_values,
            borderWidth: 2,
            backgroundColor: [
                        'rgba(82, 235, 52, 0.7)',
                        'rgba(235, 192, 52, 0.9)',
                        'rgba(52, 232, 235, 0.7)'
                    ],
          }]
        },
        options: {
          scales: {
            x: {
                ticks: {
                        color: '#fff' // Light color for x-axis text
                        }
                    },
            y: {
              beginAtZero: true,
              ticks: {
                            color: '#fff' // Light color for y-axis text
                        }
            }
          }
        }
      });
}
round_diagram()