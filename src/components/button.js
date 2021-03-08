import { h } from "preact";

function Button({ icon, text }) {
	return (
		<button class="flex items-center justify-center rounded-md w-1/2 p-2 text-white bg-blue-700 hover:bg-blue-200 hover:text-black">
			<span class="material-icons">{icon}</span>
			{text}
		</button>
	);
}

export { Button };
