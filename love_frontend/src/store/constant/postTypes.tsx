import { Message } from "../../types/message";
import { Post } from "../../types/postT";

export enum PostEnum {
  CREATE = "SERVE::POST::CREATE",
  LIST = "SERVE::POST::LIST",
  DETAIL = "SERVE::POST:DETAIL",
}

export interface PostState {
  readonly post: Post[];
  readonly data: Post;
  readonly message: Message;
  readonly loading: boolean;
}
