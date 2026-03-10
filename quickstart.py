from instapy import InstaPy
from instapy import smart_run

session = InstaPy(
    username="YOUR_INSTAGRAM_USERNAME",
    password="YOUR_INSTAGRAM_PASSWORD",
    headless_browser=True
)

with smart_run(session):

    # activity limits
    session.set_quota_supervisor(
        enabled=True,
        peak_likes_daily=50,
        peak_comments_daily=10,
        peak_follows_daily=20
    )

    # like posts from hashtags
    session.like_by_tags(
        ["travel","nature","photography"],
        amount=20
    )

    # follow some users
    session.follow_by_tags(
        ["travel","nature"],
        amount=10
    )

    # optional comment
    session.set_do_comment(True, percentage=20)

    session.set_comments([
        "Nice post!",
        "Great shot!",
        "Awesome content!"
    ]) 