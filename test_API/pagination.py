from rest_framework.pagination import PageNumberPagination

class CustomPagination(PageNumberPagination):
    page_size = 2  # Número de elementos por página
    page_size_query_param = 'tamaño'
    max_page_size = 10
