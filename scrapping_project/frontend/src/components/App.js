import React, { Component, Fragment } from "react";
import ReactDOM from "react-dom";

import Navbar from './layout/Navbar';
import ItemList from './layout/ItemList';

class App extends Component {
  render() {
    return (
      <Fragment>
        <Navbar />
        <ItemList />
      </Fragment>
    );
  }
}


ReactDOM.render(<App />, document.getElementById("app"));