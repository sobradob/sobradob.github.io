+++
title = "Leaflet timeline in R"
description = "How to make a timeline of GPS measurements."
tags = ["R"]
Categories = ["R","GPS","Android"]
draft = false
date = "2018-02-08T15:52:58+02:00"
series = ["Hacking","Statistics"]

+++

[Leaflet](https://rstudio.github.io/leaflet/) is a powerful tool for visualasing spatial data in R. However, after much googling I could not find an easy way to create a timeline to visualise changes in time. Therefore, I decided to create a simple shiny app that does it.

## Raw Android GPS Movements

### Code
The code below takes raw location measurements from my Android phone visualises them over time. The size of the circle is the confidence interval of the measurement. Before you go and try to find me at those spots, I no longer live there!

``` {app}
# this is a shiny web app. Save as app.r

library(shiny)
library(leaflet)
library(dplyr)

# Define UI for application that draws a map
data<- readRDS("f.rds") # loading the data. It has the timestamp, lon, lat, and the accuracy (size of circles)

ui <- bootstrapPage(
  tags$style(type = "text/css", "html, body {width:100%;height:100%}"),
  leafletOutput("mapAct", width = "100%", height = "100%"),
  absolutePanel(top = 10, right = 10,
  sliderInput("animation", "Time:",
              min = as.POSIXct("2017-02-15 00:00:00",tz = "Europe/Budapest"),
              max = as.POSIXct("2017-02-15 23:59:59",tz = "Europe/Budapest"),
              value = as.POSIXct("2017-02-15 00:00:00",tz = "Europe/Budapest"),
              timezone = "+0200",
              animate =
                animationOptions(interval = 600, loop = TRUE))
  )

  )


# Define server logic required
server <- function(input, output) {
  #stuff in server
  filteredData <- reactive({
    #add rollified thing
    from<- input$animation-90
    till<- input$animation+90
    data %>% filter(time >= from & time <=  till)
  })

  output$mapAct<-renderLeaflet({
    leaflet() %>%
      addTiles() %>%
      addProviderTiles(providers$CartoDB.Positron)%>%
      fitBounds(lng1 = 5,lat1 = 52,lng2 = 5.2,lat2 = 52.2)# set to reactive minimums
  })

  observe({
    leafletProxy("mapAct", data = filteredData()) %>%
      clearShapes() %>%
      addCircles(lng = ~lon, lat = ~lat,
                 radius = ~accuracy, fillOpacity = 0.02,color = "#DF2935")
  })

}

# Run the application
shinyApp(ui = ui, server = server)

```

### App

And this is what the application looks like ( I only start moving around 10 am):

<iframe src="https://sobrado.shinyapps.io/showcase/" style="border: none; width: 650px; height: 900px"></iframe>
