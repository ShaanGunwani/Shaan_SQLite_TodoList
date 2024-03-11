import { initializeApp } from "firebase/app";
import { getDatabase } from "firebase/database";
import { getAuth } from "firebase/auth";

const firebaseConfig = {
  apiKey: "AIzaSyB3q1c9TBKfV2L3i2G9ZA8ufNarJRcDJps",
  authDomain: "todoapp-shaan-gunwani.firebaseapp.com",
  databaseURL: "https://todoapp-shaan-gunwani-default-rtdb.asia-southeast1.firebasedatabase.app",
  projectId: "todoapp-shaan-gunwani",
  storageBucket: "todoapp-shaan-gunwani.appspot.com",
  messagingSenderId: "892884530152",
  appId: "1:892884530152:web:ed6738a6a0c88f1a22aa5d"
};

const app = initializeApp(firebaseConfig);
export const db = getDatabase(app);
export const auth = getAuth();
