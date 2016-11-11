import io

from django.core.management.base import BaseCommand, CommandError

import boto3
import botocore.exceptions
from botocore.handlers import disable_signing
import exifread

from metapile.models import Photo

class Command (BaseCommand):
  help = 'Processes images in S3 bucket'

  def add_arguments(self, parser):
    parser.add_argument('bucket', nargs='+')

  def handle(self, *args, **options):
    s3 = boto3.resource('s3')
    s3.meta.client.meta.events.register('choose-signer.s3.*', disable_signing)
    
    for bname in options['bucket']:
      bucket = s3.Bucket(bname)
      for key in bucket.objects.all():
        photo, created = Photo.objects.get_or_create(path=key.key, bucket=bname)
        if created:
          print(key.key)
          try:
            file_obj = io.BytesIO(key.get()['Body'].read())
            
          except botocore.exceptions.ClientError:
            print('!!! File Read Error !!!')
            continue
            
          tags = exifread.process_file(file_obj, details=False)
          meta = {}
          for tag_name, tag_value in tags.items():
            meta[tag_name] = str(tag_value)
            
          photo.metadata = meta
          photo.save()
          
        else:
          print('Skipped:', key.key)
          