import { h } from "preact";

function Sidebar({ links }) {
	return (
		<div class="w-1/4 bg-blue-900">
			{links.map(function (link) {
				return (
					<div class="">
						<a
							className="flex items-center p-3 text-white hover:bg-blue-800"
							href={link.url}
						>
							<span className="material-icons">{link.icon}</span>
							{link.text}
						</a>
					</div>
				);
			})}
		</div>
	);
}

export { Sidebar };
