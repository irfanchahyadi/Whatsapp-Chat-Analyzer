import os, dotenv

dotenv.load_dotenv()
DB_CREDENTIALS = {
    'user': os.getenv('DB_USERNAME'),
    'pass': os.getenv('DB_PASSWORD'),
    'host': os.getenv('DB_HOST'),
    'port': os.getenv('DB_PORT'),
    'db': os.getenv('DB_DATABASE')}

LOGO = '/assets/logo.png'
FONT_AWESOME = 'https://use.fontawesome.com/releases/v5.10.2/css/all.css'
FROM_LANDING_PAGE = '?from=landing_page'
CHART_HEIGHT = 250
DAYS = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
HOURS = [f'0{i}:00'[-5:] for i in range(24)]
CONTENT = ['Contact', 'Deleted', 'Location', 'Media', 'Text']
CATEGORIES = ['Contact', 'Deleted', 'Event', 'Location', 'Media', 'Text']

PATTERN = {
    'universal': {
        'emoji': '<(?:Emoji)(?:[^>]+)>',
        'link': '(?:(?:(?:https|http|ftp):\/\/(?:www\.)?)|(?:www\.))\S+\.\S+',
        'mention': '@\d+'},
    'en': {
        'language': 'English',
        'date': '%m/%d/%y, %H:%M',
        'media': '<(?:Media)(?:[^>]+)>',
        'location': '(?:live location shared|(?:location:\s{}))',
        'contact': '^.+\.(vcf \(file attached\))',
        'deleted': '(This message was deleted|You deleted this message)',
        'events': [
            '.+\s(Messages to this group are now secured with end-to-end encryption.)\s.+',
            "^(You're now an admin)",
            '(.+)\s(created group)\s"(.+)"',
            '(.+)\s(changed the subject)\s.+to\s"(.+)"',
            "(.+)\s(changed this group's icon)",
            '(.+)\s(added)\s(.+)',
            '(.+)\s(changed their phone number)\s.+',
            '(.+)\s(changed to)\s(.+)',
            '(.+)\s(left)']}}

TOOLTIPS = {
    'created': 'User who created this chat group',
    'messages': 'Count all sent message (including Media, Location, Link, Contact, and Deleted) and count deleted message'
}