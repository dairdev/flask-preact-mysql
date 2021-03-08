import { preact, h, render, Fragment } from "preact";

function HomeApp({ user }) {
	return <Fragment>Hello {user}</Fragment>;
}

render(<HomeApp user={user} />, document.getElementById("app"));
