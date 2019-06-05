/*
Template Name: Material Pro Admin
Author: Themedesigner
Email: niravjoshi87@gmail.com
File: js
*/
$(function () {
    "use strict";
    // ==============================================================
    // Sales overview
    // ==============================================================
    var chart2 = new Chartist.Bar('.amp-pxl', {
          labels: ['Mon', 'Tue', 'Wed', 'Thu'],
          series: [
            [9, 5, 3, 7],
            [6, 3, 9, 5]
          ]
        }, {
          axisX: {
            // On the x-axis start means top and end means bottom
            position: 'end',
            showGrid: false
          },
          axisY: {
            // On the y-axis start means left and end means right
            position: 'start'
          },
        high:'12',
        low: '0',
        plugins: [
            Chartist.plugins.tooltip()
        ]
    });


});
