import time
import pytest
from QuestForm import QuestForm


@pytest.fixture(scope="class")
def quest_form():
    test_quest_form = QuestForm(0, 100)
    test_quest_form.open_page()
    yield test_quest_form
    test_quest_form.close_browser()


def test_run_loop(quest_form):
    quest_form.start_task()
