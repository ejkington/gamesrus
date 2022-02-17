from django.http import HttpResponse

class StripeWH_Handler:
    """handles stripe webhooks """
    
    def __init__(self, request):
        self.request = request
        
    def handle_event(self, event):
        """handle a generic/unexpected webhook event"""
        
        return HttpResponse(
            content=f'unhandled webhook recived: {event["type"]}',
            status=200)
        
    def handle_payment_intent_succeeded(self, event):
        """handle payment_intent.succeeded webhok from sprite """
        
        return HttpResponse(
            content=f'Webhook recived: {event["type"]}',
            status=200)
        
    def handle_payment_intent_payment_failed(self, event):
        """handle the payment_intent.payment_failed webhook from sprite"""
        
        return HttpResponse(
            content=f'Webhook recived: {event["type"]}',
            status=200)