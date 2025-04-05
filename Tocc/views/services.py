import reflex as rx
from Tocc.styles.styles import Size, Spacing
from Tocc.styles.colors import Color, TextColor

def services() -> rx.Component:
    return rx.vstack(
        rx.vstack(
            rx.text("Servicios integrales a la medida y su necesidad", size="8", font_weight="bold"),
            rx.text("Ofrecemos una amplia gama de servicios para satisfacer tus necesidades tecnológicas.", size="5"),
            spacing="2",
            width="100%",
            padding_x=Size.DEFAULT.value,
            padding_y=Size.DEFAULT.value,
            border_radius="10px",
            bg=Color.LILA.value,
            align="center",
        ),
        rx.hstack(
            rx.image(
                src=("/desarrollo.png"),
                width="100%",
                height="auto",
                alt="Desarrollo software y soluciones digitales",
                border_radius="10px",  
            ),
            rx.vstack(
                rx.text("Desarrollo de software y soluciones digitales", size="5", font_weight="bold", align="center"),
                rx.text("Desarrollo de software a la medida", size="3", align="center"),
                rx.text("Desarrollo web y móviles", size="3", align="center"),
                rx.text("Creacion de paginas web", size="3", align="center"),
            ),
        ),
        width="100%",
    )

