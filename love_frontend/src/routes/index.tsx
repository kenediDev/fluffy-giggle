import { ConnectedRouter } from "connected-react-router";
import React from "react";
import { useDispatch, useSelector } from "react-redux";
import { Route, Switch } from "react-router-dom";
import Authorization from "../component/authorization";
import HomeComponent from "../component/home";
import Validate from "../component/validate";
import { Userfilter, userList } from "../store/action/user.actions";
import { ApplicationState, history } from "../store/configureStore";
import { UserEnum } from "../store/constant/userTypes";
import _ from "lodash";

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
    let mount = true;
    if (mount) {
      dispatch(userList(filter.text));
      return () => {
        mount = false;
      };
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
        <div className={filter.show ? "noc-navbar-input-dropdown" : "hidden"}>
          <div className="noc-navbar-dropdown-content">
            <div className="noc-navbar-dropdown-list">
              {_.map(
                Boolean(selector.soft[0]) ? selector.soft : selector.user,
                (base, index) => {
                  return (
                    <div className="noc-navbar-dropdown-acc" key={index}>
                      <img
                        src="data:image/jpeg;base64,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"
                        alt=""
                      />
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
