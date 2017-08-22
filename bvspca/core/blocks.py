from wagtail.contrib.table_block.blocks import TableBlock
from wagtail.wagtaildocs.blocks import DocumentChooserBlock
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailembeds.blocks import EmbedBlock
from wagtail.wagtailcore.blocks import (
    CharBlock, ChoiceBlock, RichTextBlock, StreamBlock, StructBlock, TextBlock,
    RawHTMLBlock)


class ImageBlock(StructBlock):
    image = ImageChooserBlock(required=True)
    caption = CharBlock(required=False)
    attribution = CharBlock(required=False)

    class Meta:
        label = 'Image'
        icon = 'image'
        template = 'core/blocks/image_block.html'


class DocumentBlock(StructBlock):
    document = DocumentChooserBlock(required=True)
    title = CharBlock(required=False)

    class Meta:
        label = 'Document'
        icon = 'document'
        template = 'core/blocks/image_block.html'


class HeadingBlock(StructBlock):
    heading_text = CharBlock(classname='title', required=True)
    size = ChoiceBlock(choices=[
        ('', 'Select a header size'),
        ('h2', 'H2'),
        ('h3', 'H3'),
        ('h4', 'H4')
    ], blank=True, required=False)

    class Meta:
        label = 'Heading'
        icon = 'title'
        template = 'core/blocks/heading_block.html'


class BlockQuote(StructBlock):
    text = TextBlock()
    attribute_name = CharBlock(
        blank=True, required=False, label='e.g. Mary Berry')

    class Meta:
        label = 'Quote'
        icon = 'fa-quote-left'
        template = 'core/blocks/quote-block.html'


class ContentTableBlock(StructBlock):
    table = TableBlock()
    caption = CharBlock(required=False)

    class Meta:
        label = 'Table'
        icon = 'fa-table'
        template = 'core/blocks/table_block.html'


class ContentRawHTML(StructBlock):
    html = RawHTMLBlock()

    class Meta:
        label = 'Raw HTML'
        icon = 'fa-code'
        template = 'core/blocks/raw_html_block.html'


class ContentStreamBlock(StreamBlock):
    heading_block = HeadingBlock()
    paragraph_block = RichTextBlock(
        label='Paragraph',
        icon='fa-paragraph',
    )
    image_block = ImageBlock()
    block_quote = BlockQuote()
    embed_block = EmbedBlock(
        label='Embedded Media',
        help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks',
        icon='fa-external-link-square',
    )
    table_block = ContentTableBlock()
    raw_html = ContentRawHTML()