"""empty message

Revision ID: 0a5356f460a4
Revises: 7bae22a48842
Create Date: 2024-06-21 08:23:37.778114

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0a5356f460a4'
down_revision = '7bae22a48842'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('submission', schema=None) as batch_op:
        batch_op.drop_constraint('submission_business_identifier_key', type_='unique')
        batch_op.create_index(batch_op.f('ix_submission_business_identifier'), ['business_identifier'], unique=True)

    with op.batch_alter_table('submission_history', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_submission_history_business_identifier'), ['business_identifier'], unique=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('submission_history', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_submission_history_business_identifier'))

    with op.batch_alter_table('submission', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_submission_business_identifier'))
        batch_op.create_unique_constraint('submission_business_identifier_key', ['business_identifier'])

    # ### end Alembic commands ###
