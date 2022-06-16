import smartpy as sp

FA2 = sp.io.import_script_from_url("https://smartpy.io/templates/fa2_lib.py")


class NFT(
    FA2.Admin,
    # FA2.ChangeMetadata,
    FA2.OffchainviewTokenMetadata,
    FA2.MintNft,
    FA2.Fa2Nft
):

    def __init__(self, administrator, **kwargs):
        FA2.Fa2Nft.__init__(self, **kwargs)
        FA2.Admin.__init__(self, administrator)

    @sp.offchain_view()
    def is_claimed(self, token_id):
        """Return the claimed state of a given token"""
        sp.trace(sp.unpack(self.data.token_metadata[token_id].token_info['claimed'], sp.TString))
        sp.result(self.data.token_metadata[token_id].token_info['claimed'])

