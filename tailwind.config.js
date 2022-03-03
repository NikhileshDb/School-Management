module.exports = {
  content: [
    "./templates/**/*.{html,js}",
    "./static/**/*.{html,js}",
  ],
  theme: {
    fontFamily: {
        'display': ['Ubuntu'], 
        'body': ['Ubuntu'],
    },
    extend: {
    },
  },
  plugins: [
    require('tw-elements/dist/plugin')
    
  ],
}
