from rest_framework import serializers
from mainapp.payment.paymentModel import invoice, payment

"""Invoice Serializer"""
class InvoiceSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        #We can create our custom creation methode here but we'll use functional view for this
        return invoice.objects.create(**validated_data)

    class Meta:
        model = invoice
        fields = ['invoice_id','title', 'description','creation_timestamp', 'amount','amount_paid', 'payment_method', 'status' , 'student' , 'category', 'session_year']
    
    # def to_representation(self, instance):
    #     response = super().to_representation(instance)
    #     response['student'] = StudentSerializer(instance.student).data
    #     response['session_year'] = SessionYearSerializer(instance.session_year).data
    #     return response


"""Payment Serializer"""
class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = payment
        fields = '__all__'
