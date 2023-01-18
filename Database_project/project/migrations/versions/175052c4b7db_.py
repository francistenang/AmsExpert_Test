"""empty message

Revision ID: 175052c4b7db
Revises: ddd8b31e073b
Create Date: 2021-11-05 18:41:07.865479

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '175052c4b7db'
down_revision = 'ddd8b31e073b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Expert', 'numero')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Expert', sa.Column('numero', sa.INTEGER(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###