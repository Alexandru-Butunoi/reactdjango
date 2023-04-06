import React from 'react';
import {
  BrowserRouter as Router,
  Routes,
  Route,
} from "react-router-dom";
import Home from './components/Home';
import SignIn from './components/SignIn';
import SignUp from './components/SignUp';
import About from './components/About';
import Contact from './components/Contact';
import Listings from './components/Listings';
import ListingDetail from './components/ListingDetail';
import Layout from './components/Layout';
import NotFound from './components/NotFound';
import './sass/main.scss';

import { Provider } from 'react-redux';
import store from './store';

const App = () => (
    <Provider store={(store)}>
		<Router>
			<Layout>
				<Routes>
					<Route exact path='/' element={<Home/>}/>
					<Route exact path='/about' element={<About/>}/>
					<Route exact path='/contact' element={<Contact/>}/>
					<Route exact path='/listings' element={<Listings/>}/>
					<Route exact path='/listings/:id' element={<ListingDetail/>}/>
					<Route exact path='/login' element={<SignIn/>}/>
					<Route exact path='/signup' element={<SignUp/>}/>
					<Route path='*' element={<NotFound />} />
              	</Routes>
          	</Layout>
      	</Router>
	</Provider>
);

export default App;
