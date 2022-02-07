"""removed column comment from pictches table

Revision ID: 2ebe48d41784
Revises: 
Create Date: 2022-02-07 14:15:45.082295

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2ebe48d41784'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('comment', sa.Text(), nullable=False))
    op.drop_column('comments', 'comments')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('comments', sa.TEXT(), autoincrement=False, nullable=False))
    op.drop_column('comments', 'comment')
    # ### end Alembic commands ###