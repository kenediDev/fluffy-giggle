import { connectRouter } from "connected-react-router";
import { History } from "history";
import { combineReducers } from "redux";
import { postReducer } from "./reducer/post.reducer";
import { userReducer } from "./reducer/user.reducer";

const stores_ = (history: History) =>
  combineReducers({
    router: connectRouter(history),
    user: userReducer,
    post: postReducer,
  });

export default stores_;
