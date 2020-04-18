#!/usr/bin/env python
class Catalog:
    """Локаторы для каталога товаром под обычным пользователем"""

    HOME = "#product-category ul > li > a > i.fa-home"

    """List of products if 'Cameras" is selected'"""

    DESKTOPS = "#column-left > div.list-group a:nth-child(1)"
    LAPTOPS_AND_NOTEBOOKS = "#column-left > div.list-group a:nth-child(2)"
    COMPONENTS = "#column-left > div.list-group a:nth-child(3)"
    TABLETS = "#column-left > div.list-group a:nth-child(4)"
    SOFTWARE = "#column-left > div.list-group a:nth-child(5)"
    PHONES_AND_PDAS = "#column-left > div.list-group a:nth-child(6)"
    CAMERAS = "#column-left > div.list-group a:nth-child(7)"
    MP3_PLAYERS = "#column-left > div.list-group a:nth-child(8)"

    """Refine search"""

    LIST_VIEW = "#list-view"
    GRID_VIEW = "#grid-view"
    PRODUCT_COMPARE = "#compare-total"
    SORT_BY = "#input-sort"
    SHOW = "#input-limit"
