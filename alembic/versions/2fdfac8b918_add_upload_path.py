"""Add upload path

Revision ID: 2fdfac8b918
Revises: 230feeb5b86
Create Date: 2015-06-09 14:17:39.222173

"""

# revision identifiers, used by Alembic.
revision = '2fdfac8b918'
down_revision = '230feeb5b86'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('upload', sa.Column('path', sa.String(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('upload', 'path')
    ### end Alembic commands ###
