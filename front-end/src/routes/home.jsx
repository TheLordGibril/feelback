import "./home.css"
import Header from "../components/header"
import Footer from "../components/footer"


import { Link } from "react-router-dom";

export default function home() {

    return (
        <div className="container-home">
            <Header/>
            <Link to="/dashboard" id="dashboard-button" className="link-button">consulter le tableau de bord</Link>
            <h3 id="home-title">Bienvenue sur l'application FeelBack</h3>
            <p id="home-subtitle">Cette application vous permet d'évaluer la livraison de vote commande</p>
            <Link to="form" id="form-button" className="link-button">créer une commande fictive et remplir le questionnaire de satisfaction</Link>
            <Footer/>
        </div>
    )
}