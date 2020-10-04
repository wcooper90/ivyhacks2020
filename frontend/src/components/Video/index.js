import React, { useState, } from 'react';
import { Button, Container } from './styles'

const startText = `https://www.youtube.com/watch?v=3mnSDifDSxQ`


function Text() {


  const [articleURL, setArticleURL] = useState(startText);
  const [summaryText, setSummaryText] = useState("");

  const summarizeText = async text => {
    //const url = 'https://api.smrzr.io/summarize?ratio=0.15'
    const settings = {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(text)
    };

    const response = await fetch('/get_demo', settings);
    const summary = await response.json();
    setSummaryText(summary.output);
  }

    return (
        <div>

          <Container>
            <h2>
              Video input coming Soon !
            </h2>
          </Container>
          <Container>
            <p>
              Enter your video URL into the left hand box and click "Summarize" to see a quick summarization! This demo
              makes a quick call to a backend API which implements a TextRank method to summarize the text. More options
              to come soon!
            </p>
          </Container>
          <br />
          <Container>
            <Button onClick={() => summarizeText(articleURL)}>
               Summarize
            </Button>
          </Container>
          <br />
          <Container>
            <input name='text' cols="120" placeholder="Type or Paste Text..." value={articleURL} onChange={event => setArticleURL(event.currentTarget.value)}></input>
          </Container>
          <Container>
            <textarea rows="25" cols="60" placeholder="Output..." value={summaryText} readOnly></textarea>
          </Container>
        </div>
    );
}

export default Text
