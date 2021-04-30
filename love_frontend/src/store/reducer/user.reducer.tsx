import { Reducer } from "redux";
import { UserEnum, UserState } from "../constant/userTypes";

const initial: UserState = {
  token: "",
  user: [],
  data: {},
  message: {
    message: "",
    valid: false,
    show: false,
  },
  loading: false,
};

export const userReducer: Reducer<UserState> = (state = initial, action) => {
  switch (action.type) {
    case UserEnum.LOGIN:
      return { ...state, token: action.payload.token };
      break;
    case UserEnum.REVOKE:
      return { ...state, token: "" };
      break;
    case UserEnum.MESSAGE:
      return {
        ...state,
        message: {
          message: action.payload.message,
          valid: action.payload.valid,
          show: action.payload.show,
        },
      };
      break;

    default:
      return state;
      break;
  }
};
