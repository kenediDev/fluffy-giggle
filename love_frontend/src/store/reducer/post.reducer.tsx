import { Reducer } from "redux";
import { PostEnum, PostState } from "../constant/postTypes";

const initial: PostState = {
  post: [],
  data: { content: "", photo: "", author: {} },
  loading: false,
  message: {},
};

export const postReducer: Reducer<PostState> = (state = initial, action) => {
  switch (action.type) {
    case PostEnum.LIST:
      return {
        ...state,
        post: action.payload.post,
      };
      break;

    default:
      return state;
      break;
  }
};
