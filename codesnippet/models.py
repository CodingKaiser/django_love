from django.db import models

# Create your models here.
class CodeSnippet(models.Model):
    content = models.CharField(max_length=2000, blank=False, null=False)
    title = models.CharField(max_length=256, blank=False, null=False)
    JAVA = 'JA'
    JAVASCRIPT = 'JS'
    PYTHON = 'PY'
    HTML = 'HT'
    POSSIBLE_LANGUAGES = (
        (JAVA, 'Java'),
        (JAVASCRIPT, 'Javascript'),
        (PYTHON, 'Python'),
        (HTML, 'HTML'),
    )
    languages = models.CharField(
        max_length=2,
        choices=POSSIBLE_LANGUAGES,
        default=PYTHON,
    )

    def __str__(self):
        return "%s: code snippet" % self.title
