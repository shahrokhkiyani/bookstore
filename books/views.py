from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

from .models import Book
from .forms import CommentForm


class BookListView(generic.ListView):
    model = Book
    paginate_by = 4
    template_name = "books/book_list.html"
    context_object_name = "books"


def book_detail_view(request, pk):
    # get book comments

    book = get_object_or_404(Book, pk=pk)
    book_comment = book.comments.all()

    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
    else:
        comment_form = CommentForm()

    return render(
        request,
        "books/book_detail.html",
        {"book": book, "comments": book_comment, "comment_form": comment_form},
    )


class BookCreateView(generic.CreateView):
    model = Book
    fields = [
        "title",
        "author",
        "content",
        "price",
        "cover",
    ]
    template_name = "books/book_create.html"


class BookUpdateView(generic.UpdateView):
    model = Book
    fields = ["title", "author", "content", "cover"]
    template_name = "books/book_update.html"


class BookDeleteView(generic.DeleteView):
    model = Book
    template_name = "books/book_delete.html"
    success_url = reverse_lazy("book_list")
