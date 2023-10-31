// import logo from './logo.svg';
import { useState, useContext, createContext } from 'react';
import './App.css';
import 'bootstrap/dist/css/bootstrap.css';
import Login from './components/Login/Login';
import Header from './Header/Header';
import Main from './Main';
function App() {
  const initLoginState = {
    access_token: localStorage.getItem('access_token') ? localStorage.getItem('access_token') : null,
    expiration_datetime: localStorage.getItem("expiration_datetime") ? localStorage.getItem("expiration_datetime") : null,
    isLogin: localStorage.getItem('isLogin') ? localStorage.getItem('isLogin') : false,
    isAdmin: localStorage.getItem('isAdmin') ? localStorage.getItem('isAdmin') : true
  }
  const [loginState, setLoginState] = useState(initLoginState)
  const LoginContext = createContext(loginState)
  return (
    <div>
      <LoginContext.Provider value={loginState}>
        <Header admin={true} show={loginState.isLogin} />
        <Login show={!loginState.isLogin || (Date.now() > Date.parse(loginState.expiration_datetime))} setLoginState={setLoginState} />
        <Main show={loginState.isLogin} />
      </LoginContext.Provider>
    </div>
  )
}

export default App;
