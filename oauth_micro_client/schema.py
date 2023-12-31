from marshmallow import Schema, fields, validate


class CreateAccountHolderSchema(Schema):
    first_name = fields.Str(required=True, allow_none=False,
                            validate=validate.Length(min=1))
    middle_name = fields.Str(required=True, allow_none=False)
    last_name = fields.Str(required=True, allow_none=False)
    gender = fields.Str(
        required=True, validate=validate.OneOf(["Male", "Female"]))
    kyc_type = fields.Str(required=True, validate=validate.OneOf(
        ["VOTER_ID", "PAN", "PASSPORT", "DRIVING_LICENCE"]))
    kyc_value = fields.Str(required=True, validate=validate.Length(min=5))
    phone_number = fields.Str(
        required=True, validate=validate.Length(equal=10))
    dob = fields.Date(required=True)


class CreateAccountSchema(Schema):
    account_holder_id = fields.Str(required=True)
    accounts = fields.List(fields.Str(
        required=True, validate=validate.Length(min=5)))


class CreateResourceSchema(Schema):
    account_holder_id = fields.Str(required=True)
    account_id = fields.Str(required=True, validate=validate.Length(equal=36))
    mobile_number = fields.Str(
        required=True, validate=validate.Length(equal=10))


class UpdateResourceStatusSchema(Schema):
    status = fields.Str(required=True, validate=validate.OneOf(
        ["ACTIVE", "INACTIVE", "DELETED"]))
    description = fields.Str()


class DeleteResourceStatusSchema(Schema):
    status = fields.Str(required=True, validate=validate.OneOf(
        ["DELETED"]))


class UpdateFormFactorStatusSchema(Schema):
    status = fields.Str(required=True, validate=validate.OneOf(
        ["ACTIVE", "INACTIVE", "DELETED"]))
    description = fields.Str()


class SuspendAccountSchema(Schema):
    status = fields.Str(required=True)


class AccountDebitSchema(Schema):
    debit_account_id = fields.Str(required=True)
    amount = fields.Integer(required=True)
    remarks = fields.Str(required=True)
    attributes = fields.Dict(keys=fields.String(), values=fields.String())


class AccountCreditSchema(Schema):
    credit_account_id = fields.Str(required=True)
    amount = fields.Integer(required=True)
    remarks = fields.Str(required=True)
    attributes = fields.Dict(keys=fields.String(), values=fields.String())


class AccountTransferSchema(Schema):
    debit_account_id = fields.Str(required=True)
    credit_account_id = fields.Str(required=True)
    amount = fields.Integer(required=True)
    remarks = fields.Str(required=True)
    attributes = fields.Dict(keys=fields.String(), values=fields.String())
