import React, { Component } from "react";

class JobList extends Component {
  render() {
    const jobs = this.props.jobs;
    console.log("Joblist test")
    return <>
        Text
    

        <h1> {jobs} </h1>
        
    </>
  }
}

export default JobList;