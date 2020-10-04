import React from 'react';
import { Button, Details, Header1, HeaderImage, AboutDescription } from './styles'
import img from '../../notes.svg'


function Home() {

  return (
      <div style={{ width: '100%', minHeight: '65vh', maxWidth: '1024px' }}>
        <AboutDescription>
          <div>
            <Header1>create dynamic summaries like never before.</Header1>
            <Details>Generate rich summaries from news articles, research papers, lecture videos, and other mediums through our
                AI-driven platform.
                </Details>
            <Button>Learn More</Button>
          </div>
          <HeaderImage src = {img} />

        </AboutDescription>
      </div>
  );
}

export default Home
