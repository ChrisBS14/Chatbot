$(document).ready(function(){

    //add the robot icon
    var robot_svg = `
        <svg width="20" height="20">
            <image class="robot" xlink:href="/robot.svg" width="20" height="20" />
        </svg>
    `

    //add the user icon
    var user_svg = `
        <svg width="20" height="20">
            <image class="user" xlink:href="/person.svg" width="20" height="20" />
        </svg>
    `

    //define variables
    var chat_button = $("#chat_button");
    var chat_input = $("#chat_input");
    var chat = $("#chat");

    //start message from bot
    var text = robot_svg + " - Hello, my name is Chatbotty. How can I help you? Write 'help' if you don't know how to proceed."

    //set the chatbot start message
    chat.html(text);

    chat_button.on("click", function(){

        //get user input value
        answer = chat_input.val();

        //if the user input is bye redirect
        if(answer === "bye"){
            location.replace("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        }

        //if the user input is bye redirect
        if(answer === "website"){
            location.replace("https://itsolutions555.com/")
        }

        //clear input field
        chat_input.val("");

        //add user input to chat with user icon
        text += "<br>" + user_svg + " - " + answer;

        //add chat text to chat object html
        chat.html(text);

        //send user input to server(api) as json/post
        $.ajax({
            url: "/api/answers",
            type: "POST",
            data: JSON.stringify({answer: answer}),
            contentType: "application/json",

            //if successfull
            success: function(data){

                //parse the data to JSON
                data = JSON.parse(data);

                //add the answer to the text
                text += "<br>" + robot_svg + " - " + data.question;

                //add the text to the chat object html
                chat.html(text);
            }
        })
    });

    //if enter is pressed sumbit the input
    chat_input.on("keypress", function (e){
        if(e.which === 13){
            chat_button.click();
        }
    });
});
