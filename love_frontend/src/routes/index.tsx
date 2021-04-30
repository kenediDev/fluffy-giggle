import React from "react";
import { Route, Switch } from "react-router-dom";
import HomeComponent from "../component/home";

const Routes = () => {
  return (
    <Switch>
      <Route path="/" exact={true} component={HomeComponent} />
    </Switch>
  );
};

export default Routes;
