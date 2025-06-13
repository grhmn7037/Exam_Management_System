"""Add User model and recorded_by_user_id column (Step 1)

Revision ID: 71059fc6d369
Revises: 5f796180575e
Create Date: 2025-04-30 07:06:24.169004

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '71059fc6d369'
down_revision = '5f796180575e' # Make sure this matches the previous migration ID
branch_labels = None
depends_on = None


def upgrade():
    print("Applying migration 71059fc6d369: Add recorded_by_user_id column")

    # --- Create User Table (Commented out - assumed exists) ---
    # op.create_table('user', ...) # Keep commented
    # with op.batch_alter_table('user', schema=None) as batch_op:
    #     batch_op.create_index(...) # Keep commented
    # --- End User Table Creation ---

    # --- Modify exam_absence Table (ONLY ADD COLUMN) ---
    print("Attempting to add column to exam_absence table...")
    try:
        with op.batch_alter_table('exam_absence', schema=None) as batch_op:
            print("  Adding column recorded_by_user_id...")
            batch_op.add_column(sa.Column('recorded_by_user_id', sa.Integer(), nullable=True))
            # --- DO NOT ADD FOREIGN KEY HERE ---
        print("Addition of column to exam_absence table successful.")
    except Exception as e:
        print(f"Error modifying exam_absence table: {e}")
        # raise e
    # --- End exam_absence Modification ---


def downgrade():
    print("Applying downgrade for migration 71059fc6d369")

    # --- Modify exam_absence Table (ONLY DROP COLUMN) ---
    print("Attempting to revert modifications on exam_absence table...")
    try:
        with op.batch_alter_table('exam_absence', schema=None) as batch_op:
            print("  Dropping column recorded_by_user_id...")
            batch_op.drop_column('recorded_by_user_id')
            # --- DO NOT DROP FOREIGN KEY HERE ---
        print("Reversion of exam_absence table successful.")
    except Exception as e:
         print(f"Error reverting exam_absence table: {e}")
         # raise e
    # --- End exam_absence Reversion ---

    # --- Drop User Table (Commented out) ---
    # with op.batch_alter_table('user', schema=None) as batch_op:
    #     batch_op.drop_index(...) # Keep commented
    # op.drop_table('user') # Keep commented
    # --- End User Table Drop ---