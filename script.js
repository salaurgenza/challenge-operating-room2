<script type="module">
    // 1. Importa Firebase
  import {initializeApp} from "https://www.gstatic.com/firebasejs/10.12.0/firebase-app.js";
  import {getFirestore, collection, addDoc} from "https://www.gstatic.com/firebasejs/10.12.0/firebase-firestore.js";

  // 2. Configurazione (sostituisci con i tuoi dati reali)
  const firebaseConfig = {
        apiKey: "AIzaSyBsEp6DgveSe1dJUNAY0zXWjyCokcKrdyQ",
    authDomain: "challenge-operating-room.firebaseapp.com",
    projectId: "challenge-operating-room",
    storageBucket: "challenge-operating-room.firebasestorage.app",
    messagingSenderId: "254422148900",
    appId: "1:254422148900:web:7db06ae37dadd0c2e335b1",
    measurementId: "G-3FM6ZTWVHM"
};

  // 3. Inizializza Firebase
  const app = initializeApp(firebaseConfig);
  const db = getFirestore(app);

  // 4. Funzione di salvataggio
  async function salvaRisposteQuiz() {
    // Legge i dati anagrafici dai campi input (assicurati che gli ID siano corretti)
    const nome = document.getElementById("nome").value;
    const cognome = document.getElementById("cognome").value;
    const professione = document.getElementById("professione").value;
    const anniServizio = document.getElementById("anniServizio").value;
    const email = document.getElementById("email").value;

    // Dati del quiz ? adatta queste variabili alla tua logica
    const punteggio = window.punteggioFinale || 0;
    const risposte = window.risposteUtente || [];

    const datiStudente = {
        nome,
        cognome,
        professione,
        anniServizio,
        email,
        punteggio,
        risposte,
        data: new Date()
    };

    try {
        await addDoc(collection(db, "risposteQuiz"), datiStudente);
      alert("Risposte salvate correttamente su Firebase!");
    } catch (e) {
        console.error("Errore durante il salvataggio: ", e);
      alert("Errore nel salvataggio. Riprova.");
    }
  }

  // 5. Rendi la funzione disponibile globalmente
  window.salvaRisposteQuiz = salvaRisposteQuiz;
</script>















