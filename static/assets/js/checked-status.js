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
const blockBanner = document.querySelectorAll('.main-banner')

function changeHeight() {
	if (document.documentElement.clientWidth < 550) {
	blocks.forEach(el => {
		if(el.querySelector('img')){
			el.style = `${el.getAttribute('style')} height:400px;`
		} else {
			el.style = `${el.getAttribute('style')} height:215px;`
	}})
}
}
changeHeight()
