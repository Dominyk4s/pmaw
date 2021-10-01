from .config import tape, reddit, post_ids, comment_ids
from pmaw import PushshiftAPI
import pytest

@tape.use_cassette('test_comment_praw_ids')
def test_safe_exit_praw():
  with pytest.raises(NotImplementedError):
    api_praw = PushshiftAPI(praw=reddit)
    comments = api_praw.search_comments(ids=comment_ids, safe_exit=True)

@tape.use_cassette('test_submission_search_ids')
def test_asc_sort():
  with pytest.raises(NotImplementedError):
    api = PushshiftAPI()
    posts = api.search_submissions(ids=post_ids, sort='asc')

