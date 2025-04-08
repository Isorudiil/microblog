"""add language to posts

Revision ID: 880f0470220f
Revises: 30b621746bc5
Create Date: 2025-04-08 10:20:28.382061

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '880f0470220f'
down_revision = '30b621746bc5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.add_column(sa.Column('language', sa.String(length=5), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.drop_column('language')

    # ### end Alembic commands ###
