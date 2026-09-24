from django.contrib import admin

from .models import Listing, LikedListing, ListingInquiry, ListingInquiryAttempt
class ListingAdmin(admin.ModelAdmin):
    readonly_fields = ('id', )


class LikedListingAdmin(admin.ModelAdmin):
    readonly_fields = ('id', )


class ListingInquiryAdmin(admin.ModelAdmin):
    list_display = (
        'profile',
        'listing',
        'created_at',
        'attempt_count',
    )
    search_fields = (
        'profile__user__username',
        'listing__model',
    )
    readonly_fields = (
        'created_at',
        'attempt_count',
    )
    def attempt_count(self, obj):
        return obj.attempts.count()
    attempt_count.short_description = 'Emails Sent'


class ListingInquiryAttemptAdmin(admin.ModelAdmin):
    list_display = (
        'inquiry',
        'sent_at',
    )
    search_fields = (
        'inquiry__profile__user__username',
        'inquiry__listing__model',
    )
    readonly_fields = (
        'sent_at',
    )


admin.site.register(Listing, ListingAdmin)
admin.site.register(LikedListing, LikedListingAdmin)
admin.site.register(
    ListingInquiry,
    ListingInquiryAdmin
)
admin.site.register(
    ListingInquiryAttempt,
    ListingInquiryAttemptAdmin
)

