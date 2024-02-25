const { defineConfig } = require('@vue/cli-service')
// module.exports = defineConfig({
//   transpileDependencies: true,
//   allowedHosts: [
//     'localhost'
//   ],
// })
module.exports = {
  devServer: {
    allowedHosts: [
      'localhost'
    ],
  }
}