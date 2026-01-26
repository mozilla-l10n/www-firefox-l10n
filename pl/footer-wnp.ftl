# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.


## New WNP CMS footer - cms/includes/wnp-footer.html

# Variables:
# $mozilla_link_attrs (attrs) - link to https://www.mozilla.org/
# $mozilla_foundation_link_attrs (attrs) - link to https://foundation.mozilla.org/
footer-visit-mozilla = Odwiedź <a { $mozilla_foundation_link_attrs }>{ -brand-name-mozilla-foundation(case: "acc") }</a>, nadrzędną organizację non-profit <a { $mozilla_link_attrs }>{ -brand-name-mozilla-corporation }</a>.
footer-firefox-support = Pomoc dla { -brand-name-firefox(case: "gen") }
footer-privacy-notice = Zasady ochrony prywatności
footer-donate = Przekaż darowiznę { -brand-name-mozilla(case: "loc") }
footer-donate-v2 = Przekaż datek na rzecz { -brand-name-mozilla-foundation }
