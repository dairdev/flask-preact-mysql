import { preact, h, render, Fragment } from "preact";
import { useState, useEffect } from "preact/hooks";
import { Sidebar } from "../components/sidebar";
import { Button } from "../components/button";
import { links } from "../components/links";

function App({ user }) {
	const [files, setFiles] = useState([]);

	useEffect(() => {
		//console.log('useEffect');
		fetch("/documents/list", {
			method: "GET",
		})
			.then((res) => res.json())
			.then((json) => {
				console.log(json);
				setFiles(json.files);
			})
			.catch((eror) => console.log(eror));
	}, []);

	const onClickUpload = () => {
		const formData = new FormData();

		formData.append("file", document.querySelector("#uploadFile").files[0]);

		fetch("/upload", {
			method: "POST",
			body: formData,
		})
			.then((res) => res.json())
			.then((json) => {
				setFiles(json.files);
			})
			.catch((eror) => console.log(eror));
	};

	const onClickDelete = (target) => {
		if (target.tagName == "SPAN") target = target.parentNode;

		fetch("/document/delete", {
			method: "POST",
			headers: {
				"Content-Type": "application/json",
			},
			body: JSON.stringify({ id: target.dataset.id }),
		})
			.then((res) => res.json())
			.then((json) => {
				if (json.result == true) {
					let index = files.findIndex(
						(f) => f.id == target.dataset.id
					);
					setFiles((fs) => fs.splice(index, 1));
				}
			})
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

							<div className="flex flex-col p-3">
								{files
									? files.map(function (f) {
											return (
												<div className="flex items-center justify-between p-5 bg-blue-100 rounded-sm md-1">
													<span>{f.fileName}</span>
													<button
														type="button"
														title="Borrar archivo"
														className="hover:text-red-600"
														data-id={f.id}
														onClick={(e) =>
															onClickDelete(
																e.target
															)
														}
													>
														<span className="material-icons-sharp">
															delete
														</span>
													</button>
												</div>
											);
									  })
									: null}
							</div>
						</div>
					</div>
				</div>
			</div>
		</Fragment>
	);
}

render(<App user={user} />, document.getElementById("app"));
