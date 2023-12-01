<?php
// Check if the parameters are provided
if (isset($_GET['firstname']) && isset($_GET['lastname'])) {
    // Retrieve the values of the parameters
    $firstname = $_GET['firstname'];
    $lastname = $_GET['lastname'];

    // Print the welcome message
    echo "Hello, $firstname $lastname. Welcome to Sparrow!";
} else {
    // Print an error message if parameters are missing
    echo "Error: Please provide both 'firstname' and 'lastname' parameters.";
}
?>
