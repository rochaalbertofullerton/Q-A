from getquestion.getquestion import get_question
from Lambdatest.lambdasql import post_question
from deletequestion.deletequestion import delete_question

question_id = ''

def setup_function():
    global question_id

    event = { 'question': 'test_delete_question', 'author': 'tester' }
    result = post_question(event)
    question_id = result[0][0]
    

def test_delete_question():
    global question_id

    event = { 'idquestion': question_id }
    response = delete_question(event)

    assert response == 'deleted'