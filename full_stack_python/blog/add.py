import reflex as rx

from ..ui.base import base_page
from . import forms


def blog_post_add_page() -> rx.Component:
    my_form = forms.blog_post_add_form()
    my_child = rx.vstack(
        rx.heading("New Blog Spot", size="9"),
        rx.desktop_only(rx.box(my_form, id="my-form-box", width="35vw")),
        rx.mobile_and_tablet(rx.box(my_form, id="my-form-box", width="65vw")),
        spacing="5",
        align="center",
        min_height="95vh",
    )
    return base_page(my_child, hide_navbar=False)
