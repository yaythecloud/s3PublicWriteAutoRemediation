import boto3
import datetime
import json

def storage_compliance():
    c = boto3.client('config')
    b = boto3.client('s3')
    r = boto3.resource('s3')
    
    print ('Fixing non compliant resource %s' % datetime.datetime.now())
    
    bCompliance = c.describe_compliance_by_resource(
       ResourceType = 'AWS::S3::Bucket',
       ComplianceTypes = ['NON_COMPLIANT']
     )
    print (bCompliance)
    
    sBucket = bCompliance['ComplianceByResources']
    
    for sb in sBucket:
        print ("---Bucket with Public write permissions---")
        print (sb)
        print ("---Bucket Name---")
        print (sb['ResourceId'])
        bn = sb['ResourceId']
        sb = b.put_bucket_acl(
            ACL = 'private',
            Bucket = bn
        )
    print ('---Bucket was fixed successfully---')
        

def lambda_handler(event, context):
    
    storage_compliance()
   
    