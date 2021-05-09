"""This module contains the main driver of the service"""
import asyncio
from dotenv import load_dotenv

from git_analyzer import GitStatisticsAnalyzer

load_dotenv('.env')

def main():
    # TODO add rest_interface logic
    analyzer = GitStatisticsAnalyzer()
    asyncio.run(analyzer.analyze())


if __name__ == "__main__":
    main()
