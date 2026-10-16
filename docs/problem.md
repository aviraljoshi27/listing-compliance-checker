# The problem: risky claims in product listings

## Who this is for

The main user is a compliance analyst at an online marketplace. I did this
job at Amazon. Risky listings reached us in two ways. Another team flagged a
listing and sent it to us, or we took a long list of one brand's listings in
a category, checked a sample by hand, and gave the whole group the result of
that sample.

A seller checking a listing before publishing it is a second user. The same
check works for them, but I built this around the analyst.

## What hurts

It takes a lot of time. Each listing has many things to check, so an analyst
can only read so many in a day.

Sampling causes mistakes in both directions. When a sample's result is given
to a whole group of listings, most of those listings were never read. A
clean listing can end up marked as bad, and a risky one can end up marked as
fine.

The usual way to flag listings automatically is a keyword list: a list of
risky words like "cure", "arthritis" or "FDA approved". A program flags any
listing that contains one of those words. It checks for the words, not what
the sentence means, so it makes the same two mistakes as sampling.

It misses risky claims that use different words. "Say goodbye to joint pain
forever" promises to fix a health problem, but it contains none of the
words on the list, so it passes as fine.

It flags harmless listings that happen to use a listed word. "Cure time for
this glue is 24 hours" uses "cure" to mean the glue hardens, but the program
sees the word "cure" and flags it as bad.

## What success looks like

Every listing gets checked, not just a sample. The analyst only opens the
listings the tool flags, and each flag shows the exact claim, which rule it
breaks, and a short reason. It should flag fewer harmless listings than a
keyword list does, so the analyst isn't buried in false alarms.

If there's time after the core works and is measured, I want to add three
more things, in this order:

1. A summary of flagged listings grouped by brand and by category.
2. An alert when a brand's flagged listings pass a set limit, marking it
   as a risky brand.
3. When a listing's brand looks wrong, a guess at which brand it most
   likely belongs to. This one needs a list of real brands, which my data
   doesn't have, so it's the hardest.

## How I'll measure it

I'll label about 100 listings by hand, using my own compliance judgment, and
compare every system against my labels. The systems are a keyword list,
hosted models (Claude and GPT), and a small model running on my laptop.

For each one I'll record:

- how many of its flags were really risky (so the analyst isn't wasting time)
- how many of the risky listings it caught (so nothing slips through)
- whether it got the brand and product type right
- what it costs and how long it takes per listing

What would make my old compliance manager say yes: it catches risky claims
the keyword list misses, doesn't drown the team in false flags, costs less
than a minute of an analyst's time per listing, and gives a brand-wise and
category-wise summary of what it found.