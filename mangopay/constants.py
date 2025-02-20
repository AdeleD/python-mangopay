from .utils import Choices


USER_TYPE_CHOICES = Choices(
    ('NATURAL_USER', 'natural', 'Natural user'),
    ('LEGAL_USER', 'legal', 'Legal user')
)

LEGAL_USER_TYPE_CHOICES = Choices(
    ('BUSINESS', 'business', 'Business'),
    ('ORGANIZATION', 'organization', 'Organization')
)

STATUS_CHOICES = Choices(
    ('CREATED', 'created', 'Created'),
    ('SUCCEEDED', 'succeeded', 'Succeeded'),
    ('FAILED', 'failed', 'Failed')
)

CARD_TYPE_CHOICES = Choices(
    ('CB_VISA_MASTERCARD', 'cb_visa_mastercard', 'CB VISA MASTERCARD'),
    ('MAESTRO', 'maestro', 'Maestro'),
    ('DINERS', 'diners', 'Diners')
)

PAYMENT_STATUS_CHOICES = Choices(
    ('WAITING', 'waiting', 'Waiting'),
    ('CANCELED', 'canceled', 'Canceled'),
    ('EXPIRED', 'expired', 'Expired'),
    ('VALIDATED', 'validated', 'Validated')
)

VALIDITY_CHOICES = Choices(
    ('UNKNOWN', 'unknown', 'Unknown'),
    ('VALID', 'valid', 'Valid'),
    ('INVALID', 'invalid', 'Invalid')
)

TRANSFER_TYPE_CHOICES = Choices(
    ('PAY_IN', 'payin', 'Pay In'),
    ('PAY_OUT', 'payout', 'Pay out'),
    ('TRANSFER', 'transfer', 'Transfer')
)

NATURE_CHOICES = Choices(
    ('REGULAR', 'regular', 'Regular'),
    ('REFUND', 'refund', 'Refund'),
    ('REPUDIATION', 'repudiation', 'Repudiation')
)

EXECUTION_TYPE_CHOICES = Choices(
    ('WEB', 'web', 'Web'),
    ('DIRECT', 'direct', 'Direct')
)

SECURE_MODE_CHOICES = Choices(
    ('DEFAULT', 'default', 'Default'),
    ('FORCE', 'force', 'Force')
)

BANK_ACCOUNT_TYPE_CHOICES = Choices(
    ('IBAN', 'iban', 'Iban'),
    ('GB', 'gb', 'GB'),
    ('US', 'us', 'US'),
    ('CA', 'ca', 'CA'),
    ('OTHER', 'other', 'Other')
)

DEPOSIT_CHOICES = Choices(
    ('CHECKING', 'checking', 'Checking'),
    ('SAVINGS', 'savings', 'Savings'),
)

DOCUMENTS_TYPE_CHOICES = Choices(
    ('IDENTITY_PROOF', 'identity_proof', 'Identity proof'),
    ('REGISTRATION_PROOF', 'registration_proof', 'Registration proof'),
    ('ARTICLES_OF_ASSOCIATION', 'articles_of_association', 'Articles of association'),
    ('SHAREHOLDER_DECLARATION', 'shareholder_declaration', 'Shareholder Declaration'),
    ('ADDRESS_PROOF', 'address_proof', 'Address Proof')
)

DOCUMENTS_STATUS_CHOICES = Choices(
    ('CREATED', 'created', 'Created'),
    ('VALIDATION_ASKED', 'validation_asked', 'Validation asked'),
    ('VALIDATED', 'validated', 'Validated'),
    ('REFUSED', 'refused', 'Refused')
)

EVENT_TYPE_CHOICES = Choices(
    ('KYC_CREATED', 'kyc_created', 'KYC Created'),
    ('KYC_SUCCEEDED', 'kyc_succeeded', 'KYC succeeded'),
    ('KYC_FAILED', 'kyc_failed', 'KYC failed'),
    ('KYC_VALIDATION_ASKED', 'kyc_validation_asked', 'KYC Validation asked'),
    ('PAYIN_NORMAL_CREATED', 'payin_normal_created', 'Payin normal created'),
    ('PAYIN_NORMAL_SUCCEEDED', 'payin_normal_succeeded', 'Payin normal succeeded'),
    ('PAYIN_NORMAL_FAILED', 'payin_normal_failed', 'Payin normal failed'),
    ('PAYOUT_NORMAL_CREATED', 'payout_normal_created', 'Payout normal created'),
    ('PAYOUT_NORMAL_SUCCEEDED', 'payout_normal_succeeded', 'Payout normal succeeded'),
    ('PAYOUT_NORMAL_FAILED', 'payout_normal_failed', 'Payout normal failed'),
    ('TRANSFER_NORMAL_CREATED', 'transfer_normal_created', 'Transfer normal created'),
    ('TRANSFER_NORMAL_SUCCEEDED', 'transfer_normal_succeeded', 'Transfer normal succeeded'),
    ('TRANSFER_NORMAL_FAILED', 'transfer_normal_failed', 'Transfer normal failed'),
    ('PAYIN_REFUND_CREATED', 'payin_refund_created', 'Payin refund created'),
    ('PAYIN_REFUND_SUCCEEDED', 'payin_refund_succeeded', 'Payin refund succeeded'),
    ('PAYIN_REFUND_FAILED', 'payin_refund_failed', 'Payin refund failed'),
    ('PAYOUT_REFUND_CREATED', 'payout_refund_created', 'Payout refund created'),
    ('PAYOUT_REFUND_SUCCEEDED', 'payout_refund_succeeded', 'Payout refund succeeded'),
    ('PAYOUT_REFUND_FAILED', 'payout_refund_failed', 'Payout refund failed'),
    ('TRANSFER_REFUND_CREATED', 'transfer_refund_created', 'Transfer refund created'),
    ('TRANSFER_REFUND_SUCCEEDED', 'transfer_refund_succeeded', 'Transfer refund succeeded'),
    ('TRANSFER_REFUND_FAILED', 'transfer_refund_failed', 'Transfer refund failed')
)

NOTIFICATION_STATUS_CHOICES = Choices(
    ('ENABLED', 'enabled', 'Enabled'),
    ('DISABLED', 'disabled', 'Disabled')
)

NOTIFICATION_VALIDITY_CHOICES = Choices(
    ('VALID', 'valid', 'Valid'),
    ('INVALID', 'invalid', 'Invalid')
)

DIRECT_DEBIT_TYPE_CHOICES = Choices(
    ('SOFORT', 'sofort', 'Sofort'),
    ('ELV', 'elv', 'ELV'),
    ('GIROPAY', 'giropay', 'Giropay')
)
