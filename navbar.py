"""Creates a sample navigation bar with ReactPy and Bootstrap 5.

Builds components with ReactPy and styled by Bootstrap. ReactPy-Router
is used to generate routes for the navbar buttons. The navbar design
is responsive to both desktop and mobile screens.
"""


from reactpy import component, html
from reactpy.backend.fastapi import configure, Options
from reactpy_router import route, simple
from fastapi import FastAPI


BOOTSTRAP_CSS = html.link(
    {
        'rel': 'stylesheet',
        'href': 'https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/'
                'dist/css/bootstrap.min.css',
        'integrity': 'sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80'
                     'zW1RWuH61DGLwZJEdK2Kadq2F9CUG65',
        'crossorigin': 'anonymous'
    }
)

BOOTSTRAP_SCRIPT = html.script(
    {
        'src': 'https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/'
               'dist/js/bootstrap.bundle.min.js',
        'integrity': 'sha384-kenU1KFdBIe4zVF0s0G1M5b4hcpxyD9'
                     'F7jL+jjXkk+Q2h455rYXK/7HAuoJl+0I4',
        'crossorigin': 'anonymous'
    }
)

HEADER_TITLE = 'ReactPy-Navbar'


@component
def NavItem(label: str, path: str, is_active: bool = False):
    attribute = {'href': path}
    if is_active:
        attribute.update(
            {'class': 'nav-link active', 'aria-current': 'page'},
        ),
    else:
        attribute.update(
            {'class': 'nav-link'},
        ),

    return html.div(
        html.li(
            {'class': 'nav-item'},
            html.a(attribute, label),
        ),
    )


@component
def NavBar(nav_attr: dict):
    return html.nav(
        {'class': 'navbar navbar-dark navbar-expand-lg bg-dark'},
        html.div(
            {'class': 'container-fluid'},
            html.a({'class': 'navbar-brand text-primary', 'href': '#'},
                   'ReactPy-Navbar'),
            html.button(
                {
                    'class': 'navbar-toggler',
                    'type': 'button',
                    'data-bs-toggle': 'collapse',
                    'data-bs-target': '#navbarSupportedContent',
                    'aria-controls': 'navbarSupportedContent',
                    'aria-expanded': 'false',
                    'aria-label': 'Toggle navigation',
                },
                html.span({'class': 'navbar-toggler-icon'}),
            ),
            html.div(
                {'class': 'collapse navbar-collapse',
                 'id': 'navbarSupportedContent'},
                html.ul(
                    {'class': 'navbar-nav me-auto mb-2 mb-lg-0'},
                    NavItem('Home', '/', nav_attr.get('Home', False)),
                    NavItem('Blog', '/blog', nav_attr.get('Blog', False)),
                ),
            ),
        ),
    )


@component
def Home():
    return html.div(
        BOOTSTRAP_CSS,
        BOOTSTRAP_SCRIPT,
        html.div(
            {'class': 'container mt-3'},
            NavBar({'Home': True}),

            # Home content starts here.
            ######################################################
            html.div(
                html.h5({'class': 'my-3'}, 'Home'),
                html.h2('The Food supply'),
                html.p(
                    '''Lorem ipsum dolor sit amet, consectetur
                       adipiscing elit. Suspendisse volutpat nisi
                       quis ligula lobortis, eget venenatis elit.
                       Integer vel nunc at felis tristique faucibus.
                       Nullam id est quis sapien aliquet tincidunt.'''
                ),
                html.p(
                    '''In euismod massa a aliquet posuere. Ut tristique
                       libero euismod ex feugiat consectetur. Maecenas
                       ultricies, justo sit amet rhoncus sagittis, nisi
                       eros venenatis nulla, ut vestibulum odio turpis
                       nec dolor. Vivamus lobortis.'''
                ),
            ),
        ),
    )


@component
def Blog():
    return html.div(
        BOOTSTRAP_CSS,
        BOOTSTRAP_SCRIPT,
        html.div(
            {'class': 'container mt-3'},
            NavBar({'Blog': True}),

            # Blog content starts here.
            ######################################################
            html.div(
                html.h5({'class': 'my-3'}, 'Blog'),
                html.h2('The good news in year 2025'),
                html.p(
                    '''Lorem ipsum dolor sit amet, consectetur adipiscing
                       elit. Fusce a nisi vitae urna posuere iaculis.
                       Suspendisse eget lorem a velit ultricies sodales.'''
                ),
                html.p(
                    '''Sed venenatis magna eget ipsum fringilla, nec
                       dignissim nisi interdum. Duis ut dapibus orci.
                       In lobortis elit sit amet semper.'''
                ),
            ),
        ),
    )


@component
def MissingLink():
    return html.div(
        BOOTSTRAP_CSS,
        html.div(
            {'class': 'container mt-3'},
            html.h1(html.h1("Missing Link 🔗‍💥"))
        ),
    )


@component
def root():
    return simple.router(
        route('/', Home()),
        route('/blog', Blog()),
        route('*', MissingLink()),
    )


app = FastAPI()
configure(app, root, options=Options(head=html.head(html.title(HEADER_TITLE))))
