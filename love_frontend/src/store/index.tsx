import { connectRouter } from "connected-react-router";
import { History } from "history";
import { combineReducers } from "redux";
import { userReducer } from "./reducer/user.reducer";

const stores_ = (history: History) =>
  combineReducers({
    router: connectRouter(history),
    user: userReducer,
  });

export default stores_;
