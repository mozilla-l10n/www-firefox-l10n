# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.


### These are strings used inside components that are part of the
### Content Management System. It means they can be combined to build new
### pages and don't correspond to any specific page.

# Step Cards: Cards used to give instructions. Each card gets a heading with "Step 01", "Step 02", etc.
# Variables:
#   $number (number) - the number of the step
block-step-card-step = Krok { $number }
# Download Firefox button
# Download Firefox button has optional "set as default" checkmark label
block-set-as-default = Nastavte si { -brand-name-firefox } jako svůj výchozí prohlížeč.
# Code block: a code sample, an AI prompt, or the text an AI model returned
# Button above the sample that copies it.
block-code-copy = Kopírovat
# Replaces block-code-copy for a moment after the sample has been copied.
block-code-copied = Zkopírováno
# Label above a sample that shows the exact text (the prompt) given to an AI model.
block-code-prompt = Výzva
# Label above a sample that shows the text an AI model returned.
block-code-output = Výstup
# Accessibility label for a sample with no programming language shown. Read by
# screen readers; not shown visually.
block-code = Kód
