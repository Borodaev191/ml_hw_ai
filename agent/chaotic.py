import random

from agent.base import BaseAgent
from base.protocol import OfferRequest, DealRequest, RoundResult


class ChaoticAgent(BaseAgent):

    def get_my_name(self) -> str:
        return 'Chaotic'

    def offer_action(self, data: OfferRequest) -> int:
        return random.randint(0, data.total_amount)

    def deal_action(self, data: DealRequest) -> bool:
        return random.choice([True, False])

    def round_result_action(self, data: RoundResult):
        pass
