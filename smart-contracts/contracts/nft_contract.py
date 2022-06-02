import smartpy as sp
from templates import fa2_lib as FA2


class SingleUseTickets(
    FA2.Admin,
    FA2.ChangeMetadata,
    FA2.WithdrawMutez,
    FA2.MintNft,
    FA2.Fa2Nft
):
    ...


sp.add_compilation_target(
    "single_use_tickets",
    SingleUseTickets(
        metadata=sp.utils.metadata_of_url("http://example.com")
    )
)
