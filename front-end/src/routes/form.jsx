import "./form.css"

import RadioGroup from "../components/radiogroup";
import Header from "../components/header"
import Footer from "../components/footer"

import React from "react";
import axios from "axios";

import { Link } from "react-router-dom";

export default function Form() {

    const [formState, setFormState] = React.useState({
        delay: 3,
        state: 3,
        behavior: 3
    });

    function test(name, value) {
        setFormState(prevState => ({
            ...prevState,
            [name]: value
        }));
    
        console.log(name, value); 
    }
    

    async function post_result() {
        try {
            const response = await axios.post('/api/create-answer/', [
                {
                    form: 1,
                    question: 1,
                    answer: formState.delay,
                    customer: 4,
                    deleted_at: null
                },
                {
                    form: 1,
                    question: 2,
                    answer: formState.state,
                    customer: 4,
                    deleted_at: null
                },
                {
                    form: 1,
                    question: 3,
                    answer: formState.behavior,
                    customer: 4,
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
            <Link to="/" id="home-button" className="link-button">revenir a la page daccueil</Link>
            <h2 id="opinion">Donner votre avis</h2>
        
            <RadioGroup handleChange={test} text="évaluer de 1 a 5 le respect du délai de livraison" name="delay"/>
            <RadioGroup handleChange={test} text="évaluer de 1 a 5 l'état de votre colis a sa réception" name="state"/>
            <RadioGroup handleChange={test} text="évaluer de 1 a 5 le comportement du livreur" name="behavior"/>

            <button id="send-button" className="link-button" onClick={post_result}>envoyer</button>
            <Footer/>
            
        </div>
    )
}