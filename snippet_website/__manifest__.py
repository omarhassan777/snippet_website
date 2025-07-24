{
    'name': 'Snippet Website custom',
    'version': '1.0',
    'category': 'website',
    'sequence': 10,
    'summary': '',
    'description': """
            create snippet on website odoo 17
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
            'snippet_website/static/src/scss/property_agent.scss',
            
        ]
    },
    'installable': True,
    'auto_install': False,
    'application': False,
}