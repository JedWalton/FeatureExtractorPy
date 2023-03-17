from src.feature_extractor_package.extract_title_block.titleBlock import TitleBlock


def test_titleBlock_init():
    title = "Example Title"
    date = "01/01/2021"
    scale = "1:10"
    units = "mm"
    drawn_by = "John Doe"
    orthographic_projection = "Third-angle"

    tb = TitleBlock(title, date, scale, units, drawn_by, orthographic_projection)

    assert tb.title == title
    assert tb.date == date
    assert tb.scale == scale
    assert tb.units == units
    assert tb.drawn_by == drawn_by
    assert tb.orthographic_projection == orthographic_projection
