module.exports = {
  outputDir: '../static/assets',
  filenameHashing: false,
  configureWebpack: {
    resolve: {
      alias: {
        'vue$': 'vue/dist/vue.esm.js',
      }
    }
  },
  chainWebpack: config => {
    config.plugins.delete('hmr');
    config.plugins.delete('html');
    config.plugins.delete('preload');
    config.plugins.delete('prefetch');
  }
};
