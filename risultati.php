<?php
$conn = new mysqli("localhost", "tuo_utente", "tua_password", "quiz_db");
$sql = "SELECT nome, cognome, punteggio, dataCompletamento FROM risposte_quiz ORDER BY dataCompletamento DESC";
$result = $conn->query($sql);
?>

<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Risultati Quiz</title>
    <style>
        table { width: 80%; margin: auto; border-collapse: collapse; }
        th, td { padding: 10px; border: 1px solid #ccc; text-align: center; }
        th { background-color: #f0f0f0; }
    </style>
</head>
<body>
    <h2 style="text-align:center;">Risultati Quiz</h2>
    <table>
        <thead>
            <tr><th>Nome</th><th>Cognome</th><th>Punteggio</th><th>Data</th></tr>
        </thead>
        <tbody>
            <?php while ($row = $result->fetch_assoc()): ?>
            <tr>
                <td><?= htmlspecialchars($row['nome']) ?></td>
                <td><?= htmlspecialchars($row['cognome']) ?></td>
                <td><?= $row['punteggio'] ?></td>
                <td><?= $row['dataCompletamento'] ?></td>
            </tr>
            <?php endwhile; ?>
        </tbody>
    </table>
</body>
</html>
