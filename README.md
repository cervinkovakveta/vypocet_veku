# webová kalkulačka věku (Flask)
Jednoduchá webová aplikace postavená na frameworku Flask, která demonstruje propojení backendu v Pythonu s frontendovým HTML formulářem. Aplikace přijímá rok narození od uživatele a vypočítává jeho aktuální věk.

**vlastnosti**
Využití šablonovacího systému `render_template` pro zobrazení výsledků.
Implementace metod `GET` a `POST` pro příjem dat od uživatele.
Ochrana proti neplatnému vstupu (např. text místo čísla) pomocí bloku `try-except`.
Dynamický výpočet věku na straně serveru.
