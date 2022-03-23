"""empty message

Revision ID: 3642a431c03c
Revises: 
Create Date: 2022-02-26 10:27:38.972346

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3642a431c03c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('email_capture',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('capture', sa.String(length=10), nullable=False),
    sa.Column('creat_time', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('email_capture')
    # ### end Alembic commands ###
