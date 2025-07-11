"""Add default_staff_id to task_template

Revision ID: 9a81aef09e90
Revises: 704d12e9a1f8
Create Date: 2025-04-27 17:29:49.520107

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9a81aef09e90'
down_revision = '704d12e9a1f8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('task_template', schema=None) as batch_op:
        batch_op.add_column(sa.Column('default_staff_id', sa.Integer(), nullable=True))
        batch_op.create_index(batch_op.f('ix_task_template_default_staff_id'), ['default_staff_id'], unique=False)
        # batch_op.create_foreign_key(None, 'staff', ['default_staff_id'], ['id'])
        batch_op.create_foreign_key('fk_task_template_default_staff', 'staff', ['default_staff_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('task_template', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_index(batch_op.f('ix_task_template_default_staff_id'))
        batch_op.drop_column('default_staff_id')

    # ### end Alembic commands ###
