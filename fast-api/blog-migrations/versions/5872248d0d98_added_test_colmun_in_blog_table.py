"""added test colmun in blog table

Revision ID: 5872248d0d98
Revises: d615a590334c
Create Date: 2024-08-19 03:33:27.429680

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5872248d0d98'
down_revision: Union[str, None] = 'd615a590334c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Blogs', sa.Column('test', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Blogs', 'test')
    # ### end Alembic commands ###