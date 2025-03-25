import reflex as rx

from ..ui.base import base_page


def blog_post_detail_page() -> rx.Component:
    my_child = rx.vstack(
        rx.heading("Blog Post Detail", size="9"),
        rx.text(
            "Blog Post Entry",
        ),
        spacing="5",
        justify="center",
        align="center",
        min_height="85vh",
        id="my-child",
    )
    return base_page(my_child, hide_navbar=False)
