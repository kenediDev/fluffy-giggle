import { applyMiddleware, createStore, Store } from "redux";
import { composeWithDevTools } from "redux-devtools-extension";
import thunkMiddleware from "redux-thunk";
import loggerMiddleware from "redux-logger";
import store_ from "..";
import { routerMiddleware } from "connected-react-router";
import { createBrowserHistory } from "history";
import { UserState } from "../constant/userTypes";

export const history = createBrowserHistory();

export interface ApplicationState {
  user: UserState;
}

export default function configureStore(preloadedStore?: any) {
  const middleware = [thunkMiddleware];
  const store: Store<ApplicationState> = createStore(
    store_(history),
    preloadedStore,
    composeWithDevTools(
      applyMiddleware(
        ...middleware,
        loggerMiddleware,
        routerMiddleware(history)
      )
    )
  );
  if (module.hot) {
    module.hot.accept(() => {
      store.replaceReducer(store_(history));
    });
  }
  return store;
}
