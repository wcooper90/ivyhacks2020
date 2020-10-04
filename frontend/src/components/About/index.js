import React  from 'react';
import { Container } from './styles'


function About() {

    return (
      <Container>
        <div className="nine columns main-col">
           <h2>About</h2>

           <p>The availability of information is now greater than ever with the internet. Webinars and free lecture series have made learning new and front line research drastically easier. Despite this, many of us still find ourselves with a shortage of time or motivation to be watching long, educational videos, or to read through descriptive and boring articles or research papers. As the demand for interesting yet concise information rises, natural language processing for information aggregation will become one of the most powerful tools available to curious learners and researchers. The app idea - makes use of web scraping techniques in conjunction with the most recent text summarization machine learning frameworks to allow for various inputs and various outputs. Inputs would include a webinar URL, a Wikipedia article, or a chunk of text, while outputs would include basic summarizations, interactive/dynamic summarizations, and potentially even dashboards or infographics. </p>

        </div>
      </Container>

    );
}

export default About;
