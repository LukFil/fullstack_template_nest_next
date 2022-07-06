const path = require("path");

const buildEslintCommand = (filenames) =>
  `next lint --fix --file ${filenames
    .map((f) => path.relative(process.cwd(), f))
    .join(" --file ")}`;

module.exports = {
  "*.{js,jsx,ts,tsx}": [buildEslintCommand, "prettier --write"],
};
// {
//     "*.{ts,tsx}": ["yarn next lint --fix"],
//     "*.{json,md,html,js,jsx,ts,tsx}": ["prettier --write"]
// }
