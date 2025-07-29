from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from drf_spectacular.utils import extend_schema, extend_schema_view
from .models import Item
from .serializers import ItemSerializer, ItemCreateSerializer, ItemUpdateSerializer

@extend_schema_view(
    list=extend_schema(
        summary="List all items",
        description="Retrieve a paginated list of all items with optional filtering and search"
    ),
    create=extend_schema(
        summary="Create a new item",
        description="Create a new item with the provided data"
    ),
    retrieve=extend_schema(
        summary="Retrieve an item",
        description="Get details of a specific item by ID"
    ),
    update=extend_schema(
        summary="Update an item",
        description="Update all fields of an existing item"
    ),
    partial_update=extend_schema(
        summary="Partially update an item",
        description="Update specific fields of an existing item"
    ),
    destroy=extend_schema(
        summary="Delete an item",
        description="Delete an existing item by ID"
    ),
)
class ItemViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing items with full CRUD operations.
    
    Provides:
    - GET /items/ - List all items (with pagination, filtering, search)
    - POST /items/ - Create a new item
    - GET /items/{id}/ - Retrieve a specific item
    - PUT /items/{id}/ - Update an item (full update)
    - PATCH /items/{id}/ - Partially update an item
    - DELETE /items/{id}/ - Delete an item
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['name', 'description']
    ordering_fields = ['name', 'price', 'created_at', 'updated_at']
    ordering = ['-created_at']

    def get_serializer_class(self):
        if self.action == 'create':
            return ItemCreateSerializer
        elif self.action in ['update', 'partial_update']:
            return ItemUpdateSerializer
        return ItemSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, 
            status=status.HTTP_201_CREATED, 
            headers=headers
        )

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return_serializer = ItemSerializer(instance)
        return Response(return_serializer.data)

    def partial_update(self, request, *args, **kwargs):
        """Partially update an item (PATCH)"""
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

    # @extend_schema(
    #     summary="Get item statistics",
    #     description="Get statistics about items including count, average price, etc."
    # )
    # @action(detail=False, methods=['get'])
    # def stats(self, request):
    #     """Get item statistics"""
    #     from django.db.models import Count, Avg, Max, Min
        
    #     stats = Item.objects.aggregate(
    #         total_items=Count('id'),
    #         average_price=Avg('price'),
    #         max_price=Max('price'),
    #         min_price=Min('price')
    #     )
        
    #     if stats['average_price']:
    #         stats['average_price'] = float(stats['average_price'])
    #     if stats['max_price']:
    #         stats['max_price'] = float(stats['max_price'])
    #     if stats['min_price']:
    #         stats['min_price'] = float(stats['min_price'])
            
    #     return Response(stats)