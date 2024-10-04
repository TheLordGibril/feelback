import Header from "../components/header"
import Footer from "../components/footer"

import { useEffect, useState } from "react"

import "./dashboard.css"

import { Link } from "react-router-dom"

export default function Dashboard() {

    const [stats, setStats] = useState(null);

    useEffect(() => {
      fetch('http://127.0.0.1:8000/api/answer-stats/?format=json')
        .then(response => response.json())
        .then(json => setStats(json))
        .catch(error => console.error(error));
    }, []);

    return(
        <div className="container-dashboard">
            <Header/>
            <Link to="/" id="home-button" className="link-button">revenir a la page d'accueil</Link>
            <h2>Tableau de bord</h2>
            <p>Cette page regroupe des statistiques moyennes sur l'ensemble des réponses données</p>
                
            <div id="container-stats">
                <div className="total-answers">
                    <p className="stat">{stats ? stats[0]["nb_submissions"] : "undefined"}</p>
                    <p className="text">Réponses</p>
                </div>
                <div className="delivery-delay">
                    <p className="stat">{stats? stats[0]["avg_answer"].toFixed(1) : "undefined"} / 5</p>
                    <p className="text">Délai de livraison</p>
                </div>
                <div className="package-state">
                    <p className="stat">{stats? stats[1]["avg_answer"].toFixed(1) : "undefined"} / 5</p>
                    <p className="text">Etat du colis</p>
                </div>
                <div className="deliverer-behavior">
                    <p className="stat">{stats? stats[2]["avg_answer"].toFixed(1) : "undefined"} / 5</p>
                    <p className="text">Comportement du livreur</p>
                </div>
            </div>
            <Footer/>
        </div>
    )
}