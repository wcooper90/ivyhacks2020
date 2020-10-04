import React, { Component, useState } from 'react';
import { Button, Container } from './styles'
// import axios from 'axios';


function Scan() {
  // <input type="file" onChange={this.onFileChange} />
  //     <button onClick={this.onFileUpload}>
  //       Upload!
  //     </button>


  const [inputFile, setInputFile] = useState([]);
  const [summaryText, setSummaryText] = useState("");

  const onChangeFile = async file => {
    const settings = {
      method: 'POST',
      headers: {
        'Content-Type': 'multipart/form-data',
      },
      body: file
    };

    const response = await fetch('/get_scan', settings);
    const summary = await response.json();
    setSummaryText(summary.output);
  }
    return (
        <div>

          <Container>
            <h2>
              Scanned input coming Soon !
            </h2>
          </Container>
          <Container>
            <p>
              Enter your file below and click "Summarize" to see a quick summarization! This demo
              makes a quick call to a backend API which implements a TextRank method to summarize the text. More options
              to come soon!
            </p>
          </Container>
          <br />
          <Container>
          <input type="file" name="file" onChange={e => onChangeFile(e)}/>


          </Container>
          <br />
          <Container>
            <textarea rows="25" cols="60" placeholder="Output..." value={summaryText} readOnly></textarea>
          </Container>
        </div>
  );
}

export default Scan
