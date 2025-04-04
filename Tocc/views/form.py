import reflex as rx
from Tocc.styles.styles import Size, Spacing
from Tocc.styles.colors import Color, TextColor

class FormState(rx.State):

    @rx.event
    def submit(self, form_data):
        return rx.toast(form_data)

def form() -> rx.Component:
    return rx.vstack(
            rx.text("Contactanos", size="9", font_weight="bold"),
            rx.text("No dudes en ponerte en contacto con nosotros.", size="5"),
            rx.hstack(
                rx.box(
                    rx.image(
                        src="/contactanos.png",
                        width="100%",
                        height="100%",
                        alt="Contacto",
                        border_radius="10px",
                    ),
                    padding_y=Size.DEFAULT.value,
                    padding_x=Size.SMALL.value,
                    flex="1",
                ),
                rx.vstack(
                    rx.form(
                        rx.vstack(
                            rx.text("Dejanos tu mensaje", size="8", font_weight="bold", align="center", margin_bottom=Size.DEFAULT.value),
                            rx.input(placeholder="Nombre", name="name"),
                            rx.input(placeholder="Email ", name="email"),
                            rx.select(
                                ["Desarrollo de sofware y soluciones digitales",
                                 "Ciberseguridad y protección de datos",
                                 "Consultorías y asesorías tecnológicas",
                                 "Soluciones de hardawe y equipamiento tecnológico",
                                 "Otros"],
                                 font_weight="bold",
                                 name="select",
                                 placeholder="Selecciona un servicio",
                            ),
                            rx.text_area(placeholder="Mensaje", name="message"),
                            rx.button("Enviar", 
                                    type_="submit", 
                                    width="100%",
                                    bg=Color.PURPLE.value, 
                                    color=TextColor.LIGHT.value, 
                                    size="4", 
                                    border="none",
                                    box_shadow = "none",
                                    padding_x=Size.SMALL.value, 
                                    padding_y=Size.SMALL.value
                            ),
                            width="100%",
                            height="100%",
                            padding_x=Size.DEFAULT.value,
                            padding_y=Size.BIG.value,
                            align_items="stretch",
                            border_radius="10px",
                        ),
                        width="100%",
                        height="100%",
                        spacing="3",
                        padding=Size.DEFAULT.value,
                        on_submit=FormState.submit,
                        bg=Color.LILA.value,
                        aling="center",
                        border_radius="10px",
                    ),
                    padding_y=Size.DEFAULT.value,
                    padding_x=Size.DEFAULT.value,
                    flex="1",
                    align="center",
                    widht="100%",
                    height="100%",
                ),  
            width="100%",
            padding=Size.DEFAULT.value,
            border_radius=Size.SMALL.value,
            bg=Color.PURPLE.value,
            ),
        width="100%",
        padding_x=Size.DEFAULT.value,
        padding_y=Size.DEFAULT.value,
        border_radius=Size.SMALL.value,
        bg=Color.LILA.value,
        align="center",
    )