{
    'name': 'Snippest Website custom',
    'version': '1.0',
    'category': 'Accounting',
    'sequence': 1,
    'summary': '',
    'description': """
            Invoice Tax
    """,
     'author': '',
    'company': '',
    'maintainer': '',
    'website': "omar",
    'website': 'omarhassanhh7@gmail.com',
    'depends': ['base','account','website'],
    'data': [
        # 'report/account_move_reports.xml',
        'views/snippets/options.xml',
        'views/snippets/property_agents.xml',
        'views/snippets/snippets.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'snippest_website/static/src/scss/property_agent.scss',
            
        ]
    },
    'installable': True,
    'auto_install': False,
    'application': False,
}