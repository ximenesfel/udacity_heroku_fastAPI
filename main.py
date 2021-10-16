"""
ML Pipeline
"""
import argparse
import src.basic_cleaning
import src.train_test_model
import src.check_score
import logging


def execute(args):
    """
    Execute the pipeline
    """
    logging.basicConfig(level=logging.INFO)

    if args.step == "basic_cleaning":
        logging.info("Basic cleaning procedure started")
        src.basic_cleaning.execute_cleaning()

    if args.step == "train_model":
        logging.info("Train model procedure started")
        src.train_test_model.train_test_model()

    if args.step == "check_score":
        logging.info("Score check procedure started")
        src.check_score.check_score()

    if args.step == "all":
        logging.info("Basic cleaning procedure started")
        src.basic_cleaning.execute_cleaning()
        logging.info("Train model procedure started")
        src.train_test_model.train_test_model()
        logging.info("Score check procedure started")
        src.check_score.check_score()


if __name__ == "__main__":
    """
    Main program
    """
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--step",
        type=str,
        choices=["basic_cleaning",
                 "train_model",
                 "check_score",
                 "all"],
        default="all",
        help="Pipeline step"
    )

    main_args = parser.parse_args()

    execute(main_args)
