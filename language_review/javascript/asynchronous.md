# python_review

* JavaScript is a single-threaded programming language

## Call Stack
* A mechanism for an interpreter to keep track of its place in a script that calls multiple functions
* Process
  * When function is called, interpreter adds it to call stack, then starts carrying out the function 
  * If a function is called within a function that's already in the call stack, it's added to the call stack further up
  * When current function is finished, interpreter pops it off stack and resumes execution where it left off

*  JavaScript has a single call stack (LIFO)

***

## Event Loop
* In most browsers, there's an event loop for every tab
  * makes every process isolated
  * avoids a web page with infinite loops/heavy processing to block entire browser
* Event loop looks into call stack and determines if call stack is empty or not
  * If empty, it looks into message queue 
    * Whatever is in message queue is added to the call stack
  * Event loop adds from message queue to call stack only if call stack is empy


***

## References
* https://developer.mozilla.org/en-US/docs/Glossary/Call_stack
* https://blog.bitsrc.io/understanding-asynchronous-javascript-the-event-loop-74cd408419ff
* https://www.youtube.com/watch?v=4xsvn6VUTwQ
