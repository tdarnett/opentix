import smartpy as sp

FA2 = sp.io.import_script_from_url("https://smartpy.io/templates/fa2_lib.py")


class SingleUseTickets(
    FA2.Admin,
    # FA2.ChangeMetadata,
    # FA2.WithdrawMutez,
    FA2.MintNft,
    FA2.Fa2Nft
):

    def __init__(self, administrator, **kwargs):
        FA2.Fa2Nft.__init__(self, **kwargs)
        FA2.Admin.__init__(self, administrator)


def make_metadata(symbol, name):
    """Helper function to build metadata JSON bytes values."""
    return sp.map(
        l={
            "name": sp.utils.bytes_of_string(name),
            "symbol": sp.utils.bytes_of_string(symbol),
        }
    )


admin = sp.test_account("Administrator")
alice = sp.test_account("Alice")
tok0_md = make_metadata(name="Cowboys SZN22", symbol="CBY22")


@sp.add_test(name="Mint Basic NFT")
def test_mint_nft():
    # We define a test scenario, called sc,
    # together with some outputs and checks

    scenario = sp.test_scenario()
    # We first define a contract and add it to the scenario

    ticket_contract = SingleUseTickets(
        metadata=sp.utils.metadata_of_url("ipfs://example"),
        token_metadata=[tok0_md],
        ledger={
            0: alice.address,
        },
        policy=None,
        administrator=admin.address
    )
    scenario += ticket_contract
    # Attempt to mint  a token from a non-admin account and get an error
    ticket_contract.mint([sp.record(metadata=tok0_md, to_=alice.address)]).run(
        sender=alice, valid=False, exception="FA2_NOT_ADMIN"
    )

    scenario.h3("Mint from non-admin account")
    # Mint of a new NFT token from a non-admin account
    ticket_contract.mint(
        [
            sp.record(metadata=tok0_md, to_=alice.address),
        ]
    ).run(sender=admin)
    # THEN alice's balance should increase
    # TODO add tests to check the metadata for said token
    scenario.verify(ticket_contract.get_balance(sp.record(owner=alice.address, token_id=0)) == 1)
