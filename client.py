class Eip712TypedSignaturePhishingSanitizerClient:
    def sanitize_typed_signature(self, verifying_contract='0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48', spender_address='0x742d35Cc6634C0532925a3b844Bc454e4438f44e', token_amount_wei=1000000000000000000):
        is_unlimited = token_amount_wei > 10**30
        return {
            'permit_scan_id': 'eip_scn_9918',
            'verifying_contract': verifying_contract,
            'spender_address': spender_address,
            'is_phishing_risk': is_unlimited,
            'unlimited_allowance_requested': is_unlimited,
            'spender_contract_reputation': 'VERIFIED_DEX_ROUTER',
            'signature_safety_grade': 'SAFE_SCOPED_PERMIT',
            'sanitized_dossier_url': 'https://security.crypto.genpark.ai/permits/eip_scn_9918.json'
        }
