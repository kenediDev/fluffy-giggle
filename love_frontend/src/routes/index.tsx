import { ConnectedRouter } from "connected-react-router";
import React from "react";
import { useDispatch, useSelector } from "react-redux";
import { Redirect, Route, Switch } from "react-router-dom";
import Authorization from "../component/authorization";
import HomeComponent from "../component/home";
import Validate from "../component/validate";
import { Userfilter, userList } from "../store/action/user.actions";
import { ApplicationState, history } from "../store/configureStore";
import { UserEnum } from "../store/constant/userTypes";
import _ from "lodash";
import { postList } from "../store/action/post.action";

const array = [
  "Blueasy88 bot",
  "Dũng Trần",
  "GoLD iNgoT",
  "Chuuni Character",
  "Christopher Albert",
  "CatHappy MeoMeo",
  "Eric kk",
  "hhjjsnsbdnd skjdhdje",
  "Daniel Lee",
  "2LD25 余佩倫 YU PUI LUN",
  "Candy_Cat",
  "Milk Special",
  "SHUNQI lEE",
  "Schwi Chan",
  "Bibi Gaming",
  "VanillaPopsicle",
];

const Navbar = () => {
  const selector = useSelector((state: ApplicationState) => state.user);
  const dispatch = useDispatch();

  const [filter, setFilter] = React.useState({
    show: false,
    text: "",
  });

  React.useEffect(() => {
    if (localStorage.getItem("token")) {
      dispatch(userList(filter.text));
    }
  }, [Boolean(localStorage.getItem("token"))]);

  const changeFilter = (args: React.ChangeEvent<HTMLInputElement>) => {
    let show: boolean = false;
    if (args.currentTarget.value) {
      show = true;
    } else {
      show = false;
    }
    dispatch(Userfilter(selector.user, args.currentTarget.value));
    setFilter({ ...filter, text: args.currentTarget.value, show: show });
  };

  const changeRouter = (args: string) => {
    history.push(args);
  };
  return (
    <div className="noc-navbar">
      <div className="noc-brand">Love</div>
      <div className="noc-input">
        <input
          type="text"
          placeholder="Search"
          value={filter.text}
          onChange={changeFilter}
        />
        <button className="noc-btn-input">
          <i className="fas fa-search"></i>
        </button>
        <div className="noc-navbar-input-dropdown">
          <div className="noc-navbar-dropdown-list">
            {_.map(
              Boolean(selector.soft[0]) ? selector.soft : selector.user,
              (base, index) => {
                return (
                  <div className="noc-navbar-dropdown-acc" key={index}>
                    <img src={base.accounts.avatar} alt="" />
                    <div className="noc-navbar-dropdown-acc-content">
                      <a href="">{base.first_name}</a>
                      <span>{base.accounts.bio.bio}</span>
                    </div>
                  </div>
                );
              }
            )}
          </div>
        </div>
      </div>
      <div className="noc-group">
        <button className="noc-t" onClick={changeRouter.bind("", "/accounts")}>
          Sign in
        </button>
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

  React.useEffect(() => {
    let mount = true;
    if (mount) {
      dispatch(postList());
    }
  }, []);

  return (
    <ConnectedRouter history={history}>
      <Navbar />
      <Validate />
      <Switch>
        <Route path="/" exact={true} component={HomeComponent} />
        <Route
          path="/accounts"
          render={({ location }) =>
            !localStorage.getItem("token") ? (
              <Authorization />
            ) : (
              <Redirect to={{ pathname: "/", state: { from: location } }} />
            )
          }
        />
      </Switch>
    </ConnectedRouter>
  );
};

export default Routes;
