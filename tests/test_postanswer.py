from Lambdatest.lambdasql import post_question
from postanswer.postanswer import post_answer
from deletequestion.deletequestion import delete_question
from deleteanswer.deleteanswer import delete_answer

answer_id = ''
question_id = ''

def setup_function():
    global question_id

    event = { 'question': test_post_answer, 'author': 'tester' }
    result = post_question(event)
    question_id = result[0][0]


def teardown_function():
    global question_id, answer_id

    event = { 'idquestion': question_id }
    delete_question(event)

    event = { 'idanswer': answer_id }
    delete_answer(event)
    

def test_post_answer():
    global question_id, answer_id
    
    event = { 'idquestion': question_id, 'answer': 'testing', 'author': 'tester' }

    result = post_answer(event)
    answer_id = result[0][0]
    assert type(answer_id) is str