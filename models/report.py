class Report:
    def __init__(self, report_type, content, generated_at):
        self.report_type = report_type
        self.content = content
        self.generated_at = generated_at

    def to_dict(self):
        return {
            "report_type": self.report_type,
            "content": self.content,
            "generated_at": self.generated_at
        }

