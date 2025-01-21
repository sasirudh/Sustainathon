library(shiny)
library(ggplot2)
library(DT)

# Load Data 
data <- read.csv("sample_data.csv")

# Ensure Required Columns Exist
if (!("total_score" %in% colnames(data)) || !("mood" %in% colnames(data))) {
  stop("Required columns 'total_score' or 'mood' are missing.")
}

# Function to Classify Depression Severity
classify_severity <- function(score) {
  if (score >= 1 & score <= 4) {
    return("Minimal depression")
  } else if (score >= 5 & score <= 9) {
    return("Mild depression")
  } else if (score >= 10 & score <= 14) {
    return("Moderate depression")
  } else if (score >= 15 & score <= 19) {
    return("Moderately severe depression")
  } else if (score >= 20 & score <= 27) {
    return("Severe depression")
  } else {
    return(NA)
  }
}

# Add Severity Classification to Data
data$Severity <- sapply(data$total_score, classify_severity)

# UI for Shiny App
ui <- fluidPage(
  titlePanel("Mood-Based Dashboard"),
  
  sidebarLayout(
    sidebarPanel(
      selectInput("mood_filter", "Select Mood:", 
                  choices = unique(data$mood), 
                  selected = unique(data$mood)[1])
    ),
    
    mainPanel(
      tabsetPanel(
        tabPanel("Depression Severity",
                 textOutput("average_score"),
                 tableOutput("severity_table")
        ),
        tabPanel("Visualizations",
                 plotOutput("mood_bar"),
                 plotOutput("mood_pie"),
                 plotOutput("scatter_plot")
        ),
        tabPanel("Time Series",
                 plotOutput("time_series")
        ),
        tabPanel("Raw Data", DTOutput("data_table"))
      )
    )
  )
)

# Server Logic for Shiny App
server <- function(input, output, session) {
  
  # Reactive Data Filtering
  filtered_data <- reactive({
    req(input$mood_filter)
    filtered <- data[data$mood == input$mood_filter, ]
    if (nrow(filtered) == 0) {
      return(data.frame()) # Return an empty data frame
    }
    return(filtered)
  })
  
  # Average Total Score
  output$average_score <- renderText({
    if (nrow(filtered_data()) == 0) {
      return(paste("No data available for mood:", input$mood_filter))
    }
    avg_score <- mean(filtered_data()$total_score, na.rm = TRUE)
    paste("Average Total Score for", input$mood_filter, ":", round(avg_score, 2))
  })
  
  # Severity Table
  output$severity_table <- renderTable({
    if (nrow(filtered_data()) == 0) {
      return(data.frame(Severity = "No Data", Count = 0))
    }
    severity_counts <- table(filtered_data()$Severity)
    data.frame(Severity = names(severity_counts), Count = as.numeric(severity_counts))
  })
  
  # Bar Chart: Counts of Each Mood
  output$mood_bar <- renderPlot({
    ggplot(data, aes(x = mood)) +
      geom_bar(fill = "steelblue") +
      theme_minimal() +
      labs(title = "Mood Distribution", x = "Mood", y = "Count")
  })
  
  # Pie Chart: Proportions of Each Mood
  output$mood_pie <- renderPlot({
    mood_counts <- data.frame(table(data$mood))
    colnames(mood_counts) <- c("mood", "count")
    ggplot(mood_counts, aes(x = "", y = count, fill = mood)) +
      geom_bar(stat = "identity", width = 1) +
      coord_polar("y") +
      theme_void() +
      labs(title = "Mood Proportions")
  })
  
  # Scatter Plot: Relationship Between Variables
  output$scatter_plot <- renderPlot({
    ggplot(filtered_data(), aes(x = variable1, y = variable2)) + 
      geom_point(aes(color = mood), size = 3) + 
      theme_minimal() + 
      labs(title = paste("Scatter Plot for Mood:", input$mood_filter),
           x = "Variable 1", y = "Variable 2")
  })
  
  # Time Series Plot
  output$time_series <- renderPlot({
    if ("timestamp" %in% colnames(data)) {
      ggplot(filtered_data(), aes(x = as.Date(timestamp), y = variable1)) +
        geom_line(color = "darkorange", size = 1) +
        theme_minimal() +
        labs(title = "Time Series Plot", x = "Date", y = "Variable 1")
    } else {
      plot.new()
      title("No Timestamp Column Found")
    }
  })
  
  # Raw Data Table Output
  output$data_table <- renderDT({
    datatable(filtered_data())
  })
}

# Run the Shiny App
shinyApp(ui, server)


