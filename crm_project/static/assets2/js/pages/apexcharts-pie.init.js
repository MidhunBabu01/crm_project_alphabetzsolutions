var options={series:[44,55,13,43,22],chart:{height:300,type:"pie"},labels:["Team A","Team B","Team C","Team D","Team E"],legend:{position:"bottom"},dataLabels:{dropShadow:{enabled:!1}},colors:["#038edc","#51d28c","#f7cc53","#f34e4e","#564ab1"]},chart=new ApexCharts(document.querySelector("#simple_pie_chart"),options);chart.render();options={series:[44,55,41,17,15],chart:{height:300,type:"donut"},legend:{position:"bottom"},dataLabels:{dropShadow:{enabled:!1}},colors:["#038edc","#51d28c","#f7cc53","#f34e4e","#564ab1"]};(chart=new ApexCharts(document.querySelector("#simple_dount_chart"),options)).render();var options={series:[44,55,13,33],chart:{height:280,type:"donut"},dataLabels:{enabled:!1},legend:{position:"bottom"},colors:["#038edc","#51d28c","#f7cc53","#f34e4e"]},upadatedonutchart=new ApexCharts(document.querySelector("#updating_donut_chart"),options);function appendData(){var e=upadatedonutchart.w.globals.series.slice();return e.push(Math.floor(100*Math.random())+1),e}function removeData(){var e=upadatedonutchart.w.globals.series.slice();return e.pop(),e}function randomize(){return upadatedonutchart.w.globals.series.map(function(){return Math.floor(100*Math.random())+1})}function reset(){return options.series}upadatedonutchart.render(),document.querySelector("#randomize").addEventListener("click",function(){upadatedonutchart.updateSeries(randomize())}),document.querySelector("#add").addEventListener("click",function(){upadatedonutchart.updateSeries(appendData())}),document.querySelector("#remove").addEventListener("click",function(){upadatedonutchart.updateSeries(removeData())}),document.querySelector("#reset").addEventListener("click",function(){upadatedonutchart.updateSeries(reset())});options={series:[44,55,41,17,15],chart:{height:300,type:"donut"},plotOptions:{pie:{startAngle:-90,endAngle:270}},dataLabels:{enabled:!1},fill:{type:"gradient"},legend:{position:"bottom"},title:{text:"Gradient Donut with custom Start-angle",style:{fontWeight:500}},colors:["#038edc","#51d28c","#f7cc53","#f34e4e","#564ab1"]};(chart=new ApexCharts(document.querySelector("#gradient_chart"),options)).render();options={series:[44,55,41,17,15],chart:{height:300,type:"donut",dropShadow:{enabled:!0,color:"#111",top:-1,left:3,blur:3,opacity:.2}},stroke:{width:0},plotOptions:{pie:{donut:{labels:{show:!0,total:{showAlways:!0,show:!0}}}}},labels:["Comedy","Action","SciFi","Drama","Horror"],dataLabels:{dropShadow:{blur:3,opacity:.8}},fill:{type:"pattern",opacity:1,pattern:{enabled:!0,style:["verticalLines","squares","horizontalLines","circles","slantedLines"]}},states:{hover:{filter:"none"}},theme:{palette:"palette2"},title:{text:"Favourite Movie Type",style:{fontWeight:500}},legend:{position:"bottom"},colors:["#038edc","#51d28c","#f7cc53","#f34e4e","#564ab1"]};(chart=new ApexCharts(document.querySelector("#pattern_chart"),options)).render();options={series:[44,33,54,45],chart:{height:300,type:"pie"},colors:["#93C3EE","#E5C6A0","#669DB5","#94A74A"],fill:{type:"image",opacity:.85,image:{src:["./assets/images/auth-bg.jpg","./assets/images/profile-bg.jpg","./assets/images/small/img-5.jpg","./assets/images/small/img-2.jpg"],width:25,imagedHeight:25}},stroke:{width:4},dataLabels:{enabled:!0,style:{colors:["#111"]},background:{enabled:!0,foreColor:"#fff",borderWidth:0}},legend:{position:"bottom"}};(chart=new ApexCharts(document.querySelector("#image_pie_chart"),options)).render();options={series:[25,15,44,55,41,17],chart:{height:300,type:"pie"},labels:["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"],theme:{monochrome:{enabled:!0,color:"#038edc",shadeTo:"light",shadeIntensity:.6}},plotOptions:{pie:{dataLabels:{offset:-5}}},title:{text:"Monochrome Pie",style:{fontWeight:500}},dataLabels:{formatter:function(e,t){return[t.w.globals.labels[t.seriesIndex],e.toFixed(1)+"%"]},dropShadow:{enabled:!1}},legend:{show:!1}};(chart=new ApexCharts(document.querySelector("#monochrome_pie_chart"),options)).render();