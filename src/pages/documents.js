import { preact, h, render, Fragment } from "preact";
import { useState } from "preact/hooks";
import { Sidebar } from "../components/sidebar";
import { Button } from "../components/button";

const links = [
	{ url: "/home", icon: "home", text: "Home" },
	{ url: "/documents", icon: "folder", text: "Documents" },
];

function App({ user }) {
	const [files, setFiles] = useState(null);

	const onClickUpload = () => {
		console.log("uploading ...");

		const formData = new FormData();

		formData.append("file", document.querySelector("#uploadFile").files[0]);

		fetch("/upload", {
			method: "POST",
			body: formData,
		})
			.then((res) => res.json())
			.then((json) => console.log(json))
			.catch((eror) => console.log(eror));
	};

	return (
		<Fragment>
			<div class="text-3xl">Hello {user}</div>
			<div className="flex">
				<Sidebar links={links} />
				<div class="w-3/4">
					<div className="flex items-center">
						<div class="w-3/4">
							<form class="p-2 flex items-center justify-between">
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
								<Button
									icon="done"
									text="Upload"
									type="button"
									onClickCallback={onClickUpload}
								/>
							</form>
						</div>
						<div class="flex flex-col p-3"></div>
					</div>
				</div>
			</div>
		</Fragment>
	);
}

render(<App user={user} />, document.getElementById("app"));
