SF_SM_ARN = 'SF_SM_ARN'
INPUT_BKT = 'INPUT_BKT'
OUTPUT_BKT = 'OUTPUT_BKT'
DETECT_TOPIC_ARN = 'DETECT_TOPIC_ARN'
TEXTRACT_PUBLISH_ROLE = 'TEXTRACT_PUBLISH_ROLE'
ANALYZE_TOPIC_ARN = 'ANALYZE_TOPIC_ARN'
OUT_DETECT_PREFIX = '_detectText'
OUT_ANALYZE_PREFIX = '_analyzeText'
OUT_TASK_TOKEN_PREFIX = '_tasks'
OUT_DUMP_PREFIX ='_dump'
OUT_ANSWERS_PREFIX='_answers'
COMPREHEND_EP_ARN = 'COMPREHEND_EP_ARN'

SUPPORTED_FILES = [".pdf", ".png", ".jpg", ".jpeg", ".tiff"]

Payslip_Queries = [
    {
        "Text": "Who is the Landlord",
        "Alias": "LANDLORD"
    },
    {
        "Text": "Where is the Landlord address",
        "Alias": "LANDLORD_ADDRESS"
    },
    {
        "Text": "Who is the tenant",
        "Alias": "TENANT"
    },
    {
        "Text": "Where is the Lease",
        "Alias": "LEASE_ADDRESS"
    },
    {
        "Text": "What is the Premises",
        "Alias": "PREMISES"
    },
    {
        "Text": "What is the TERM",
        "Alias": "TERM"
    },
    {
        "Text": "What is the Start Date",
        "Alias": "START_DATE"
    },
    {
        "Text": "What is the Expiration Date",
        "Alias": "EXPIRATION_DATE"
    },
    {
        "Text": "What is the base rent",
        "Alias": "BASE_RENT"
    },
    {
        "Text": "What is the rent abatement",
        "Alias": "RENT_ABATEMENT"
    },
    {
        "Text": "WhO to make payment to",
        "Alias": "PAYEE"
    }
]

Bank_Queries = [
    {
        "Text": "Who is the Landlord",
        "Alias": "LANDLORD"
    },
    {
        "Text": "Where is the Landlord address",
        "Alias": "LANDLORD_ADDRESS"
    },
    {
        "Text": "Who is the tenant",
        "Alias": "TENANT"
    },
    {
        "Text": "Where is the Lease",
        "Alias": "LEASE_ADDRESS"
    },
    {
        "Text": "What is the Premises",
        "Alias": "PREMISES"
    },
    {
        "Text": "What is the TERM",
        "Alias": "TERM"
    },
    {
        "Text": "What is the Start Date",
        "Alias": "START_DATE"
    },
    {
        "Text": "What is the Expiration Date",
        "Alias": "EXPIRATION_DATE"
    },
    {
        "Text": "What is the base rent",
        "Alias": "BASE_RENT"
    },
    {
        "Text": "What is the rent abatement",
        "Alias": "RENT_ABATEMENT"
    },
    {
        "Text": "WhO to make payment to",
        "Alias": "PAYEE"
    },
]

Application_Queries = [
    {
        "Text": "Who is the Landlord",
        "Alias": "LANDLORD"
    },
    {
        "Text": "Where is the Landlord address",
        "Alias": "LANDLORD_ADDRESS"
    },
    {
        "Text": "Who is the tenant",
        "Alias": "TENANT"
    },
    {
        "Text": "Where is the Lease",
        "Alias": "LEASE_ADDRESS"
    },
    {
        "Text": "What is the Premises",
        "Alias": "PREMISES"
    },
    {
        "Text": "What is the TERM",
        "Alias": "TERM"
    },
    {
        "Text": "What is the Start Date",
        "Alias": "START_DATE"
    },
    {
        "Text": "What is the Expiration Date",
        "Alias": "EXPIRATION_DATE"
    },
    {
        "Text": "What is the base rent",
        "Alias": "BASE_RENT"
    },
    {
        "Text": "What is the rent abatement",
        "Alias": "RENT_ABATEMENT"
    },
    {
        "Text": "WhO to make payment to",
        "Alias": "PAYEE"
    },
]
