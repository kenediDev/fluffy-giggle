import { ConnectedRouter } from "connected-react-router";
import React from "react";
import { useDispatch, useSelector } from "react-redux";
import { Route, Switch } from "react-router-dom";
import Authorization from "../component/authorization";
import HomeComponent from "../component/home";
import Validate from "../component/validate";
import { ApplicationState, history } from "../store/configureStore";
import { UserEnum } from "../store/constant/userTypes";

const Navbar = () => {
  return (
    <div className="noc-navbar">
      <div className="noc-brand">Love</div>
      <div className="noc-input">
        <input type="text" placeholder="Search" />
        <button className="noc-btn-input">
          <i className="fas fa-search"></i>
        </button>
      </div>
      <div className="noc-group">
        <button className="noc-t">Sign in</button>
      </div>
    </div>
  );
};

const Routes: React.FC = () => {
  const dispatch = useDispatch();
  const selector = useSelector((state: ApplicationState) => state);
  React.useEffect(() => {
    if (selector.user.token) {
      localStorage.setItem("token", selector.user.token);
      dispatch({
        type: UserEnum.REVOKE,
      });
      document.location.reload();
    }
  }, [Boolean(selector.user.token)]);

  return (
    <ConnectedRouter history={history}>
      <Navbar />
      <Validate />
      <Switch>
        <Route path="/" exact={true} component={HomeComponent} />
        <Route path="/accounts" component={Authorization} />
      </Switch>
    </ConnectedRouter>
  );
};

export default Routes;
