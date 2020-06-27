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
          method: 'POST', // or 'PUT'
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({'ip_type': 'private'}),
        })
      .then((response) => response.json())
      .then((data) => this.setState({ privateIpAddress: data }));

    fetch('api/ip', {
          method: 'POST', // or 'PUT'
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({'ip_type': 'public'}),
        })
      .then((response) => response.json())
      .then((data) => this.setState({ publicIpAddress: data }));
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