# Esto es un diccionario de tuplas que contiene el ejercicio, el musculo que trabaja
# y cada uno de sus multiplicadores

EJERCICIOS = {

#   EJERCICIO              |   MUSCULO   multi1 multi2 multi3

    # PIERNAS
    "Sentadilla":             ("piernas", 0.8,  1.4,  2.0),
    "Sentadilla frontal":     ("piernas", 0.6,  1.1,  1.6),
    "Sentadilla bulgara":     ("piernas", 0.4,  0.7,  1.0),
    "Peso muerto":            ("piernas", 1.0,  1.7,  2.4),
    "Peso muerto rumano":     ("piernas", 0.7,  1.1,  1.6),
    "Hip thrust":             ("piernas", 1.0,  1.8,  2.7),
    "Prensa de piernas":      ("piernas", 1.5,  2.2,  3.0),
    "Curl femoral":           ("piernas", 0.35, 0.5,  0.7),
    "Extension cuadriceps":   ("piernas", 0.4,  0.6,  0.9),

    # PECHO
    "Press banca":            ("pecho",   0.7,  1.0,  1.5),
    "Press inclinado barra":  ("pecho",   0.6,  0.8,  1.2),
    "Press declinado barra":  ("pecho",   0.7,  1.0,  1.4),
    "Fondos":                 ("pecho",   0.8,  1.0,  1.4),
    "Flexiones":              ("pecho",   0.6,  0.7,  1.0),
    "Cruces polea":           ("pecho",   0.18, 0.25, 0.4),

    # ESPALDA
    "Dominadas":              ("espalda", 0.8,  1.0,  1.3),
    "Jalon al pecho":         ("espalda", 0.5,  0.75, 1.0),
    "Remo barra":             ("espalda", 0.6,  0.85, 1.2),
    "Remo mancuerna":         ("espalda", 0.25, 0.4,  0.6),
    "Remo polea":             ("espalda", 0.55, 0.75, 1.0),
    "Face pull":              ("espalda", 0.15, 0.2,  0.35),

    # HOMBROS
    "Press militar barra":    ("hombros", 0.4,  0.6,  0.9),
    "Elevaciones laterales":  ("hombros", 0.05, 0.08, 0.12),
    "Elevaciones frontales":  ("hombros", 0.06, 0.1,  0.15),
    "Press Arnold":           ("hombros", 0.15, 0.25, 0.35),
    "Encogimientos trapecio": ("hombros", 0.6,  0.8,  1.3),

    # BICEPS
    "Curl barra":             ("biceps",  0.25, 0.4,  0.6),
    "Curl mancuernas":        ("biceps",  0.12, 0.2,  0.3),
    "Curl martillo":          ("biceps",  0.14, 0.22, 0.35),
    "Curl predicador":        ("biceps",  0.2,  0.3,  0.45),
    "Curl concentrado":       ("biceps",  0.1,  0.15, 0.25),

    # TRICEPS
    "Press cerrado":          ("triceps", 0.6,  0.8,  1.2),
    "Fondos triceps":         ("triceps", 0.8,  1.0,  1.5),
    "Extension polea":        ("triceps", 0.25, 0.35, 0.5),
    "Press frances":          ("triceps", 0.25, 0.4,  0.6),
    "Skullcrusher":           ("triceps", 0.25, 0.4,  0.6),

    # CORE
    "Crunch con peso":        ("core",    0.1,  0.2,  0.35),
    "Russian twist":          ("core",    0.1,  0.18, 0.3),
    "Sit up con peso":        ("core",    0.15, 0.3,  0.45),
    "Elevacion piernas":      ("core",    0.08, 0.15, 0.25),
    "Plancha con peso":       ("core",    0.15, 0.3,  0.5),
}