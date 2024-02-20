"""empty message

Revision ID: 7bae22a48842
Revises: 80c36ed40ebb
Create Date: 2024-02-16 16:31:20.531366

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7bae22a48842'
down_revision = '80c36ed40ebb'
branch_labels = None
depends_on = None


def upgrade():
    # remove all except current submission for each business
    op.execute("delete from submission where id not in (select id from (select business_identifier, max(id) as id from submission group by business_identifier) as current_records)")
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('submission', schema=None) as batch_op:
        batch_op.alter_column('business_identifier',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)
        batch_op.create_unique_constraint(None, ['business_identifier'])

    with op.batch_alter_table('submission_history', schema=None) as batch_op:
        batch_op.alter_column('business_identifier',
               existing_type=sa.VARCHAR(length=255),
               nullable=False,
               autoincrement=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('submission_history', schema=None) as batch_op:
        batch_op.alter_column('business_identifier',
               existing_type=sa.VARCHAR(length=255),
               nullable=True,
               autoincrement=False)

    with op.batch_alter_table('submission', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.alter_column('business_identifier',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)

    # ### end Alembic commands ###
