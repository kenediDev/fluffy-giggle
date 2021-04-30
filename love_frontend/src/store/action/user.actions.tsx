import axios, { AxiosResponse } from "axios";
import { Dispatch } from "redux";
import { User } from "../../types/userT";
import { UserEnum } from "../constant/userTypes";

export const login = (
  args: User,
  argsState: React.Dispatch<React.SetStateAction<User>>
) => {
  return async (dispatch: Dispatch) => {
    const response = await axios
      .post(
        "api-token-auth/",
        { username: args.username, password: args.password },
        {
          headers: {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "POST",
            "Access-Control-Allow-Headers":
              "Content-Type, Origin, Accepted, X-Requested-With",
          },
          timeout: 865000,
          responseType: "json",
          withCredentials: false,
          maxRedirects: 5,
          maxContentLength: 2000,
          validateStatus: (status: number) => status >= 200 && status < 300,
          transformResponse: [
            function (data) {
              dispatch({
                type: UserEnum.MESSAGE,
                payload: {
                  show: false,
                },
              });

              return data;
            },
          ],
        }
      )
      .then((res: AxiosResponse<any>) => {
        argsState({
          ...args,
          username: "",
          password: "",
        });
        dispatch({
          type: UserEnum.LOGIN,
          payload: {
            token: res.data.token,
          },
        });
      })
      .catch((err) => {
        setTimeout(() => {
          dispatch({
            type: UserEnum.MESSAGE,
            payload: {
              message: err.response.data.non_field_errors[0],
              valid: false,
              show: true,
            },
          });
        }, 500);
      });
    return response;
  };
};

export const register = (
  args: User,
  argsState: React.Dispatch<React.SetStateAction<User>>
) => {
  return async (dispatch: Dispatch) => {
    const response = await axios
      .post(
        "api/v1/user/",
        {
          username: args.username,
          email: args.email,
          password: args.password,
          confirm_password: args.confirm_password,
        },
        {
          headers: {
            "Content-Type": "application/json",
            "Access-Control-Allow-Methods": "POST",
            "Access-Control-Allow-Headers":
              "Content-Type, Origin, Accepted, X-Requested-With",
            "Access-Control-Allow-Origin": "*",
          },
          timeout: 865000,
          responseType: "json",
          withCredentials: false,
          maxRedirects: 5,
          maxContentLength: 2000,
          validateStatus: (status: number) => status >= 201 && status < 300,
          transformResponse: [
            function (data) {
              dispatch({ type: UserEnum.MESSAGE, payload: { show: false } });
              return data;
            },
          ],
        }
      )
      .then((res: AxiosResponse<any>) => {
        argsState({
          ...args,
          username: "",
          email: "",
          password: "",
          confirm_password: "",
        });
        setTimeout(() => {
          dispatch({
            type: UserEnum.MESSAGE,
            payload: {
              message: res.data.message,
              valid: true,
              show: true,
            },
          });
        }, 500);
      })
      .catch((err) => {
        setTimeout(() => {
          dispatch({
            type: UserEnum.MESSAGE,
            payload: {
              message: err.response.data.message,
              valid: false,
              show: true,
            },
          });
        }, 500);
      });
    return response;
  };
};

export const forgot = (
  args: User,
  argsState: React.Dispatch<React.SetStateAction<User>>
) => {
  return async (dispatch: Dispatch) => {
    const response = await axios
      .post(
        "api/v1/user/reset/password/",
        { token: args.token },
        {
          headers: {
            "Content-Type": "application/json",
            "Access-Control-Allow-Methods": "POST",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers":
              "Content-Type, Origin, Accepted, X-Requested-With",
          },
          timeout: 865000,
          responseType: "json",
          withCredentials: false,
          maxRedirects: 5,
          maxContentLength: 2000,
          validateStatus: (status: number) => status >= 200 && status < 300,
          transformResponse: [
            function (data) {
              dispatch({
                type: UserEnum.MESSAGE,
                payload: { show: false },
              });
              return data;
            },
          ],
        }
      )
      .then((res: AxiosResponse<any>) => {
        argsState({ ...args, token: "" });
        setTimeout(() => {
          dispatch({
            type: UserEnum.MESSAGE,
            payload: { message: res.data.message, valid: true, show: true },
          });
        }, 500);
      })
      .catch((err) => {
        setTimeout(() => {
          dispatch({
            type: UserEnum.MESSAGE,
            payload: {
              message: err.response.data.message,
              valid: false,
              show: true,
            },
          });
        }, 500);
      });
    return response;
  };
};
