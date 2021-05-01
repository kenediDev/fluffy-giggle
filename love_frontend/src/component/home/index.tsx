import React from "react";
import { useSelector } from "react-redux";
import { useHistory } from "react-router";
import { ApplicationState } from "../../store/configureStore";
import _ from "lodash";

const HomeComponent: React.FC = () => {
  const selector = useSelector((state: ApplicationState) => state.post);
  const history = useHistory();
  const handleClickRouter = (args: string) => {
    history.push(args);
  };
  return (
    <div className="noc-grid">
      <div className="noc-col">First </div>
      <div className="noc-col">
        {_.map(selector.post, (base, index) => {
          return (
            <div className="noc-post" key={index}>
              <div className="noc-post-author">
                <img src={base.author.accounts.avatar} alt="" />
                <div className="noc-post-author-headers">
                  <a href="">
                    <span>{base.author.first_name}</span>
                    <span>
                      {base.author.last_name ? base.author.last_name : ""}
                    </span>
                  </a>
                  <span className="noc-post-metadata">{base.time}</span>
                </div>
              </div>
              <div className="noc-post-content">
                <div
                  className="noc-post-photo"
                  style={{ backgroundImage: `url(${base.photo})` }}
                ></div>
                <span>{base.content}</span>
              </div>
            </div>
          );
        })}
      </div>
      <div className="noc-col">Three</div>
    </div>
  );
};

export default HomeComponent;

// {_.map(selector.post, (base, index) => {
//   return (
//     <div className="noc-post" key={index}>
//       <div className="noc-content">
//         <img src={base.photo} alt="" />
//         <span>{base.content}</span>
//       </div>
//     </div>
//   );
// })}
