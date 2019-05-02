from Lambdatest.lambdasql import post_question
from getanswer.getanswer import get_answer
from postanswer.postanswer import post_answer
from deletequestion.deletequestion import delete_question
from deleteanswer.deleteanswer import delete_answer

answer_id = ''
question_id = ''
author = 'tester'

def setup_function():
    global question_id, answer_id, author

    # post a question
    event = { 'question': 'we are testing', 'author': author }
    result = post_question(event)
    question_id = result[0][0]

    # post an answer to that question
    event = { 'idquestion': question_id, 'answer': 'testing', 'author': author }
    result = post_answer(event)
    answer_id = result[0][0]


def teardown_function():
    global question_id, answer_id

    event = { 'idanswer': answer_id }
    delete_answer(event)

    event = { 'idquestion': question_id }
    delete_question(event)
    

def test_get_answer():
    global question_id, answer_id

    event = { 'idquestion': question_id }
    answers = get_answer(event)

    assert len(answers) > 0

    a = answers[0]

    assert a['idanswer'] == answer_id
    assert a['author'] == author
    assert a['idquestion'] == question_id
    
    
    assert type(answer_id) is str