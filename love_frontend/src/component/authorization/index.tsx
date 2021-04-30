import React from "react";
import { AuthChoice, AuthContext, AuthContextC } from "./context";

const Authorization: React.FC = () => {
  const [choice, setChoice] = React.useState<AuthChoice>("login");

  return (
    <AuthContext.Provider
      value={{
        choice,
        setChoice,
      }}
    >
      <div className="noc-form">
        <AuthContextC />
      </div>
    </AuthContext.Provider>
  );
};

export default Authorization;
