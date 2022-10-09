import Navbar from './components/navbar/Navbar';
import './App.scss';
import {Routes, Route} from 'react-router-dom';
import HomeContainer from './components/containers/HomeContainer';
import * as Constants from './Constants';
import IndicatorContainer from './components/containers/IndicatorContainer';

function App() {
  return (
  <>
      <Navbar/>
      <Routes>
        <Route path={Constants.HOME_ROUTE} exact element={HomeContainer}/>
        <Route path={Constants.INDICATOR_ROUTE} exact element={IndicatorContainer}/>
        <Route path={Constants.RELATIONS_ROUTE} exact element={IndicatorContainer}/>
        <Route path={Constants.ENVIRONMENT_ROUTE} exact element={IndicatorContainer}/>

      </Routes>
  </>
  );
}

export default App;
