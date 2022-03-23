"""empty message

Revision ID: 199023ec1322
Revises: 230195f46794
Create Date: 2022-02-27 19:27:48.566463

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '199023ec1322'
down_revision = '230195f46794'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('share',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('share')
    # ### end Alembic commands ###
