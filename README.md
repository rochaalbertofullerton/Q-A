
https://11mhxjzim1.execute-api.us-west-1.amazonaws.com/dev/postquestion
use api to post question ; post
input :
{
	“question”: “    ”
}


https://lmftmlwlwc.execute-api.us-west-1.amazonaws.com/dev/postanswer
use api to post answer, must pass the idquestion and answer; post
input
{
	“idquestion” : “      ”,
	“answer: “      “
}

https://mierc8uxb6.execute-api.us-west-1.amazonaws.com/dev/getquestion
use api to get question, get
 add them as params question=A STRING TO SERACH THE DATABASE

https://mek4qh4vgg.execute-api.us-west-1.amazonaws.com/dev/getanswer
use api to get answer , get
 add them as params idquestion=A STRING TO SERACH THE DATABASE

 https://u2sgx1z365.execute-api.us-west-1.amazonaws.com/dev/deletequestion
use api to delete a question, detele 
{
	“idquestion” : “      ”
}

https://qjd7xu5yu6.execute-api.us-west-1.amazonaws.com/dev/deleteanswer
use api to delete answer, delete
{
	"idanswer" : "  " 
}
