<?php
session_start();
require_once 'config.php';

// Check if user is logged in
if (!isset($_SESSION['user_id'])) {
    header("Location: login.php");
    exit;
}

$username = $_SESSION['username'];
$role = $_SESSION['role'];

// Fetch student data
$stmt = $pdo->query("SELECT * FROM stud_info");
$students = $stmt->fetchAll(PDO::FETCH_ASSOC);
?>

<!DOCTYPE html>
<html>
<head>
    <title>Dashboard</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 0; padding: 20px; }
        .container { max-width: 1000px; margin: 0 auto; }
        .header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; }
        .button { background-color: #4CAF50; color: white; padding: 10px 15px; border: none; cursor: pointer; text-decoration: none; display: inline-block; }
        .button-red { background-color: #f44336; }
        table { width: 100%; border-collapse: collapse; }
        table, th, td { border: 1px solid #ddd; }
        th, td { padding: 12px; text-align: left; }
        th { background-color: #f2f2f2; }
        .error { color: red; margin-bottom: 15px; }
        .message { color: green; margin-bottom: 15px; }
        .query-box { margin-top: 20px; padding: 20px; background-color: #f9f9f9; }
        textarea { width: 100%; height: 100px; padding: 8px; margin-bottom: 10px; }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h2>Welcome, <?= htmlspecialchars($username) ?> (<?= htmlspecialchars($role) ?>)</h2>
            <div>
                <?php if ($role === 'admin'): ?>
                    <a href="manage_users.php" class="button">Manage Users</a>
                <?php endif; ?>
                <a href="logout.php" class="button button-red">Logout</a>
            </div>
        </div>
        
        <?php if (isset($_SESSION['message'])): ?>
            <div class="message"><?= $_SESSION['message'] ?></div>
            <?php unset($_SESSION['message']); ?>
        <?php endif; ?>
        
        <?php if (isset($_SESSION['error'])): ?>
            <div class="error"><?= $_SESSION['error'] ?></div>
            <?php unset($_SESSION['error']); ?>
        <?php endif; ?>
        
        <h3>Student Information</h3>
        
        <table>
            <thead>
                <tr>
                    <th>Roll</th>
                    <th>Name</th>
                    <th>Age</th>
                    <th>Branch</th>
                    <th>Hometown</th>
                    <?php if ($role === 'admin' || $role === 'editor'): ?>
                        <th>Actions</th>
                    <?php endif; ?>
                </tr>
            </thead>
            <tbody>
                <?php foreach ($students as $student): ?>
                    <tr>
                        <td><?= htmlspecialchars($student['roll']) ?></td>
                        <td><?= htmlspecialchars($student['name']) ?></td>
                        <td><?= htmlspecialchars($student['age']) ?></td>
                        <td><?= htmlspecialchars($student['branch']) ?></td>
                        <td><?= htmlspecialchars($student['hometown']) ?></td>
                        <?php if ($role === 'admin' || $role === 'editor'): ?>
                            <td>
                                <a href="edit_student.php?roll=<?= $student['roll'] ?>" class="button">Edit</a>
                                <?php if ($role === 'admin'): ?>
                                    <a href="delete_student.php?roll=<?= $student['roll'] ?>" class="button button-red" onclick="return confirm('Are you sure?')">Delete</a>
                                <?php endif; ?>
                            </td>
                        <?php endif; ?>
                    </tr>
                <?php endforeach; ?>
            </tbody>
        </table>
        
        <?php if ($role === 'admin' || $role === 'editor'): ?>
            <p><a href="add_student.php" class="button">Add New Student</a></p>
        <?php endif; ?>
        
        <?php if ($role === 'admin'): ?>
            <div class="query-box">
                <h3>Run SQL Query (Admin Only)</h3>
                <form method="post" action="run_query.php">
                    <textarea name="query" placeholder="Enter your SQL query here"></textarea>
                    <button type="submit" class="button">Run Query</button>
                </form>
            </div>
        <?php endif; ?>
        
        <?php if (isset($_SESSION['query_result']) && $role === 'admin'): ?>
            <div class="query-results">
                <h3>Query Results:</h3>
                <?php if (empty($_SESSION['query_result'])): ?>
                    <p>No results found.</p>
                <?php else: ?>
                    <table>
                        <thead>
                            <tr>
                                <?php foreach ($_SESSION['query_result'][0] as $key => $value): ?>
                                    <th><?= htmlspecialchars($key) ?></th>
                                <?php endforeach; ?>
                            </tr>
                        </thead>
                        <tbody>
                            <?php foreach ($_SESSION['query_result'] as $row): ?>
                                <tr>
                                    <?php foreach ($row as $value): ?>
                                        <td><?= htmlspecialchars($value) ?></td>
                                    <?php endforeach; ?>
                                </tr>
                            <?php endforeach; ?>
                        </tbody>
                    </table>
                <?php endif; ?>
            </div>
            <?php
            unset($_SESSION['query_result']);
            unset($_SESSION['executed_query']);
        endif;
        ?>
    </div>
</body>
</html>
