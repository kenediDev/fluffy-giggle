import React from "react";
import { useDispatch } from "react-redux";
import { forgot, login, register } from "../../../store/action/user.actions";
import { User } from "../../../types/userT";

export type AuthChoice = "login" | "register" | "forgot";

interface Context {
  choice: AuthChoice;
  setChoice: React.Dispatch<React.SetStateAction<AuthChoice>>;
}

export const AuthContext = React.createContext<Partial<Context>>({});
export const AuthContextC = () => {
  const { choice, setChoice } = React.useContext(AuthContext);
  const dispatch = useDispatch();
  const [state, setState] = React.useState<User>({
    token: "",
    username: "",
    email: "",
    password: "",
    confirm_password: "",
  });
  const changeToken = (args: React.ChangeEvent<HTMLInputElement>) => {
    setState({ ...state, token: args.currentTarget.value });
  };
  const changeUsername = (args: React.ChangeEvent<HTMLInputElement>) => {
    setState({
      ...state,
      username: args.currentTarget.value,
    });
  };
  const changeEmail = (args: React.ChangeEvent<HTMLInputElement>) => {
    setState({ ...state, email: args.currentTarget.value });
  };
  const changePassword = (args: React.ChangeEvent<HTMLInputElement>) => {
    setState({
      ...state,
      password: args.currentTarget.value,
    });
  };
  const changeConfirmPassword = (args: React.ChangeEvent<HTMLInputElement>) => {
    setState({ ...state, confirm_password: args.currentTarget.value });
  };
  const submit = (args: React.FormEvent<HTMLFormElement>) => {
    args.preventDefault();
    if (choice === "login") {
      dispatch(login(state, setState));
    } else if (choice === "register") {
      dispatch(register(state, setState));
    } else if (choice === "forgot") {
      dispatch(forgot(state, setState));
    }
  };

  const handleClickChoice = (args: AuthChoice) => {
    setState({
      ...state,
      token: "",
      username: "",
      email: "",
      password: "",
      confirm_password: "",
    });
    setChoice(args);
  };

  return (
    <AuthContext.Consumer>
      {({ choice }) => {
        switch (choice) {
          case "login":
            return (
              <form className="noc-authorization" onSubmit={submit}>
                <div className="noc-field">
                  <input
                    type="text"
                    name="username"
                    id="username"
                    placeholder="Username"
                    autoComplete="off"
                    value={state.username || ""}
                    onChange={changeUsername}
                    required={true}
                  />
                </div>
                <div className="noc-field">
                  <input
                    type="password"
                    name="password"
                    id="password"
                    placeholder="Password"
                    autoComplete="off"
                    onChange={changePassword}
                    value={state.password || ""}
                    required={true}
                  />
                </div>
                <div className="noc-field">
                  <button type="submit" className="noc-authorization-btn">
                    Sign in
                  </button>
                  <div id="noc-field">
                    <a
                      href="#"
                      onClick={handleClickChoice.bind("", "register")}
                      className="noc-link"
                    >
                      Create New Accounts?
                    </a>
                    <a
                      href="#"
                      onClick={handleClickChoice.bind("", "forgot")}
                      className="noc-link"
                    >
                      Forgotted Password?
                    </a>
                  </div>
                </div>
              </form>
            );
            break;
          case "register":
            return (
              <form className="noc-authorization" onSubmit={submit}>
                <div className="noc-field">
                  <input
                    type="text"
                    name="username"
                    id="username"
                    placeholder="Username"
                    autoComplete="off"
                    value={state.username || ""}
                    onChange={changeUsername}
                    required={true}
                  />
                </div>
                <div className="noc-field">
                  <input
                    type="email"
                    name="email"
                    id="email"
                    placeholder="Email"
                    value={state.email || ""}
                    onChange={changeEmail}
                    autoComplete="off"
                    required={true}
                  />
                </div>
                <div className="noc-field">
                  <input
                    type="password"
                    name="password"
                    id="password"
                    placeholder="Password"
                    autoComplete="off"
                    onChange={changePassword}
                    value={state.password || ""}
                    required={true}
                  />
                </div>
                <div className="noc-field">
                  <input
                    type="password"
                    name="confirm_password"
                    id="confirm_password"
                    value={state.confirm_password || ""}
                    onChange={changeConfirmPassword}
                    placeholder="Confirm Password"
                    autoComplete="off"
                    required={true}
                  />
                </div>
                <div className="noc-field">
                  <button type="submit" className="noc-authorization-btn">
                    Sign up
                  </button>
                  <div id="noc-field">
                    <a
                      href="#"
                      onClick={handleClickChoice.bind("", "login")}
                      className="noc-link"
                    >
                      Already exists accounts?
                    </a>
                  </div>
                </div>
              </form>
            );
            break;
          case "forgot":
            return (
              <form className="noc-authorization" onSubmit={submit}>
                <div className="noc-field">
                  <input
                    type="text"
                    name="token"
                    id="token"
                    placeholder="Enter your username or email address"
                    autoComplete="off"
                    value={state.token || ""}
                    onChange={changeToken}
                    required={true}
                  />
                </div>

                <div className="noc-field">
                  <button type="submit" className="noc-authorization-btn">
                    Reset
                  </button>
                  <div id="noc-field">
                    <a
                      href="#"
                      onClick={handleClickChoice.bind("", "login")}
                      className="noc-link"
                    >
                      Already exists accounts?
                    </a>
                  </div>
                </div>
              </form>
            );
          default:
            break;
        }
      }}
    </AuthContext.Consumer>
  );
};
