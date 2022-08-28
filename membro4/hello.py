from .styled_text import StyledText


def hello():
    styled_text_engine = StyledText()
    return styled_text_engine.render("""<br/><remove-indent>
        Olá, eu sou o <text light_blue><bold>Geovane</></><br/>
        Tenho <text light_cyan><bold>20</></> anos.<br/>

        Atualmente meus hobbies são <bold><text light_green>programação</></>
        e <bold><text light_green>leitura</></>.<br/>

        Experiência prévia de programação: Programei para muitas coisas,
        principalmente relacionado à <bold><text cyan>Web</></>.<br/>

        Nessa disciplina, espero melhorar as habilidades de <text light_yellow><bold>programação orientada a objetos</></> e fazer um jogo
        <bold>legal</bold>.<br/>
    </>""")
