from celery import shared_task
from .models import Loan
from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone


@shared_task
def send_loan_notification(loan_id):
    try:
        loan = Loan.objects.get(id=loan_id)
        member_email = loan.member.user.email
        book_title = loan.book.title
        send_mail(
            subject="Book Loaned Successfully",
            message=f'Hello {loan.member.user.username},\n\nYou have successfully loaned "{book_title}".\nPlease return it by the due date.',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[member_email],
            fail_silently=False,
        )
    except Loan.DoesNotExist:
        pass


@shared_task
def check_overdue_loans():
    overdue_loans_emails = Loan.objects.filter(
        is_returned=False, due_date__lt=timezone.now().date()
    ).values("member__user__email", "book__title")

    # Using iterator for better performance if size would be large
    for email in overdue_loans_emails.iterator(chunk_size=100):
        print(email)
        send_mail(
            subject=f"Please return book {email['book__title']}",
            message=f"Please return book {email['book__title']}",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[email["member__user__email"]],
        )
