# The character that starts/ends the sequence
coding_char = "~"

# Max length limit. Once it is reached, the sequence is cleared
max_symbols = 10


# manually defined shortcuts
shortcuts = {
    # stop the listener
    "stop": "stop",
    # basic operations
    "not": "¬",
    "and": "∧",
    "or": "∨",
    "forall": "∀",
    "exists": "∃",
    "empty": "∅",
    "in": "∈",
    "notin": "∉",
    "sub": "⊂",
    "super": "⊃",
    "R": "ℝ",
    "Z": "ℤ",
    "N": "ℕ",
    "Q": "ℚ",
    "C": "ℂ",

    "!=": "≠",
    "+-": "±",
    "-+": "∓",
    "d": "∂",
    "sqrt": "√",
    "inf": "∞",
    "deg": "°",
    "int": "∫",
    "sum": "∑",
    "prod": "∏",
    "otimes": "⊗",
    "oplus": "⊕",
    # greek letters
    "alpha": "α",
    "beta": "β",
    "gamma": "γ",
    "delta": "δ",
    "pi": "π",
    "theta": "θ",
    "lambda": "λ",
    "mu": "μ",
    "sigma": "σ",
    "omega": "ω",
    "phi": "φ",
    "psi": "ψ",
    "zeta": "ζ",
    "xi": "ξ",
    "tau": "τ",
    # arrows
    "->": "→",
    "<-": "←",
    "<->": "↔",
    "=>": "⇒",
    "<=": "⇐",
    "!=>": "⇏",
    "=>!": "⇍",
    "<=>": "⇔",
    # don't know what else to add
    "sun": "☉",
    "moon": "☽",
    "star": "★",
    "hbar": "ℏ",
}


def write_power(key):
    output = ""
    converter = {
        "0": "⁰",
        "1": "¹",
        "2": "²",
        "3": "³",
        "4": "⁴",
        "5": "⁵",
        "6": "⁶",
        "7": "⁷",
        "8": "⁸",
        "9": "⁹",
        ".": "⋅",
        "T": "ᵀ",
        "+": "⁺",
        "-": "⁻",
    }

    for char in key:
        output += converter.get(char, "")
    return output
