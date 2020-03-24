{
    # Theme information
    'name': "Grs Default Theme",
    'description': 'GRS THEME',
    'category': 'Theme/Services',
	'summary': 'Corporate, Business, Tech, Services',
	'sequence': 120,
    'version': '1.0',
    'depends': ['website'],

    # templates
    'data': [
        'views/layout.xml',
        'views/assets.xml',
        'views/grs-home.xml',
        # 'views/snippets.xml',
    ],

    # demo pages
    'demo': [
        'demo/pages.xml',
    ],

    # Your information
    'author': "GRS Electronics",
    'website': "http://grselectrodomesticos.com",
    'images': [
        'static/poster.png',
    ],
	'license': 'LGPL-3',
}
