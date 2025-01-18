"""Adding cascade to foreign key

Revision ID: d77d7e03255d
Revises: bcd1f2fda727
Create Date: 2025-01-18 18:18:32.742920

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd77d7e03255d'
down_revision: Union[str, None] = 'bcd1f2fda727'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('posts_owner_id_fkey', 'posts', type_='foreignkey')
    op.create_foreign_key(None, 'posts', 'users', ['owner_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'posts', type_='foreignkey')
    op.create_foreign_key('posts_owner_id_fkey', 'posts', 'users', ['owner_id'], ['id'])
    # ### end Alembic commands ###
