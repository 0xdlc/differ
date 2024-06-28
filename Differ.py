import subprocess
from discord_webhook import DiscordWebhook, DiscordEmbed
import argparse


def main():
    def discord(title, description):
        webhook = DiscordWebhook(
            url="https://discord.com/api/webhooks/1129162629626212493/X3xvVKsoosRpb4hOJlZxAcFF3DpuXfx4R8MyV_8HQrMjeu1O79Md5tVZ7dNXaJmMQ9mo",
            rate_limit_retry=True)
        embed = DiscordEmbed(
            title=title,
            description=description,
            color='65535')
        webhook.add_embed(embed)
        response = webhook.execute()
    
    print('''
          Be Aware: 
          [!] You should have already ran the command once
          [!] You should have the output file as the Last arguement of you bash script
          ''')
    parser = argparse.ArgumentParser()
    parser.add_argument('-b', required=True, default=False, metavar='Bash profile with arguemtns Eg.: "nice_httpx.sh readfile writefile"', type=str)
    #parser.add_argument('-differ', required=True, default=False, metavar='What file should be differentiated with the processed file Eg: dropbox.fuzz.tmp', type=str)
    args = parser.parse_args()
    difile = args.b.split(' ')[-1]
    commands = args.b.split(' ')
    commands[-1] = f"{commands[-1]}.tmp"
    subprocess.call(commands)
    subprocess.call(['sort','-u','-o',commands[-1],commands[-1]])
    subprocess.call(['sort','-u','-o',difile,difile])
    new = subprocess.check_output(["comm","-23",commands[-1],difile],text=True)
    if len(new) > 1:
        ChangeTitle = f"[+] Found a Different"
        description = f'Differ:{str(new)}'
        discord(title=ChangeTitle ,description=description)
        f = open(difile, "a+")
        f.write(new)
        f.close()
    subprocess.run(["rm",difile])

if __name__ == '__main__':
    main()            

