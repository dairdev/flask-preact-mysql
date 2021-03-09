import { preact, h, render, Fragment } from "preact";
import { Button } from "../components/button";

function LoginApp() {
	return (
		<div class="mx-auto w-80">
			<h2 class="text-6xl text-blue-700">Login</h2>
			<form action="/login" method="post">
				<div class="p-3 flex flex-col">
					<label class="flex items-center" htmlFor="user">
						<span class="material-icons">person</span>
						&nbsp;Usuario
					</label>
					<input
						type="text"
						name="user"
						id="user"
						class="border border-gray-600"
					/>
				</div>
				<div class="p-3 flex flex-col">
					<label class="flex items-center" htmlFor="password">
						<span class="material-icons">password</span>
						&nbsp;Password
					</label>
					<input
						id="password"
						type="password"
						name="password"
						class="border border-gray-600"
					/>
				</div>
				{error != "" ? <p className="p-2 text-red-800">{error}</p> : ""}
				<Button icon="done" text="Entrar" />
			</form>
		</div>
	);
}

render(<LoginApp />, document.getElementById("app"));
