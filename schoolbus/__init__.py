from publicsuffix import PublicSuffixList
from schoolbus.data import UNIVERSITY_DOMAINS

_psl = PublicSuffixList()

ACADEMIC_TLDS = {
    'ac.ae': True,
    'ac.at': True,
    'ac.bd': True,
    'ac.be': True,
    'ac.cr': True,
    'ac.cy': True,
    'ac.fj': True,
    'ac.id': True,
    'ac.il': True,
    'ac.ir': True,
    'ac.jp': True,
    'ac.ke': True,
    'ac.kr': True,
    'ac.ma': True,
    'ac.mu': True,
    'ac.mw': True,
    'ac.mz': True,
    'ac.nz': True,
    'ac.pa': True,
    'ac.pg': True,
    'ac.rs': True,
    'ac.ru': True,
    'ac.rw': True,
    'ac.th': True,
    'ac.tz': True,
    'ac.ug': True,
    'ac.uk': True,
    'ac.yu': True,
    'ac.za': True,
    'ac.zm': True,
    'ac.zw': True,
    'edu': True,
    'edu.af': True,
    'edu.al': True,
    'edu.ar': True,
    'edu.au': True,
    'edu.az': True,
    'edu.ba': True,
    'edu.bb': True,
    'edu.bd': True,
    'edu.bh': True,
    'edu.bi': True,
    'edu.bn': True,
    'edu.bo': True,
    'edu.br': True,
    'edu.bs': True,
    'edu.bt': True,
    'edu.bz': True,
    'edu.co': True,
    'edu.cu': True,
    'edu.do': True,
    'edu.dz': True,
    'edu.ec': True,
    'edu.ee': True,
    'edu.eg': True,
    'edu.er': True,
    'edu.es': True,
    'edu.et': True,
    'edu.ge': True,
    'edu.gh': True,
    'edu.gr': True,
    'edu.gt': True,
    'edu.hk': True,
    'edu.hn': True,
    'edu.ht': True,
    'edu.iq': True,
    'edu.jm': True,
    'edu.jo': True,
    'edu.kg': True,
    'edu.kh': True,
    'edu.kn': True,
    'edu.kw': True,
    'edu.ky': True,
    'edu.kz': True,
    'edu.la': True,
    'edu.lb': True,
    'edu.lv': True,
    'edu.ly': True,
    'edu.mk': True,
    'edu.mm': True,
    'edu.mn': True,
    'edu.mo': True,
    'edu.mt': True,
    'edu.mx': True,
    'edu.my': True,
    'edu.ni': True,
    'edu.np': True,
    'edu.om': True,
    'edu.pa': True,
    'edu.pe': True,
    'edu.ph': True,
    'edu.pk': True,
    'edu.pl': True,
    'edu.pr': True,
    'edu.ps': True,
    'edu.pt': True,
    'edu.py': True,
    'edu.qa': True,
    'edu.rs': True,
    'edu.ru': True,
    'edu.sa': True,
    'edu.sd': True,
    'edu.sg': True,
    'edu.sv': True,
    'edu.sy': True,
    'edu.tr': True,
    'edu.tt': True,
    'edu.tw': True,
    'edu.ua': True,
    'edu.uy': True,
    'edu.ve': True,
    'edu.vn': True,
    'edu.ws': True,
    'edu.ye': True,
    'edu.zm': True,
    'vic.edu.au': True,
}

BLACKLIST_TLDS = {
    'america.edu': True,
    'academia.edu': True,
    'si.edu': True,
    # TODO: this is incomplete.
}

__all__ = ('school_names', 'is_academic')

def school_names(email):
    """
    Returns list of schools that the email can correspond to. The list can
    contain multiple names if multiple schools share a single domain.

    The list is empty if the email is not an academic email or if we don't
    know about it.
    """
    if '@' not in email:
        raise ValueError('%s is not a valid email' % email)
    _, domain = email.split('@')
    root_domain = _psl.get_public_suffix(domain)
    if root_domain in BLACKLIST_TLDS:
        return []
    return UNIVERSITY_DOMAINS.get(root_domain, [])

def is_academic(email):
    """Guesses whether the email is academic or not."""
    if '@' not in email:
        return False
    return len(school_names(email)) > 0
