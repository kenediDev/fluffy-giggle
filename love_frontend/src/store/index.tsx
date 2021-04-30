import { connectRouter } from "connected-react-router";
import { History } from "history";
import { combineReducers } from "redux";

const stores_ = (history: History) =>
  combineReducers({
    router: connectRouter(history),
  });

export default stores_;
