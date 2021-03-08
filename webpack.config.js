const path = require("path");

module.exports = {
	mode: "development",
	entry: {
		home: "./src/pages/home.js",
		login: "./src/pages/login.js",
	},
	output: {
		path: __dirname + "/static/js/",
		filename: "[name].min.js",
	},
	module: {
		rules: [
			{
				test: /\.(jsx|js)$/,
				include: path.resolve(__dirname, "src"),
				exclude: /node_modules/,
				use: [
					{
						loader: "babel-loader",
					},
				],
			},
		],
	},
	resolve: {
		alias: {
			react: "preact/compat",
			"react-dom/test-utils": "preact/test-utils",
			"react-dom": "preact/compat",
		},
	},
};
