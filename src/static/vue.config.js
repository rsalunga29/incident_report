const path = require('path')

function resolve(dir) {
  return path.join(__dirname, dir)
}

module.exports = {
  chainWebpack: config => {
    config.resolve.alias.set('@$', resolve('src'))
  },

  devServer: {
    proxy: {
      '^/api': {
        target: 'http://localhost:8000',
        ws: false,
        changeOrigin: true,
      }
    },

    historyApiFallback: true,
    overlay: {
      warnings: false,
      errors: true
    }
  },
}
