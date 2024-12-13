import azure.functions as func
from .github_balloon import main

def main(mytimer: func.TimerRequest) -> None:
    main()