import { User } from "./userT";

export interface Post {
  photo: string;
  content: string;
  author: User;
  createAt?: Date;
  updateAt?: Date;
  time?: string;
}
