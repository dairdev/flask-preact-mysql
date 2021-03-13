import { preact, h, render, Fragment } from "preact";
import { Sidebar } from "../components/sidebar";
import { links } from '../components/links';

function App({ user }) {
	return (
		<Fragment>
			<div class="text-3xl">Hello {user}</div>
			<div className="flex">
				<Sidebar links={links} />
				<div class="w-3/4">
					<div className="flex items-center">
						<div className="w-3/4">
							This is home
						</div>
						<div class="flex flex-col p-3"></div>
					</div>
				</div>
			</div>
		</Fragment>
	);
}

render(<App user={user} />, document.getElementById("app"));
