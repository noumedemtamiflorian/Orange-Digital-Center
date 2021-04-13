import './App.css';
import data from "../src/Components/data"
import Logement from "../src/Components/Logement"
import React from 'react';



class App extends React.Component {

  constructor(props) {
    super(props);
    this.state = {
      logements: data.slice(0, 4),
      eltPage: 4,
      pageCurrent: 1,
      title: "Mes Logements"
    }
  }

  changePerPage() {
    this.setState({
      eltPage: parseInt(document.querySelector('select').value),
      pageCurrent: 1,
      logements: data.slice(0, parseInt(document.querySelector('select').value)),
    })
  }

  changeCurrentPage(position) {
    this.setState({
      logements: data.slice((position - 1) * this.state.eltPage, position * this.state.eltPage),
      pageCurrent: position
    })
  }

  get pagination() {
    const nbrBtn = Math.ceil(data.length / this.state.eltPage)
    let btns = []
    let options = [4, 6, 8, 10].map((value) => {
      return <option key={value} > {value}</ option>
    })
    for (let i = 0; i < nbrBtn; i++) {
      btns.push(
        <li key={i}>
          <button onClick={() => this.changeCurrentPage(i + 1)} className={this.state.pageCurrent === (i + 1) ? "btnSelect" : 'btn'}>{i + 1}</button>
        </li>
      )
    }
    return (

      <div id="pagination">
        <select onChange={() => this.changePerPage()}>
          {options}
        </select>
        <ul>
          {btns}
        </ul>
      </div>)
  }

  get logements() {
    return this.state.logements.map((value) => {
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


  render() {
    return (
      <div>
        <header>
          <h1>{this.state.title}</h1>
          <nav>
            <ul>
              <li>nous contacter</li>
              <li>reservation</li>
              <li>reservation</li>
            </ul>
          </nav>
        </header>
        <main>
          <article>
            {this.logements}
          </article>
        </main>
        <footer>
          {this.pagination}
        </footer>
        {this.paginatedModule}
      </div>
    )
  }
}
export default App;