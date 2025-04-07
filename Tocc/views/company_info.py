import reflex as rx
from Tocc.styles.styles import Size
from Tocc.styles.colors import Color

def company_info() -> rx.Component:
    return rx.vstack(
        rx.vstack(
            rx.text("Nosotros", size="8", font_weight="bold"),
            rx.text("Conoce nuestra misión, visión y políticas de calidad que nos definen como empresa tecnológica.", size="5"),
            spacing="2",
            width="100%",
            padding_x=Size.DEFAULT.value,
            padding_y=Size.DEFAULT.value,
            border_radius="10px",
            bg=Color.LILA.value,
            align="center",
        ),
        rx.vstack(
            rx.text("MISIÓN", size="5", font_weight="bold", align="center"),
            rx.text(
                "En Tocc Technology, nuestra misión es desarrollar soluciones tecnológicas innovadoras, confiables y a la medida, " \
                "impulsando la transformación digital de empresas en Colombia y Latinoamérica. Nos especializamos en desarrollo de software, " \
                "infraestructura IT, mantenimiento de hardware y asesoría legal en tecnología, garantizando seguridad, eficiencia y " \
                "satisfacción en cada proyecto. A través de metodologías ágiles, inteligencia artificial y tecnologías emergentes, cr" \
                "eamos productos escalables y de alto impacto, siempre enfocados en entender a profundidad las necesidades de nuestros " \
                "clientes para ofrecer soluciones eficientes y una experiencia centrada en el usuario.",
                size="3",
                text_align="center",
            ),
            width="100%",
            padding=Size.DEFAULT.value,
            border_radius="10px",
            bg=Color.LILA.value,
        ),
        rx.vstack(
            rx.text("VISIÓN", size="5", font_weight="bold", align="center"),
            rx.text(
                "Para 2030, Tocc Technology será una empresa líder en tecnología y asesoría digital en América Latina, " \
                "reconocida por su excelencia en servicio, innovación continua y capacidad de adaptación a los cambios del mercado. " \
                "Nos consolidaremos como referentes en desarrollo de software, inteligencia artificial y soluciones digitales, " \
                "impactando diversas industrias y contribuyendo al crecimiento económico y tecnológico de la región. " \
                "Aspiramos a ser la primera opción para empresas y profesionales que buscan soluciones tecnológicas seguras, " \
                "eficientes y adaptadas a sus necesidades. Nuestro compromiso con la calidad, la sostenibilidad y " \
                "la evolución constante de nuestros servicios nos permitirá expandirnos globalmente, manteniendo siempre el " \
                "enfoque en la satisfacción del cliente.",
                size="3",
                text_align="center",
            ),
            width="100%",
            padding=Size.DEFAULT.value,
            border_radius="10px",
            bg=Color.LILA.value,
        ),
        rx.vstack(
            rx.text("POLÍTICAS DE CALIDAD", size="5", font_weight="bold", align="center"),
            rx.text("1. Ofrecemos soluciones tecnológicas innovadoras, eficientes y de alta calidad, adaptadas a las necesidades de nuestros " \
            "clientes.", size="3", text_align="center"),
            rx.text("2. Garantizamos el cumplimiento de estándares y normativas internacionales en seguridad informática y desarrollo digital, " \
            "asegurando la confiabilidad de nuestras soluciones.", size="3", text_align="center"),
            rx.text("3. Brindamos un servicio cercano, con soporte técnico especializado, para garantizar la satisfacción y confianza de " \
            "nuestros clientes.", size="3", text_align="center"),
            rx.text("4. Impulsamos la optimización constante de nuestros procesos mediante la integración de nuevas tecnologías y " \
            "metodologías ágiles.", size="3", text_align="center"),
            rx.text("5. Aplicamos las mejores prácticas en ciberseguridad para resguardar la información de nuestros clientes y asegurar " \
            "la confidencialidad de sus datos.", size="3", text_align="center"),
            width="100%",
            padding=Size.DEFAULT.value,
            border_radius="10px",
            bg=Color.LILA.value,
        ),
        width="100%",
    )
