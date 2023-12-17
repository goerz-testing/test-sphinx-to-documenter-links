from sphinx.domains import Domain, ObjType
from sphinx.roles import XRefRole


class JuliaDomain(Domain):
    """Julia language domain.

    This is a minimal domain sufficient for intersphinx / DocumenterInterLinks.
    """

    name = 'jl'
    label = 'Julia'
    object_types = {
        # name => (localized name, *roles)
        'macro': ObjType('macro', 'macro'),
        'func': ObjType('func', 'func'),
        'abstract': ObjType('abstract', 'abstract'),
        'type': ObjType('type', 'type'),
        'mod': ObjType('mod', 'mod'),
        'obj': ObjType('obj', 'obj'),
    }

    roles = {
        'macro': XRefRole(),
        'func': XRefRole(),
        'abstract': XRefRole(),
        'type': XRefRole(fix_parens=True),
        'mod': XRefRole(),
        'obj': XRefRole(),
    }


def setup(app):
    app.add_domain(JuliaDomain)
