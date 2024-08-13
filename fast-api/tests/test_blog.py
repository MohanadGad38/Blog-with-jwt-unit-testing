from blog import schemas, models
from blog.database import get_db
from sqlalchemy.orm import Session
from typing import List
from fastapi import Depends
from blog.repository import blog
from unittest.mock import MagicMock
import pytest


@pytest.mark.asyncio
async def test_get_all():
    # Create a mock database session
    fake_db_session: MagicMock = MagicMock()

    # Create some fake blog data
    fake_blogs: List[MagicMock] = [
        MagicMock(id=1, title="Blog 1", body="Body 1"),
        MagicMock(id=2, title="Blog 2", body="Body 2")
    ]

    # Mock the behavior of the database session to return the fake blog data
    fake_db_session.query.return_value.all.return_value = fake_blogs

    # Call the get_all function with the mocked database session
    result: blog = await blog.get_all(db=fake_db_session)
    # Assert that the result matches the fake blog data
    assert result == fake_blogs


@pytest.mark.asyncio
async def test_get_one():
    fake_db_session: MagicMock = MagicMock()

    fake_blog = MagicMock(id=1, title="Test Blog", body="Test Body", user_id=1)
    fake_db_session.query.return_value.filter.return_value.first.return_value = fake_blog

    result: blog = await blog.get_one(1, db=fake_db_session)

    assert result == fake_blog
