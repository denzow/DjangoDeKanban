module.exports = {
  outputDir: '../static/assets',
  filenameHashing: false,
  runtimeCompiler: true,
  chainWebpack: config => {
    config.plugins.delete('hmr');
    config.plugins.delete('html');
    config.plugins.delete('preload');
    config.plugins.delete('prefetch');
  },
};
