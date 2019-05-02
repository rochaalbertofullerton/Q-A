from Lambdatest.lambdasql import post_question
from getanswer.getanswer import get_answer
from postanswer.postanswer import post_answer
from deletequestion.deletequestion import delete_question
from deleteanswer.deleteanswer import delete_answer

answer_id = ''
question_id = ''

def setup_function():
    global question_id, answer_id

    # post a question
    event = { 'question': 'we are testing', 'author': 'tester' }
    result = post_question(event)
    question_id = result[0][0]

    # post an answer to that question
    event = { 'idquestion': question_id, 'answer': 'testing', 'author': 'tester' }
    result = post_answer(event)
    answer_id = result[0][0]


def teardown_function():
    global question_id

    event = { 'idquestion': question_id }
    delete_question(event)
    

def test_delete_answer():
    global answer_id

    event = { 'idanswer': answer_id }
    result = delete_answer(event)

    assert result == 'deleted'