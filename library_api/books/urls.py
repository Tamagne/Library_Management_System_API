from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AuthorViewSet, BookViewSet, MemberViewSet, BorrowTransactionViewSet, BorrowBookView, ReturnBookView, OverdueBooksView
from .views import AdminReportView, ExportReportView

router = DefaultRouter()
router.register('authors', AuthorViewSet, basename='author')
router.register('books', BookViewSet, basename='book')
router.register('members', MemberViewSet, basename='member')
router.register('transactions', BorrowTransactionViewSet, basename='transaction')

urlpatterns = [
    path('', include(router.urls)),
    path('borrow/', BorrowBookView.as_view(), name='borrow-book'),
    path('return/<int:pk>/', ReturnBookView.as_view(), name='return-book'),
    path('overdue-books/', OverdueBooksView.as_view(), name='overdue-books'),
    path('admin-report/', AdminReportView.as_view(), name='admin-report'),
    path('export-report/', ExportReportView.as_view(), name='export-report'),



]

