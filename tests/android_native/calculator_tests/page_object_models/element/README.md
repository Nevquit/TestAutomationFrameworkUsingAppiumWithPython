## Element Object 

<div align="right"> 
<img width="7%" height="7%" src="https://github.com/ikostan/ParaBankSeleniumAutomation/blob/master/images/iconfinder_availability-items_3018516.png" hspace="10">
</div>

Element is the most general base class from which all objects in a Document inherit. It only has methods and properties common to all kinds of elements.<br/>

In the HTML DOM, the Element object represents an HTML element, like P, DIV, A, TABLE, or any other HTML element.<br/>

Selenium Web Driver encapsulates a simple form element as an object of WebElement. It provides API to find the elements and take action on them like entering text into text boxes, clicking the buttons, etc.<br/>

### What is WebElement?<br/>

WebElement represents an HTML element. HTML documents are made up by HTML elements. HTML elements are written with a start tag, with an end tag, with the content in between.<br/>

The HTML element is everything from the start tag to the end tag.<br/>

HTML elements can be nested (elements can contain elements). All HTML documents consist of nested HTML elements.<br/>

One more thing to notice that WebElement can be of any type, like it can be a Text, Link, Radio Button, Drop Down, WebTable or any HTML element. But all the actions will always populate against the any element irrespective of whether the action is valid on the WebElement or not. For e.g. clear() command, even if you have a link element still you get the option to choose clear() command on it, which if you choose may result in some error or may not does anything.<br/>

Sources:<br/>

- [Selenium Form WebElement: TextBox, Submit Button, sendkeys(), click()](https://www.guru99.com/accessing-forms-in-webdriver.html)<br/>
- [WebElement Commands](https://www.toolsqa.com/selenium-webdriver/webelement-commands/)<br/>
- [Element](https://developer.mozilla.org/en-US/docs/Web/API/Element)<br/>
- [The HTML DOM Element Object](https://www.w3schools.com/jsref/dom_obj_all.asp)
- [DOM - Element Object](https://www.tutorialspoint.com/dom/dom_element_object)