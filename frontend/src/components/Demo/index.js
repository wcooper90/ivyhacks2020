import React from 'react';
import { Container, NavItem } from './styles'
import {
  Switch,
  Route,
  Link
} from "react-router-dom"
import Text from '../Text';
import Scan from '../Scan';
import Article from '../Article';
import Video from '../Video';


function Demo() {


    return (
        <div>
          <Container>
            <h2>Demo section</h2>
          </Container>
          <Container>
            <p>
              Pick any of the 4 media types below to get started with summarization!
            </p>
          </Container>
          <Container>
              <Link to='/demo/text'><NavItem>text</NavItem></Link>
              <Link to='/demo/scan'><NavItem>scan</NavItem></Link>
              <Link to='/demo/article'><NavItem>article</NavItem></Link>
              <Link to='/demo/video'><NavItem>video</NavItem></Link>
          </Container>
              <Switch>
               <Route path="/demo/text" component={Text} />
               <Route path="/demo/scan" component={Scan}  />
               <Route path="/demo/article" component={Article} />
               <Route path="/demo/video" component={Video} />
             </Switch>
        </div>
    );
}

export default Demo
