// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
    apiKey: "AIzaSyBsEp6DgveSe1dJUNAY0zXWjyCokcKrdyQ",
    authDomain: "challenge-operating-room.firebaseapp.com",
    projectId: "challenge-operating-room",
    storageBucket: "challenge-operating-room.firebasestorage.app",
    messagingSenderId: "254422148900",
    appId: "1:254422148900:web:7db06ae37dadd0c2e335b1",
    measurementId: "G-3FM6ZTWVHM"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);