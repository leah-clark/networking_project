import React from 'react';

class IPComponent extends React.Component {

   constructor(props) {
    super(props);

    this.state = {
      privateIpAddress: "",
      publicIpAddress: ""
    };
  }

  componentDidMount() {
    fetch('api/ip', {
          method: 'GET', // or 'PUT'
          headers: {
            'Content-Type': 'application/json',
          }
        })
      .then((response) => response.json())
      .then((data) => this.setState({
          publicIpAddress: data['public'],
          privateIpAddress: data['private']}));
    }

  render() {
      return (
          <div>
              <p>Private IP = {this.state.privateIpAddress}</p>
              <p>Public IP = {this.state.publicIpAddress}</p>
          </div>
        )
      }
}

export default IPComponent;