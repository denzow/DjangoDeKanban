module.exports = {
  root: true,
  env: {
    node: true
  },
  'extends': [
    'plugin:vue/essential',
    '@vue/airbnb'
  ],
  rules: {
    'no-underscore-dangle': 0,
    'no-console': process.env.NODE_ENV === 'production' ? 'error' : 'off',
    'no-debugger': process.env.NODE_ENV === 'production' ? 'error' : 'off',
    'no-shadow': ['error', { 'builtinGlobals': false, 'hoist': 'functions', 'allow': ['state', 'getters'] }],
    'arrow-parens': [2, "as-needed"],
    'no-alert': 0,
    'no-param-reassign': [
      'error',
      {
        props: true,
        ignorePropertyModificationsFor: [
          'state', // for vuex state
          'acc', // for reduce accumulators
          'e', // for e.returnvalue
        ],
      },
    ],
    'max-len': ['error', { 'code': 140 }],
  },
  parserOptions: {
    parser: 'babel-eslint'
  }
};