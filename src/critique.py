class CritiqueEngine:
    def __init__(self, model):
        self.model = model

    def generate_critique(self, text):
        # Placeholder: Lógica de detecção de ambiguidade
        if "ética" in text.lower():
            return "QUESTION: Como você define 'ética' neste contexto?"
        return "QUESTION: None (sem crítica identificada)"
