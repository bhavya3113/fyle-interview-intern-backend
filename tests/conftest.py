import pytest
import json
from tests import app
from core.models.assignments import Assignment, AssignmentStateEnum
from core import db

@pytest.fixture
def client():
    return app.test_client()


@pytest.fixture
def h_student_1():
    headers = {
        'X-Principal': json.dumps({
            'student_id': 1,
            'user_id': 1
        })
    }

    return headers


@pytest.fixture
def h_student_2():
    headers = {
        'X-Principal': json.dumps({
            'student_id': 2,
            'user_id': 2
        })
    }

    return headers


@pytest.fixture
def h_teacher_1():
    headers = {
        'X-Principal': json.dumps({
            'teacher_id': 1,
            'user_id': 3
        })
    }

    return headers


@pytest.fixture
def h_teacher_2():
    headers = {
        'X-Principal': json.dumps({
            'teacher_id': 2,
            'user_id': 4
        })
    }

    return headers


@pytest.fixture
def h_principal():
    headers = {
        'X-Principal': json.dumps({
            'principal_id': 1,
            'user_id': 5
        })
    }

    return headers

@pytest.fixture
def sub_assign():
    assignment = Assignment.get_by_id(4)
    assignment.state = AssignmentStateEnum.SUBMITTED
    assignment.grade = None
    db.session.flush()

    yield assignment

    assignment.state = AssignmentStateEnum.DRAFT
    db.session.flush()

@pytest.fixture
def draft_assign():
    assignment = Assignment.get_by_id(2)
    prev_state = assignment.state
    prev_grade = assignment.grade
    assignment.state = AssignmentStateEnum.DRAFT
    assignment.grade = None
    db.session.flush()

    yield assignment

    assignment.state = prev_state
    assignment.grade = prev_grade
    db.session.flush()

@pytest.fixture
def cleanup_assignment_transaction():
    # This fixture ensures a rollback after each test that uses it
    yield
    db.session.rollback()