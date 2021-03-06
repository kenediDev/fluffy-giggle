export interface Interested {
  name: string;
}

export interface Biodata {
  bio: string;
  interested?: Interested[];
}

export interface Location {
  country: string;
  province: string;
  city: string;
  address: string;
}

export interface Accounts {
  avatar: string;
  phone_numbers: string;
  location?: Location;
  bio: Biodata;
}

export interface User {
  token?: string;
  username?: string;
  email?: string;
  first_name?: string;
  last_name?: string;
  password?: string;
  old_password?: string;
  confirm_password?: string;
  accounts?: Accounts;
}
