from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Scope, ArticleScope


class ArticleScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        main_form = [form.cleaned_data.get('is_main') for form in self.forms if
                     form.cleaned_data.get('is_main') == True]
        set_form = set([form.cleaned_data.get('tag').id for form in self.forms])


        if len(main_form) > 1:
            raise ValidationError('Вы можете выбрать только одну основную тему статьи')
        elif len(main_form) == 0:
            raise ValidationError('Выберите основную тему статьи')
        elif len(set_form)!= len(self.forms):
            raise ValidationError('Темы повторяются')


        return super().clean()


class ArticleScopeInline(admin.TabularInline):
    model = ArticleScope
    formset = ArticleScopeInlineFormset
    extra = 0


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'text', 'published_at']
    inlines = [ArticleScopeInline, ]


@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']