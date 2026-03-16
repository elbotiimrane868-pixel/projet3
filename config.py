# Configuration settings for model selection, parameters, and customization options

class Config:
    # Model settings
    MODEL_NAME = 'default_model'  # Name of the model
    MODEL_VERSION = '1.0'          # Version of the model

    # Training parameters
    LEARNING_RATE = 0.001          # Learning rate for the optimizer
    BATCH_SIZE = 32                 # Number of samples per gradient update
    EPOCHS = 50                     # Number of epochs to train the model

    # Data parameters
    TRAIN_DATA_PATH = 'data/train/'  # Path to the training data
    VALIDATION_DATA_PATH = 'data/valid/'  # Path to validation data
    TEST_DATA_PATH = 'data/test/'    # Path to test data

    # Customization options
    ENABLE_LOGGING = True            # Enable or disable logging
    LOG_LEVEL = 'INFO'               # Logging level (DEBUG, INFO, WARNING, ERROR)

    # Other custom options
    USE_CUDA = True                  # Enable CUDA support if available
    RANDOM_SEED = 42                 # Random seed for reproducibility

    @staticmethod
    def print_config():
        import pprint
        pprint.pprint(vars(Config))
