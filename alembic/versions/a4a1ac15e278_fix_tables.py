"""fix  tables

Revision ID: a4a1ac15e278
Revises: 62bfb33ae51c
Create Date: 2024-07-09 07:05:08.680366

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a4a1ac15e278'
down_revision: Union[str, None] = '62bfb33ae51c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('2024-07-09', sa.String(), nullable=False))
    op.drop_column('users', "<class 'datetime.date'>")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column("<class 'datetime.date'>", sa.VARCHAR(), autoincrement=False, nullable=False))
    op.drop_column('users', '2024-07-09')
    # ### end Alembic commands ###
