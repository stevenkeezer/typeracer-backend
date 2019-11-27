"""empty message

Revision ID: 8314db0359a0
Revises: 205a8d2d7657
Create Date: 2019-11-26 22:04:44.078706

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8314db0359a0'
down_revision = '205a8d2d7657'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('score', sa.Column('excerpt_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'score', 'excerpts', ['excerpt_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'score', type_='foreignkey')
    op.drop_column('score', 'excerpt_id')
    # ### end Alembic commands ###