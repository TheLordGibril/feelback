import "./form.css"

import RadioGroup from "../components/radiogroup";
import Header from "../components/header"
import Footer from "../components/footer"

import { Link } from "react-router-dom";

export default function Form() {

    return(
        <div className="container-form">
            <Header/>
            <Link to="/" id="home-button" className="link-button">revenir a la page d'accueil</Link>
            <h2>Donner votre avis</h2>

            <RadioGroup text="évaluer de 1 a 5 le respect du délai de livraison"/>
            <RadioGroup text="évaluer de 1 a 5 l'état de votre colis a sa réception"/>
            <RadioGroup text="évaluer de 1 a 5 le comportement du livreur"/>

            <button id="send-button" className="link-button">envoyer</button>
            <Footer/>
            
        </div>
    )
}