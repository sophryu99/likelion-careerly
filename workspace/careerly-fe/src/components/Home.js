import React, { Component } from "react";
import { Col, Container, Row } from "reactstrap";
import JobList from "./JobList";

import axios from "axios";

import { API_URL } from "../constants";

class Home extends Component {
  // state = {
  //   jobs: []
  // };
  
  constructor (props) {
    super(props)
    this.state = {
      jobs: []
    };
    this.resetState()
  }


  componentDidMount() {
    this.resetState();
  }

  getjobs = () => {
    axios.get(API_URL).then(res => {
      
      this.setState(
        { jobs: res.data })
        // console.log(res.data, "result")
      
      }
        
      );
      
  };
  

  resetState = () => {
    this.getjobs();
  };

  render() {
    return (
      <Container style={{ marginTop: "20px" }}>
        <Row>
          <Col>
            
            <JobList
              jobs = {this.state.jobs.map((item, i) => (
                <div key = {i}>
                  <div>{item.id}</div>
                  <div>{item.jobtitle}</div>
                  <div>{item.company}</div>


                </div>

                ))
                
              }
              resetState={this.resetState}
            />
          </Col>
        </Row>
        <Row>
        </Row>
      </Container>
    );
  }
}

export default Home;
