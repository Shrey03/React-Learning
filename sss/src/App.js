import logo from "./logo.svg";
import React, { Component } from "react";
import "./App.css";

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      counter: 42,
    };
  }
  incrementCounter = () => {
    this.setState({ counter: this.state.counter + 1 });
  };
  render() {
    return (
      <div>
        <h2>{this.state.counter}</h2>
        <button onClick={this.incrementCounter}>Click</button>
      </div>
    );
  }
}

export default App;
