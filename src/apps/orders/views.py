from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Order, OrderItem
from .serializers import OrderSerializer
from apps.products.models import Cart, CartItem, Product

class OrderView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None):
        orders = Order.objects.filter(user=request.user)
        serializer = OrderSerializer(orders, many=True)
        if pk:
            order = orders.filter(id=pk).first()
            serializer = OrderSerializer(order)
        return Response(serializer.data)

    def post(self, request):
        # Fetch the user's cart
        cart = Cart.objects.get(user=request.user)
        cart_items = cart.items.all()

        if not cart_items:
            return Response({"error": "Cart is empty"}, status=status.HTTP_400_BAD_REQUEST)

        # Create an order
        order = Order.objects.create(user=request.user, status='PENDING')

        total_price = 0
        for item in cart_items:
            # Create an order item
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.price * item.quantity
            )
            total_price += item.product.price * item.quantity

            # Decrease product stock
            item.product.stock -= item.quantity
            item.product.save()

        # Set total price and save order
        order.total_price = total_price
        order.save()

        # Clear the user's cart
        cart_items.delete()

        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


    def delete(self, request, pk=None):
        order = Order.objects.get(pk=pk)
        order.delete()
        return Response({"message": "Order deleted"}, status=status.HTTP_204_NO_CONTENT)
    
    def patch(self, request, pk=None):
        order = Order.objects.get(pk=pk)
        serializer = OrderSerializer(order, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                        