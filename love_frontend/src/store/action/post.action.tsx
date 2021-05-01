import axios, { AxiosResponse } from "axios";
import { Dispatch } from "redux";
import { PostEnum } from "../constant/postTypes";

export const postList = () => {
  return async (dispatch: Dispatch) => {
    const response = await axios
      .get("/api/v1/post/", {
        headers: {
          "Content-Type": "application/json",
          "Access-Control-Allow-Methods": "GET",
          "Access-Control-Allow-Headers":
            "Content-Type, Origin, Accepted, X-Requested-With",
          "Access-Control-Allow-Origin": "*",
        },
        timeout: 865000,
        responseType: "json",
        withCredentials: false,
        maxRedirects: 5,
        maxContentLength: 2000,
        validateStatus: (status: number) => status >= 200 && status < 300,
      })
      .then((res: AxiosResponse<any>) => {
        dispatch({
          type: PostEnum.LIST,
          payload: { post: res.data },
        });
      })
      .catch((err) => {
        console.log(err);
      });
    return response;
  };
};
