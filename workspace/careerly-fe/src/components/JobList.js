import React, { Component } from "react";

class JobList extends Component {
  render() {
    const jobs = this.props.jobs;
    return (
        <h1> {jobs} </h1>
    )
  }
}

export default JobList;