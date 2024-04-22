function callbackFunction(callback) {
    callback();
}

function sayHello() {
    console.log('Hello');
}

callbackFunction(sayHello)