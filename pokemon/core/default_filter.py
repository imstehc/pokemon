from django.contrib import admin
from django.contrib.admin import ChoicesFieldListFilter, FieldListFilter
from django.contrib.admin.views.main import ChangeList
from django.utils.translation import gettext_lazy as _


class DefaultFilterChangeList(ChangeList):
    def __init__(self, request, model, list_display, list_display_links,
                 list_filter, date_hierarchy, search_fields, list_select_related,
                 list_per_page, list_max_show_all, list_editable, model_admin, sortable_by):
        self.filter_params_defaults = model_admin.get_list_filter_defaults(request) or {}
        self.filter_params_sentinel = model_admin.get_list_filter_sentinel(request)
        super().__init__(request, model, list_display, list_display_links,
                         list_filter, date_hierarchy, search_fields, list_select_related,
                         list_per_page, list_max_show_all, list_editable, model_admin, sortable_by)

    def get_filters_params(self, params=None):
        lookup_params = super().get_filters_params(params)

        for param, default in self.filter_params_defaults.items():
            if param not in lookup_params:
                lookup_params[param] = default

        lookup_params = dict(
            (param, value) for param, value in lookup_params.items() if value != self.filter_params_sentinel
        )

        return lookup_params


class DefaultFilterMixin(admin.ModelAdmin):
    list_filter_defaults = {}
    list_filter_sentinel = '_off_'

    def get_list_filter_defaults(self, request):
        return self.list_filter_defaults

    def get_list_filter_sentinel(self, request):
        return self.list_filter_sentinel

    def get_changelist(self, request, **kwargs):
        return DefaultFilterChangeList


class DefaultChoicesFieldListFilter(ChoicesFieldListFilter):
    def __init__(self, field, request, params, model, model_admin, field_path):
        self.sentinel = model_admin.get_list_filter_sentinel(request) \
            if hasattr(model_admin, 'get_list_filter_sentinel') else None
        super().__init__(field, request, params, model, model_admin, field_path)

    def choices(self, changelist):
        yield {
            'selected': self.lookup_val is None or self.lookup_val == self.sentinel,
            'query_string': changelist.get_query_string({
                self.lookup_kwarg: self.sentinel,
            }, [self.lookup_kwarg_isnull]),
            'display': _('All')
        }
        none_title = ''
        for lookup, title in self.field.flatchoices:
            if lookup is None:
                none_title = title
                continue
            yield {
                'selected': str(lookup) == str(self.lookup_val),
                'query_string': changelist.get_query_string({self.lookup_kwarg: lookup}, [self.lookup_kwarg_isnull]),
                'display': title,
            }
        if none_title:
            yield {
                'selected': bool(self.lookup_val_isnull),
                'query_string': changelist.get_query_string({self.lookup_kwarg_isnull: 'True'}, [self.lookup_kwarg]),
                'display': none_title,
            }


FieldListFilter.register(lambda f: bool(f.choices), DefaultChoicesFieldListFilter, take_priority=True)
