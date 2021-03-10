from django.contrib import admin

from .models import (
	Company,
	Department,
	Task,
	Log,
)

models = [
	Company,
	Department,
	Task,
	Log,
]

for model in models:
	admin.site.register(model)
