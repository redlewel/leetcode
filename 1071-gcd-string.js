/**
 * @param {string} str1
 * @param {string} str2
 * @return {string}
 */
var gcdOfStrings = function(str1, str2) {
    // if the result reversed is not equal then the two strings cannot have a GCD
    if (str1 + str2 != str2 + str1) {
        return '';
    }
    // Determine which string is longer and assign values to sStr and lStr
    let sStr = str1;
    let lStr = str2;
    if (str1.length > str2.length) {
        sStr = str2;
        lStr = str1;
    }
    function splat (str) {
        console.log(str);
	let strLen = str.length;
	let strLargeLen = lStr.length;
	let strSmallLen = sStr.length;
	/*
	lengthy1 = sStr.split(str).length;
	lengthy2 = lStr.split(str).length;
	console.log(`Length of large string after split: ${lengthy1}`);
	console.log(`Length of small string after split: ${lengthy2}`);
	*/
        if (strLargeLen % strLen != 0 || strSmallLen % strLen != 0) {
            return false;
        }
        else { 
            return true;
        }
    }
    let splitty = sStr;
    splatVal = splat(splitty);
	console.log(splatVal);
    while (splatVal == false) {
        splitty = splitty.slice(0, -1);
        splatVal = splat(splitty);
    } 
    return splitty;
};

console.log(gcdOfStrings("ABCABC", "ABC"));
