import "./radiogroup.css"

export default function RadioGroup(props) {
    console.log("a")

    const handleLocalChange = (event) => {
        props.handleChange(props.name,event.target.id)
    };

    return(
        <div className="container-radiogroup">
            <p id="title-radiogroup">{props.text}</p>
            <div id="container-radio">
                <input type="radio" name={props.name} id="1" onChange={handleLocalChange}/>
                <label htmlFor="1">1</label>
                <input type="radio" name={props.name} id="2" onChange={handleLocalChange} />
                <label htmlFor="1">2</label>
                <input type="radio" name={props.name} id="3" onChange={handleLocalChange} />
                <label htmlFor="1">3</label>
                <input type="radio" name={props.name} id="4" onChange={handleLocalChange} />            
                <label htmlFor="1">4</label>
                <input type="radio" name={props.name} id="5" onChange={handleLocalChange} />
                <label htmlFor="1">5</label>
            </div>
        </div>
    )
}