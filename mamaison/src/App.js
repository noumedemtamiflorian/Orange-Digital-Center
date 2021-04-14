import './App.css';
import data from "./Components/data/data"
import Logements from "./Components/Logements/Logements"
import React from 'react';
import 'antd/dist/antd.css';
import { Pagination } from "antd"

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

  handleChange = value => {
    const { eltPage } = this.state;
    const indexOfLastLog = value * eltPage;
    const indexOfFirstLog = indexOfLastLog - eltPage;
    this.setState({
      currentPage: value,
      logements: data.slice(indexOfFirstLog, indexOfLastLog)
    });
  };

  handleSelectChange = e => {
    this.setState({
      eltPage: e.target.value,
      pageCurrent: 1,
      logements: data.slice(0, e.target.value)
    });
  };

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
            <Logements logements={this.state.logements}></Logements>
          </article>
        </main>
        <footer className="pagination_div">
          <Pagination
            defaultCurrent={this.state.pageCurrent}
            defaultPageSize={this.state.eltPage} //default size of page
            pageSize={this.state.eltPage}
            onChange={this.handleChange}
            total={/*loadingOk && */data.length > 0 && data.length} //total number of card data available
          />
          <select value={this.state.eltPage} onChange={this.handleSelectChange}>
            <option>2</option>
            <option>3</option>
            <option>4</option>
          </select>
        </footer>
      </div>
    )
  }
}

export default App;