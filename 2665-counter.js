/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
	let returnVal = init;
	function modify(n) {
		if (n == 0) {
			returnVal = init;
		}
		else {
			returnVal = returnVal + n;
		}
	}
	return {
		increment() {
			modify(1);
		}, 
		decrement() {
			modify(-1);
		}, 
		reset() {
			modify(0);
		}


};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 *
