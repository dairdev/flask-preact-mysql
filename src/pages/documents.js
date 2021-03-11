import { preact, h, render, Fragment } from "preact";
import { useState } from "preact/hooks";
import { Sidebar } from "../components/sidebar";
import { Button } from "../components/button";

const links = [
	{ url: "/home", icon: "home", text: "Home" },
	{ url: "/documents", icon: "folder", text: "Documents" },
];

function App({ user }) {

	const [ files, setFiles ] = useState(null);

	return (
		<Fragment>
			<div class="text-3xl">Hello {user}</div>
			<div className="flex">
				<Sidebar links={links} />
				<div class="w-3/4">
					<div className="flex items-center">
						<div class="w-3/4">
							<div class="p-2 flex items-center justify-between">
								<span class="w-10/12">
									<span className="material-icons-sharp">
										cloud_upload
									</span>
									<input
										id="uploadFile"
										type="file"
										name="uploadFile"
										class="border border-gray-600 w-auto"
									/>
								</span>
								<Button icon="done" text="Upload" />
							</div>
						</div>
						<div class="flex flex-col p-3">
						</div>
					</div>
				</div>
			</div>
		</Fragment>
	);
}

render(<App user={user} />, document.getElementById("app"));
