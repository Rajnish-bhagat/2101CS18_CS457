<?php
session_start();
require_once 'config.php';

// Check if user is logged in and has appropriate role
if (!isset($_SESSION['user_id']) || ($_SESSION['role'] !== 'admin' && $_SESSION['role'] !== 'editor')) {
    $_SESSION['error'] = "You don't have permission to add students";
    header("Location: dashboard.php");
    exit;
}

// Process form submission
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $roll = $_POST['roll'];
    $name = $_POST['name'];
    $age = $_POST['age'];
    $branch = $_POST['branch'];
    $hometown = $_POST['hometown'];
    
    $stmt = $pdo->prepare("INSERT INTO stud_info (roll, name, age, branch, hometown) VALUES (?, ?, ?, ?, ?)");
    $stmt->execute([$roll, $name, $age, $branch, $hometown]);
    
    $_SESSION['message'] = "Student added successfully";
    header("Location: dashboard.php");
    exit;
}
?>

<!DOCTYPE html>
<html>
<head>
    <title>Add Student</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 0; padding: 20px; }
        .container { max-width: 500px; margin: 0 auto; }
        .form-group { margin-bottom: 15px; }
        label { display: block; margin-bottom: 5px; }
        input { width: 100%; padding: 8px; }
        .button { background-color: #4CAF50; color: white; padding: 10px 15px; border: none; cursor: pointer; }
    </style>
</head>
<body>
    <div class="container">
        <h2>Add New Student</h2>
        <form method="post">
            <div class="form-group">
                <label for="roll">Roll Number</label>
                <input type="number" id="roll" name="roll" required>
            </div>
            
            <div class="form-group">
                <label for="name">Name</label>
                <input type="text" id="name" name="name" required>
            </div>
            
            <div class="form-group">
                <label for="age">Age</label>
                <input type="number" id="age" name="age">
            </div>
            
            <div class="form-group">
                <label for="branch">Branch</label>
                <input type="text" id="branch" name="branch">
            </div>
            
            <div class="form-group">
                <label for="hometown">Hometown</label>
                <input type="text" id="hometown" name="hometown">
            </div>
            
            <button type="submit" class="button">Add Student</button>
        </form>
        <p><a href="dashboard.php">Back to Dashboard</a></p>
    </div>
</body>
</html>
