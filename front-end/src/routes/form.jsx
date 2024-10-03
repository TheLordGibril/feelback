import "./form.css"

import RadioGroup from "../components/radiogroup";
import Header from "../components/header"
import Footer from "../components/footer"

import axios from "axios";

import { Link } from "react-router-dom";

export default function Form() {

    
async function post_result() {
  try {
    const response = await axios.post('/api/create-answer/', [
      {
        form: 1,
        question: 1,
        answer: 4,
        customer: 2,
        deleted_at: null
      },
      {
        form: 1,
        question: 2,
        answer: 5,
        customer: 2,
        deleted_at: null
      },
      {
        form: 1,
        question: 3,
        answer: 5,
        customer: 2,
        deleted_at: null
      }
    ]);
    console.log(response.data);
  } catch (error) {
    console.error(error);
  }
}



    return(
        <div className="container-form">
            <Header/>
            <Link to="/" id="home-button" className="link-button">revenir a la page d'accueil</Link>
            <h2>Donner votre avis</h2>
        
            <RadioGroup text="évaluer de 1 a 5 le respect du délai de livraison"/>
            <RadioGroup text="évaluer de 1 a 5 l'état de votre colis a sa réception"/>
            <RadioGroup text="évaluer de 1 a 5 le comportement du livreur"/>

            <button id="send-button" className="link-button" onClick={post_result}>envoyer</button>
            <Footer/>
            
        </div>
    )
}