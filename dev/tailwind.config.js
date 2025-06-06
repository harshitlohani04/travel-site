/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html",
    "./static/**/*.js"
  ],
  theme: {
    extend: {
      colors: {
        primary: "#CB0404",
        secondary: "#F4631E",
        accent: "#FF9F00",
        background: "#F3F4F6",
        text: "#309898",
        subheading:"#129990",
        hoverbutton : "#BB3E00",
        navbar: "#EFE4D2"
      },
      fontFamily: {
        sans: ['"Inter"', 'sans-serif'],
        serif: ['"Merriweather"', 'serif'],
      },
      height:{
        herosection: "40rem",
        full: "100%"
      },
      minHeight: {
        herosection: "40rem"
      },
      fontFamily: {
        hero : ['"Gloria Hallelujah"', 'sans-serif'],
        subheading: ["Poppins", "sans-serif"]
      }
    },
  },
  plugins: [],
}

