from django.contrib import admin

from movies.models import Director, Movie


class MovieInLine(admin.StackedInline):
    model = Movie
    extra = 1


class DirectorAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ('full_name', 'biography', 'birthdate')})
    ]
    inlines = [MovieInLine]


admin.site.register(Director, DirectorAdmin)
admin.site.register(Movie)
