from django.contrib import admin

from .models import SlackToken


class SlackTokenAdmin(admin.ModelAdmin):
    raw_id_fields = ('app', 'account',)
    list_display = ('app', 'account', 'truncated_scopes', 'truncated_token', 'expires_at')
    list_filter = ('app', 'app__provider', 'expires_at')

    def truncated_scopes(self, token):
        max_chars = 20
        ret = token.scopes
        if len(ret) > max_chars:
            ret = ret[0:max_chars] + '...(truncated)'
        return ret
    truncated_scopes.short_description = 'Scopes'

    def truncated_token(self, token):
        max_chars = 40
        ret = token.token
        if len(ret) > max_chars:
            ret = ret[0:max_chars] + '...(truncated)'
        return ret
    truncated_token.short_description = 'SlackToken'


admin.site.register(SlackToken, SlackTokenAdmin)
