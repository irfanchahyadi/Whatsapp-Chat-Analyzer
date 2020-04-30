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
CHART_HEIGHT = 270
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
    'save': 'Save your chat history so you can revisit using url key',
    'created': 'User who created this chat group, and when it created',
    'messages': 'Number of all sent message (including text, media, location, link, contact, and deleted) and count deleted message',
    'words': 'Number of words used on text message',
    'emoji': 'Number of emoji used on text message',
    'mention': 'Number of mention used on text message',
    'media': 'Number of media shared, including image, video, document, gif, and audio',
    'location': 'Number of gps location shared and live location',
    'link': 'Number of link shared on text message',
    'contact': 'Number of contact shared with attach vcf file',
    'users': 'Number of active member (sent at least one message)',
    'time-series': 'Number of Activity (message & event) each interval (day/week/month/year) break down by category',
    'daily-activity': 'Number of Activity (message & event) for each weekday',
    'hourly-activity': 'Number of Activity (message & event) for each hour',
    'per-user': 'Average number of message sent each users',
    'per-text': 'Average number of word & emoji sent each text message',
    'per-day': 'Average number of text and media sent each day',
    'per-month': 'Average number of text and media sent each month',
    'busy-day': 'Most active date',
    'talk-active': 'User who sent the most messages',
    'silent-reader': 'User who sent the fewest messages',
    'long-typer': 'User who sent the most long text message',
    'emoji-fan': 'User who sent the most emoji on text message',
    'media-lover': 'User who sent the most media',
    'location-reporter': 'User who share the most location (gps and live share)',
    'link-sharer': 'User who share the most link on text message',
    'contact-sharer': 'User who share the most contact (vcf)',
    'mentioner': 'User who sent the most mention',
    'recruiter': 'User who invite the most new member to group',
    'inconstant': 'User who frequently send and delete message',
    'dominance': 'Comparison top 5 most active user over time',
    'breakdown-content': 'Top 5 most active user and amount each content they sent'
}