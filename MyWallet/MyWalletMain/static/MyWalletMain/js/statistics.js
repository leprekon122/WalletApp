var count = 0
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
        type: 'doughnut',
        data: {
          labels: keys_set,
          datasets: [{
            label: '# diagram of total values per period',
            data: keys_values,
            borderWidth: 2,
            backgroundColor: [
                        'rgb(255, 99, 132)',
                        'rgb(54, 162, 235)',
                        'rgb(255, 205, 86)'
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

function round_diagram_full_screen(){
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

     const ctx = document.getElementById('myChart_full_screen');
      new Chart(ctx, {
        type: 'doughnut',
        data: {
          labels: keys_set,
          datasets: [{
            label: '# diagram of total values per period',
            data: keys_values,
            borderWidth: 2,
            backgroundColor: [
                        'rgb(255, 99, 132)',
                        'rgb(54, 162, 235)',
                        'rgb(255, 205, 86)'
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
round_diagram_full_screen()


//function for show or hide diagram button block
function diagram_btn(){
    if (window.screen.width < 500){
        document.getElementById('diagram_btn').style.display = 'block'
        }
}
diagram_btn()

//show hide diagram block
function show_hide_diagram_block(){
    count += 1;
    if(count % 2 == 1){
        document.getElementById('diagram_main_block').style.right = '0px';

    } else{
        document.getElementById('diagram_main_block').style.right = '2000px';
    }
}