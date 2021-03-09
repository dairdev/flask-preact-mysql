import { preact, h, render, Fragment } from "preact";
import { Sidebar } from "../components/sidebar";

const links = [
	{ url: "/home", icon: "home", text: "Home" },
	{ url: "/documents", icon: "folder", text: "Documents" },
];

function App({ user }) {
	return (
		<Fragment>
			<div class="text-3xl">Hello {user}</div>
			<Sidebar links={links} />
		</Fragment>
	);
}

render(<App user={user} />, document.getElementById("app"));
