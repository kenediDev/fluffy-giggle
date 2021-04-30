import React from "react";
import { useHistory } from "react-router";

const HomeComponent: React.FC = () => {
  const history = useHistory();
  const handleClickRouter = (args: string) => {
    history.push(args);
  };
  return (
    <div>
      <div>Hello Worlds</div>
      <button onClick={handleClickRouter.bind("", "/accounts")}>Login</button>
    </div>
  );
};

export default HomeComponent;
