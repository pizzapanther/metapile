from graphene import relay, ObjectType, Schema
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from metapile.models import Photo

class PhotoNode (DjangoObjectType):
  class Meta:
    model = Photo
    filter_fields = ['path', 'bucket']
    filter_order_by = ['path']
    interfaces = (relay.Node, )
    
class Query (ObjectType):
  photo = relay.Node.Field(PhotoNode)
  photos = DjangoFilterConnectionField(PhotoNode)
  
schema = Schema(query=Query)
