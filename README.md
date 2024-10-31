BE Module 15 Lesson 2: Assignment | Implementing WebSocket Servers and Clients
Remember to take your time and work through each question diligently! Test your code, make sure it works, and try to find ways to improve. Once you are happy and satisfied with your code, upload it to Github, then turn in your Github link at the bottom of the page!

Don't forget. Make sure this assignment is in it's own repository. Not mixed in with others!

Refactoring Chat messages using Hashmap Storage
Objective: The aim of this assignment is to refactor the existing chat application to use a Hashmap storage system for storing messages.

Problem Statement: Currently, the chat application stores messages in a list. This is not an efficient approach as the list grows, especially in large-scale applications. Therefore, we want to refactor the application to use a Hashmap storage system, where each message is stored with the author as the key and the message as the value.



Task 1: Refactor the messages list to use a Hashmap called message_storage where the key is the author and the value is a list of messages.

Task 2: Modify the handle_message function to store messages in the message_storage Hashmap.

Task 3: Update the socketio.on('message') event handler to retrieve messages from the message_storage HashMap.

Task 4: Test **socket** in postman sending the follow JSON structure:

{
   "user":"JohnDoe",
     "message": "Hello world!"
}
task 5: Upate socket get_all_messages to get all messages sending by a specific user.

Expected Outcomes:


The chat application should now use a Hashmap storage system to store messages.
Messages should be stored under their respective author's key in the Hashmap.
The application should function as before, but with improved efficiency in handling and storing messages.
