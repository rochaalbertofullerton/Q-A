from getquestion.getquestion import get_question
from Lambdatest.lambdasql import post_question
from deletequestion.deletequestion import delete_question

question_id = ''
question = 'test_get_question'
author = 'tester'

def setup_function():
    global question_id, question

    event = { 'question': question, 'author': author }
    result = post_question(event)
    question_id = result[0][0]
    

def teardown_function():
    global question_id

    event = { 'idquestion': question_id }
    delete_question(event)


def test_get_question():
    global question_id, question

    event = { 'question': question }

    questions = get_question(event)
    data = questions[0]

    assert len(questions) == 1
    assert data['idquestion'] == question_id
    assert data['question'] == question
    assert data['author'] == author