var { merge } = require("webpack-merge");
var common = require("./webpack.common");
var path = require("path");

module.exports = merge(common, {
  mode: "development",
  devtool: "source-map",
  devServer: {
    contentBase: path.join(__dirname, "../dist"),
    open: 'google chrome'
  },
});
