const path = require('path');

module.exports = {
  entry: {
    main: './nhswebsites/static_src/js/main.js',
  },
  mode: 'production',
  module: {
    rules: [{
      test: /\.js$/,
      use: {
        loader: 'babel-loader',
        options: {
          presets: ['@babel/preset-env'],
        },
      },
    }],
  },
  output: {
    filename: '[name].min.js',
    path: path.resolve(__dirname, 'nhswebsites/static/js/'),
  },
  watchOptions: {
    ignored: /node_modules/,
  },
};
