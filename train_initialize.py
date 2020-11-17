from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from rasa.core import utils
from rasa.core.agent import Agent
from rasa.core.policies.memoization import MemoizationPolicy
from rasa.core.policies.sklearn_policy import SklearnPolicy

if __name__ == '__main__':
    #utils.io.configure_colored_logging(loglevel="DEBUG")

    training_data_file = './data/stories.md'
    model_path = './models/dialogue'

    agent = Agent("spotybot_domain.yml",
                  policies=[MemoizationPolicy(max_history = 2), SklearnPolicy()])

    training_data = agent.load_data(training_data_file)

    agent.train(
            training_data,
            augmentation_factor=50,
            epochs=500,
            batch_size=10,
            validation_split=0.2
    )

    agent.persist(model_path)