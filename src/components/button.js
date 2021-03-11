import { h } from "preact";

function Button({ icon, text, type, onClickCallback }) {
	return (
		<button type={type} class="btn" onClick={onClickCallback}>
			<span class="material-icons-sharp">{icon}</span>
			{text}
		</button>
	);
}

export { Button };
