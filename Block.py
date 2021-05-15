# https://developers.notion.com/reference/block

from datetime import datetime


class Block:
    def __init__(self, block_id, block_type, time_created, time_last_edited, children):
        self.object = 'block'
        self.id = block_id
        self.type = block_type
        self.created_time = datetime.strptime(time_created, "%Y-%m-%dT%H:%M:%S%z")
        self.last_edited_time = datetime.strptime(time_last_edited, "%Y-%m-%dT%H:%M:%S%z")
        self.has_children = children

    class BlockType:
        Paragraph = 'paragraph'
        Heading_1 = 'heading_1'
        Heading_2 = 'heading_2'
        Heading_3 = 'heading_3'
        Bulleted_list_item = 'bulleted_list_item'
        Numbered_list_item = 'numbered_list_item'
        To_do = 'to_do'
        Toggle = 'toggle'
        Child_page = 'child_page'
        Unsupported = 'unsupported'


class Paragraph(Block):
    def __init__(self, block_id, time_created, time_last_edited, children, text_arr, children_arr):
        super().__init__(block_id, Block.BlockType.Paragraph, time_created, time_last_edited, children)
        self.text = text_arr
        self.children = children_arr


class Heading1(Block):
    def __init__(self, block_id, time_created, time_last_edited, children, text_arr):
        super().__init__(block_id, Block.BlockType.Heading_1, time_created, time_last_edited, children)
        self.text = text_arr


class Heading2(Block):
    def __init__(self, block_id, time_created, time_last_edited, children, text_arr):
        super().__init__(block_id, Block.BlockType.Heading_2, time_created, time_last_edited, children)
        self.text = text_arr


class Heading3(Block):
    def __init__(self, block_id, time_created, time_last_edited, children, text_arr):
        super().__init__(block_id, Block.BlockType.Heading_3, time_created, time_last_edited, children)
        self.text = text_arr


class BulletedListItem(Block):
    def __init__(self, block_id, time_created, time_last_edited, children, text_arr, children_arr):
        super().__init__(block_id, Block.BlockType.Bulleted_list_item, time_created, time_last_edited, children)
        self.text = text_arr
        self.children = children_arr


class NumberedListItem(Block):
    def __init__(self, block_id, time_created, time_last_edited, children, text_arr, children_arr):
        super().__init__(block_id, Block.BlockType.Numbered_list_item, time_created, time_last_edited, children)
        self.text = text_arr
        self.children = children_arr


class ToDo(Block):
    def __init__(self, block_id, time_created, time_last_edited, children, text_arr, children_arr, is_checked=False):
        super().__init__(block_id, Block.BlockType.To_do, time_created, time_last_edited, children)
        self.text = text_arr
        self.checked = is_checked
        self.children = children_arr


class Toggle(Block):
    def __init__(self, block_id, time_created, time_last_edited, children, text_arr, children_arr):
        super().__init__(block_id, Block.BlockType.Toggle, time_created, time_last_edited, children)
        self.text = text_arr
        self.children = children_arr


class ChildPage(Block):
    def __init__(self, block_id, time_created, time_last_edited, children, page_title):
        super().__init__(block_id, Block.BlockType.Child_page, time_created, time_last_edited, children)
        self.title = page_title
