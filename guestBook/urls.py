from django.urls import path
from guestBook.views import *

urlpatterns = [
    # path('', hello_world, name = 'hello_world'),
    # path('introduction/', introduction, name = 'introduction'),
    # path('<int:id>', get_post_detail, name = '게시글 조회'),

    # path('', post_list, name = "post_list"),
    # path('<int:id>/',post_detail, name = 'post_detail'),
    # path('<int:post_id>/comment/', comment_list, name="comment_list"),
    # path('week/', post_made_week, name="post_made_week")

    # path('page/', codeReview, name='codeReview'),

    path('',guestBookList.as_view()),
    path('<int:id>/',guestBookDetail.as_view())
]