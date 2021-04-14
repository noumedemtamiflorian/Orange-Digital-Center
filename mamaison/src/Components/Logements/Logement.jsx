const Logement = ({ id, image, type, salon, chambre, douche, terrase, loyer, etat }) => {

  return (
    <div className="maison">
      <img src={image} alt={image}></img>
      <div id="description">
        <p>ID : <span>{id}</span></p>
        <p>Type : <span>{type}</span> </p>
        <p>Salon : <span>{salon}</span> </p>
        <p>Chambre : <span>{chambre}</span></p>
        <p>Sale De Bain : <span>{douche}</span></p>
        <p>Terrase :  <span>{terrase}</span></p>
        <p>Loyer :  <span>{loyer}</span></p>
        <p>Etat :  <span>{etat}</span></p>
      </div>
    </div>
  )
}
export default Logement;