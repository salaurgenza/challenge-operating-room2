<?php
// Connessione al database
$conn = new mysqli("localhost", "tuo_utente", "tua_password", "quiz_db");

// Decodifica i dati JSON
$data = json_decode(file_get_contents("php://input"), true);

// Sanifica e salva
$nome = $conn->real_escape_string($data["nome"]);
$cognome = $conn->real_escape_string($data["cognome"]);
$punteggio = (int)$data["punteggio"];
$dataCompletamento = $conn->real_escape_string($data["dataCompletamento"]);

$sql = "INSERT INTO risposte_quiz (nome, cognome, punteggio, dataCompletamento)
        VALUES ('$nome', '$cognome', $punteggio, '$dataCompletamento')";

if ($conn->query($sql) === TRUE) {
    echo "OK";
} else {
    echo "Errore: " . $conn->error;
}
$conn->close();
?>
