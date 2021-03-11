import { h } from "preact";

function Button({ icon, text }) {
	return (
		<button class="btn">
			<span class="material-icons-sharp">{icon}</span>
			{text}
		</button>
	);
}

export { Button };
