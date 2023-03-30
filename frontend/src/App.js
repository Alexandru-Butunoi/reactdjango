import React from 'react';
import {
  BrowserRouter as Router,
  Switch,
  Route,
} from "react-router-dom";
import Home from './/containers/Home';
import SignIn from './/containers/SignIn';
import SignUp from './/containers/SignUp';
import About from './/containers/About';
import Contact from './/containers/Contact';
import Listings from './/containers/Listings';
import ListingDetail from './/containers/ListingDetail';
import Layout from './/hocs/Layout';
import NotFound from './/components/NotFound';
import './/sass/main.scss';

const App = () => (
    <Router>
        <Layout>
          <Switch>
            <Route exact path='/' componet={Home} />
            <Route exact path='/SignIn' componet={SignIn} />
            <Route exact path='/SignUp' componet={SignUp} />
            <Route exact path='/about' componet={About} />
            <Route exact path='/contact' componet={Contact} />
            <Route exact path='/listings' componet={Listings} />
            <Route exact path='/listings/:id' componet={ListingDetail} />
            <Route componet={NotFound} />
          </Switch>
        </Layout>
    </Router>
);

export default App;
