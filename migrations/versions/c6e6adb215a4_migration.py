"""migration.

Revision ID: c6e6adb215a4
Revises: 23fa85aa32b2
Create Date: 2022-05-11 01:12:24.609379

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c6e6adb215a4'
down_revision = '23fa85aa32b2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('pitches', 'title')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pitches', sa.Column('title', sa.VARCHAR(length=255), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
