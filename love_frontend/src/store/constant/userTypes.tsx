import { Message } from "../../types/message";
import { User } from "../../types/userT";

export enum UserEnum {
  CREATE = "SERVE::USR::CREATE",
  UPDATE = "SERVE::USR::UPDATE",
  LOGIN = "SERVE::USR::LOGIN",
  LIST = "SERVE::USR::LIST",
  RETRIEVE = "SERVE::USR::RETRIEVE",
  LOADING = "SERVE::USR::LOADING",
  MESSAGE = "SERVE::USR::MESSAGE",
  REVOKE = "SERVE::USR::REVOKE",
}

export interface UserState {
  readonly user: User[];
  readonly data: User;
  readonly message: Message;
  readonly loading: boolean;
  readonly token: string;
}
