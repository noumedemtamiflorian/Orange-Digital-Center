import Logement from "../Logements/Logement"
const Logements = ({ logements }) => {
    return logements.map((value) => {
        return (<Logement
            key={value.id}
            id={value.id}
            image={value.image}
            type={value.type}
            salon={value.type}
            chambre={value.chambre}
            douche={value.douche}
            terrase={value.terasse}
            loyer={value.loyer}
            etat={value.etat}
        ></Logement>)
    })
}
export default Logements;