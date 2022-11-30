const statusText = document.querySelectorAll('strong')

function textWrap() {
	if (document.documentElement.clientWidth > 450) {
	statusText.forEach(el => {
		if (
			el.innerText.toLowerCase() === 'отменен' ||
			el.innerText.toLowerCase() === 'на утверждении'
		) {
			const parrentElement = el.closest('.row')
			parrentElement.style = 'flex-direction: column;'
		} else {
			return
		}
	})
}
}
textWrap()
