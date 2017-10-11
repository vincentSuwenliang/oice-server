"""New profile columnss in user table

Revision ID: fb3d310fbd
Revises: 266bc36d7ba
Create Date: 2016-11-02 10:28:00.327167

"""

# revision identifiers, used by Alembic.
revision = 'fb3d310fbd'
down_revision = '266bc36d7ba'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql
import pyramid_safile

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('avatar_storage', pyramid_safile.FileHandleStore(length=255), nullable=False, server_default='{\"filename\": \"\", \"storage\": \"fs\", \"size\": 0, \"path\": \"\"}'))
    op.add_column('user', sa.Column('description', sa.Unicode(length=1024), nullable=False, server_default=""))
    op.add_column('user', sa.Column('display_name', sa.Unicode(length=128), nullable=False))
    op.add_column('user', sa.Column('language', sa.Unicode(length=5), nullable=False, server_default="zh_HK"))
    # Set all existing display_name to the email
    conn = op.get_bind()
    conn.execute("""
        UPDATE user SET display_name = email;""")
    conn.execute("""
        UPDATE user SET avatar_storage = '{"filename": "", "storage": "fs", "size": 0, "path": ""}'""")

    op.create_unique_constraint("uq_display_name", 'user', ['display_name'])
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint("uq_display_name", 'user', type_='unique')
    op.drop_column('user', 'language')
    op.drop_column('user', 'display_name')
    op.drop_column('user', 'description')
    op.drop_column('user', 'avatar_storage')
    ### end Alembic commands ###