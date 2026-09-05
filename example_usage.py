from client import Eip712TypedSignaturePhishingSanitizerClient

def main():
    client = Eip712TypedSignaturePhishingSanitizerClient()
    res = client.sanitize_typed_signature()
    print('EIP-712 Signature Sanitizer: ' + res['permit_scan_id'] + ' (' + res['signature_safety_grade'] + ')')
    print('Phishing Risk: ' + str(res['is_phishing_risk']) + ' | Reputation: ' + res['spender_contract_reputation'])
    print('Dossier URL: ' + res['sanitized_dossier_url'])

if __name__ == '__main__':
    main()
