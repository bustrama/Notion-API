from APIs import KEYS
from Notion import Notion


notion = Notion(KEYS.NOTION_TOKEN)
db_id = KEYS.DATABASE_ID

res = notion.queryDatabase(db_id)
db = notion.getDatabase(db_id)
