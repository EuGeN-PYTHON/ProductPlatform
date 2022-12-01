const statusText = document.querySelectorAll('strong')

function textWrap() {
	if (document.documentElement.clientWidth < 450) {
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

// Контролирует баннер и его размер
const blocksBanner = document.querySelectorAll('.main-banner')

function changeHeight() {
	if (document.documentElement.clientWidth < 550) {
	blocksBanner.forEach(el => {
		if(el.querySelector('img')){
			el.style = "height: 400px;"
		} else {
			el.style = "height: 215px;"
	}})
}
}
changeHeight()
