+++
date = "2017-08-18T22:22:16-08:00"
draft = false
title = "Costa Rican Saints"
tags = ["R","Shiny","Costa Rica"]
Categories = ["R","Shiny","Costa Rica","Latin America"]
series = "hacking"
+++

One of the first things a traveller notices when going to Costa Rica is that almost every town or city is named after a Saint. Growing up in Costa Rica, I just assumed this was something true of all Latin American countries, a legacy of Spanish colonial times. California has San Jose, San Fransisco, etc. I thought it was like that from California to Argentina.

After some travelling in Latin America I realised this was simply not true. Cuba is exceptionally adept at original names (e.g. Guantanamo). Even neighbouring Nicaragua seemed to have more varied names. It turns out Costa Ricans are particularly unoriginal with names, after all approximately 10% of the population's last name is [Rodriguez, Vargas, Jimenez, Mora or Rojas](http://forebears.io/costa-rica#surnames). Similarly, 16% of all locations were named after a saint.

As an exercise, I built a [Shiny app](http://shiny.rstudio.com/) to explore all the towns with holy names, that is towns that contain "San" or "Santa" using data provided by the wonderful team at [El Estado de la Nacion](http://www.estadonacion.or.cr/). Handsome sociologist [Miguel Sobrado](http://miguelsobrado.com/) (full disclosure: he is also my grandfather) pointed out that the places with Saint in the name seem to cluster in the Central Valley and in lands later colonised by Central Valley residents.

You can see the app below. It is on limited free hosting though, so it might not be available if someone spends too long on it. The menu is on the top left, the three parallel lines.

<iframe src="https://sobrado.shinyapps.io/CostaRica/" style="border: none; width: 650px; height: 900px"></iframe>
