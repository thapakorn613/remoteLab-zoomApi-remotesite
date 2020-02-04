var someVariable = {a:1 ,b:2}

function sayHello(name){
    console.log("Hello, "+name+"!")
}

function $nonPyName(){
    console.log('Non-Py names like $ can')
}

function Rectangle(w,h){
    this.w = w;
    this.h = h
}

Rectangle.prototype = {
    getArea: function(){
        return this.w * this.h
    }
};

x = new Rectangle(10,10)