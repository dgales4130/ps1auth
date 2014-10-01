from django.contrib import admin
from django.forms import Textarea
from django.db import models
from .models import CRMPerson, PayPal, Cash, Note, EmailRecord

class PayPalInline(admin.StackedInline):
    model = PayPal

class CashInline(admin.StackedInline):
    model = Cash

class NoteInline(admin.StackedInline):
    model = Note
    extra = 1
    formfield_overrides = {
        models.TextField: {
            'widget': Textarea(attrs={'rows': 5})
        }
    }
    save_on_top = True

class EmailRecordAdminInline(admin.TabularInline):
    model = EmailRecord
    exclude = ['message', 'reply_to_email']
    readonly_fields = ['subject', 'from_email', 'to_email', 'created_at', 'sender', 'status', ]
    can_delete = False
    extra = 0
    max_num = 0

class CRMPersonAdmin(admin.ModelAdmin):
    inlines = [
        PayPalInline,
        CashInline,
        NoteInline,
        EmailRecordAdminInline,
    ]
    
admin.site.register(CRMPerson, CRMPersonAdmin)
