import "./radiogroup.css"

export default function RadioGroup(props) {


    return(
        <div className="container-radiogroup">
            <p id="title-radiogroup">{props.text}</p>
            <div>
                <input type="radio" name="1" id="1" />
                <label htmlFor="1">1</label>
                <input type="radio" name="2" id="2" />
                <label htmlFor="1">2</label>
                <input type="radio" name="3" id="3" />
                <label htmlFor="1">3</label>
                <input type="radio" name="4" id="4" />            
                <label htmlFor="1">4</label>
                <input type="radio" name="5" id="5" />
                <label htmlFor="1">5</label>
            </div>
        </div>
    )
}