# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------


def cli_billing_list_invoices(client, generate_url=False):
    """List all available invoices of the subscription"""
    invoices = client.list(expand='downloadUrl' if generate_url else None)
    return list(invoices)


def cli_billing_get_invoice(client, name=None):
    """Retrieve invoice of specific name of the subscription"""
    if name:
        return client.get(name)
    return client.get_latest()


def cli_billing_list_periods(client):
    """List all available billing periods of the subscription"""
    return list(client.list())


def cli_billing_list_enrollment_accounts(client):
    """List all available enrollment accounts"""
    return list(client.list())
