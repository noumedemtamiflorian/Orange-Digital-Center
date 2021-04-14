const Pagination = () => {
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

export default Pagination;