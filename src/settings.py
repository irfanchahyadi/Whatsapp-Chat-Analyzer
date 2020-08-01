import os, dotenv

dotenv.load_dotenv()
DATABASE_URL = os.getenv('DATABASE_URL')
GA_TRACKING_ID = os.getenv('GA_TRACKING_ID')
APP_NAME = 'Whatsapp Chat Analyzer'
LOGO = '/assets/logo.png'
FONT_AWESOME = 'https://use.fontawesome.com/releases/v5.10.2/css/all.css'
SOURCE_CODE_URL = 'https://github.com/irfanchahyadi/Whatsapp-Chat-Analyzer'
COPYRIGHT = 'Copyright \U000000A9 2020 Irfan Chahyadi'
COPYRIGHT_URL = SOURCE_CODE_URL + '/blob/master/LICENSE'
DISCLAIMER_URL = SOURCE_CODE_URL + '/blob/master/DISCLAIMER.md'
SETTINGS_URL = SOURCE_CODE_URL + '/blob/master/src/settings.py'
CONTACT_EMAIL = 'mailto:irfanchahyadi@gmail.com'
CONTACT_GITHUB = 'https://github.com/irfanchahyadi'
CONTACT_LINKEDIN = 'https://www.linkedin.com/in/irfanchahyadi'
FROM_LANDING_PAGE = '?from=landing_page'
CHART_HEIGHT = 270
DAYS = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
HOURS = [f'0{i}:00'[-5:] for i in range(24)]
CONTENT = ['Contact', 'Deleted', 'Location', 'Media', 'Text']
CATEGORIES = ['Contact', 'Deleted', 'Event', 'Location', 'Media', 'Text']
RE_LINK = '(?:(?:(?:https|http|ftp):\/\/(?:www\.)?)|(?:www\.))((?:[\w\-_]+?\.)?(?:[\w\-_]+?\.)?[\w\-_]+?\.\w+)\S*'
LINK_LOCATION = ['facebook.com', 'maps.google.com', 'foursquare.com']


LANGUAGE = {
    'en': {
        'language': 'English',
        'date': '%m/%d/%y, %H:%M',
        'media': 'Media omitted',
        'you': 'You',
        'and': 'and',
        'location': 'live location shared',
        'location2': 'location',
        'contact': 'file attached',
        'deleted': 'This message was deleted',
        'deleted2': 'You deleted this message',
        'events_encripted': 'Messages to this group are now secured with end-to-end encryption.',
        'events_encripted2': 'Messages to this chat and calls are now secured with end-to-end encryption.',
        'event_changed_phone': 'changed their phone number to a new number.',
        'event_changed_phone2': 'changed to',
        'event_admin': "You're now an admin",
        'event_create': 'created group',
        'event_subject': 'changed the subject from',
        'event_icon': "changed this group's icon",
        'event_add': 'added',
        'event_add2': 'added',
        'event_left': 'left'},
    'in': {
        'language': 'Indonesian',
        'date': '%d/%m/%y %H.%M',
        'media': 'Media tidak disertakan',
        'you': 'Anda',
        'and': 'dan',
        'location': 'Lokasi terkini dibagikan',
        'location2': 'lokasi ',
        'contact': 'file terlampir',
        'deleted': 'Pesan ini telah dihapus',
        'deleted2': 'Anda telah menghapus pesan ini',
        'events_encripted': 'Pesan yang dikirim ke grup ini kini diamankan dengan enkripsi end-to-end.',
		'events_encripted2': 'Pesan yang dikirim ke grup ini kini diamankan dengan enkripsi end-to-end.',
        'event_changed_phone': 'telah mengganti nomor teleponnya ke nomor baru.',
        'event_changed_phone2': 'telah diganti ke',
        'event_admin': 'Anda sekarang adalah admin',
        'event_create': 'telah membuat grup',
        'event_subject': 'telah mengubah subjek dari',
        'event_icon': 'telah mengubah ikon grup ini',
        'event_add': 'telah menambahkan',
        'event_add2': 'menambahkan',
        'event_left': 'keluar'}}

PATTERN = {
    'emoji': '<(?:Emoji)(?:[^>]+)>',
    'link': RE_LINK,
    'mention': '@\d{10,}',
    'media': '<(?:{media})>',
    'location': '(?:{location}|(?:{location2}:\s' + RE_LINK + '))',
    'contact': '^.+\.(vcf \({contact}\))',
    'deleted': '({deleted}|{deleted2})',
    'events': [
        '.+\s({events_encripted})\s.+',
		'.+\s({events_encripted2})\s.+',
        '(.+)\s({event_changed_phone})\s.+',
        '(.+)\s({event_changed_phone2})\s(.+)',
        "^({event_admin})",
        '(.+)\s({event_create})\s"(.+)"',
        '(.+)\s({event_subject})\s".+"\s\w+\s"(.+)"',
        "(.+)\s({event_icon})",
        '(.+?)\s({event_add}|{event_add2})\s(.+)',
        '(.+)\s({event_left})']}

TOOLTIPS = {
    'save': 'Currently not avaliable due limited capacity on heroku postgre free plan',
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
    'favorite-domain': 'Most shared link domain',
    'mentioner': 'User who sent the most mention',
    'recruiter': 'User who invite the most new member to group',
    'inconstant': 'User who frequently send and delete message',
    'dominance': 'Comparison top 5 most active user over time',
    'breakdown-content': 'Top 5 most active user and amount each content they sent',
    'emoji-used': 'Top 10 most used emoji on text message',
    'word-cloud': 'Show most used word, reflect contexts of this chat',
    'recruitment-genealogy': 'Recruitment genealogy, A invite B to group, then B invite C and D, and so on'
}