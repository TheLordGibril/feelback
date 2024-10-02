import "./header.css"
import logo from "../assets/logo.png"

export default function header() {

    return (
        <div className="container-header">
            <img src={logo} alt="" />
            <h2 id="title">FeelBack</h2>
            <h4 id="subtitle">Le questionnaire de satisfaction</h4>
        </div>
    )
}