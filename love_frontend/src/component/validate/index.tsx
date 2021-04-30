import React from "react";
import { useSelector } from "react-redux";
import { ApplicationState } from "../../store/configureStore";

const Validate: React.FC = () => {
  const selector = useSelector((state: ApplicationState) => state.user);
  return (
    <div className={selector.message.show ? "validate" : "hidden"}>
      <div
        className={
          selector.message.valid ? "validate-success" : "validate-error"
        }
      >
        <div className="validate-text">{selector.message.message}</div>
      </div>
    </div>
  );
};

export default Validate;
