from django.shortcuts import render
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import ShopifyOrder
from datetime import datetime
from django.shortcuts import render, get_object_or_404



# Create your views here.

def order_list(request):
    orders = ShopifyOrder.objects.all().order_by('-order_date')
    return render(request, 'orders/order_list.html', {
        'orders': orders
    })

def order_detail(request, order_id):
    order = get_object_or_404(ShopifyOrder, order_id=order_id)
    return render(request, 'orders/order_detail.html', {
        'order': order
    })

@csrf_exempt
def shopify_order_webhook(request):
    try:
        payload = json.loads(request.body)
        
        # Parse Shopify date string
        raw_date = payload.get('created_at', '')  # example field name from Shopify JSON
        order_date = None
        if raw_date:
            order_date = datetime.fromisoformat(raw_date.replace('Z', '+00:00')).date()
        
        ShopifyOrder.objects.update_or_create(
            order_id=payload.get("id"),
            defaults={
                'customer_name': payload.get("customer", {}).get("first_name", "") if payload.get("customer") else "",
                'total_price': payload.get("total_price", "0"),
                'currency': payload.get("currency", ""),
                'order_date': order_date,
            }
        )
        print("✅ Order saved")
        return JsonResponse({"status": "success"})
    except Exception as e:
        print(f"❌ Webhook error: {e}")
        return JsonResponse({"error": str(e)}, status=500)


