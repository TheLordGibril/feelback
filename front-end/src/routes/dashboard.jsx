import Header from "../components/header"
import Footer from "../components/footer"

import "./dashboard.css"

import { Link } from "react-router-dom"

export default function Dashboard() {

    return(
        <div className="container-dashboard">
            <Header/>
            <Link to="/" id="home-button" className="link-button">revenir a la page d'accueil</Link>
            <h2>Tableau de bord</h2>
            <p>Cette page regroupe des statistiques moyennes sur l'ensemble des réponses données</p>

            <div id="container-stats">
                <div className="total-answers">
                    <p className="stat">6</p>
                    <p className="text">Réponses</p>
                </div>
                <div className="delivery-delay">
                    <p className="stat">4.37 / 5</p>
                    <p className="text">Délai de livraison</p>
                </div>
                <div className="package-state">
                    <p className="stat">4.66 / 5</p>
                    <p className="text">Etat du colis</p>
                </div>
                <div className="deliverer-behavior">
                    <p className="stat">3.80 / 5</p>
                    <p className="text">Comportement du livreur</p>
                </div>
            </div>
            <Footer/>
        </div>
    )
}