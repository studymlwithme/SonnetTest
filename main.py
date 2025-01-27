from clients.sonnet_client import SonnetClient
from clients.git_client import GitClient
from utils.utils import utils
import argparse
def main():
    parser = argparse.ArgumentParser(
                    prog='AutoPushPullClaude',
                    description='Simply using GH as a database to store the changes I make to code with claude')
    parser.add_argument('-f','--filename', required=True)           # positional argument
    parser.add_argument('-rd', '--repoDirectory', default=".")      # option that takes a value
    parser.add_argument('-m', '--message', required=True)  # on/off flag
    args = parser.parse_args()
    git_client = GitClient(args.repoDirectory)
    sonnet_client = SonnetClient()
    git_client.pull_newest_changes()
    curr_code = utils.read_file(args.filename) 
    message = f"{args.message}\n In your message back to me only send the code, nothing else" 
    message = f"{message} \nCode Below: \n {curr_code}"
    new_code = sonnet_client.send_message(message)
    utils.write(args.filename, new_code)
    git_client.commit_repo_changes(files_to_add=[args.filename])
    response = git_client.push_newest_changes
    print(response)

if __name__ == '__main__': 
    main()
