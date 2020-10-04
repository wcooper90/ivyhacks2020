import React from 'react';
// ,{ useState, useEffect } from 'react';
import './App.css';
import { MetaContainer } from './styles'
import Home from './components/Home'
import Navbar from './components/Navbar'
import {
  Switch,
  Route
} from "react-router-dom"
import About from './components/About';
import Demo from './components/Demo';

import Team from './components/Team';
import Product from './components/Product';
import Signup from './components/Signup';
import Footer from './components/Footer';

// import { API } from  'aws-amplify';

function App() {


  return (
    <MetaContainer>
          <Navbar/>
            <Switch>
             <Route exact path="/" component={Home} />
             <Route path="/demo" component={Demo} />
             <Route path="/about" component={About}  />
             <Route path="/product" component={Product} />
             <Route path="/team" component={Team} />
             <Route path="/signup" component={Signup} />
           </Switch>
      <Footer />
    </MetaContainer>
  );
}

export default App;
