from Lambdatest.lambdasql import post_question
from deletequestion.deletequestion import delete_question

question_id = ''

def teardown_function():
    global question_id

    event = { 'idquestion': question_id }
    delete_question(event)


def test_post_question():
    global question_id
    
    event = { 'question': 'Testing...123', 'author': 'tester' }

    result = post_question(event)
    question_id = result[0][0]
    assert type(question_id) is str