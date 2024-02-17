/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{js,jsx,ts,tsx}",],
  theme: {
    extend: {
      colors: {
        'qr-color': '#63CA04',
        'qr-dark-third': 'rgba(30, 31, 38, 1)',
        'qr-dark': '#272B30',
        'qr-gray-4': '#737373',
      }
    },
  },
  plugins: [],
}

