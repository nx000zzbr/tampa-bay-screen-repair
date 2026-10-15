#!/usr/bin/env python3
"""Generates the inner pages (services, areas, screen-guide) from one header and one footer.
index.html is written by hand and is not touched. Run: python3 build.py"""
from pathlib import Path

ROOT = Path(__file__).parent
STRIPE = lambda n: '<span class="stripe" aria-hidden="true">' + '<i></i>' * n + '</span>'
STRIPE_DIV = lambda n: '<div class="stripe thin" aria-hidden="true">' + '<i></i>' * n + '</div>'
SMS = 'sms:+18135165619?&body=Hi%20Jerry%2C%20I%20need%20a%20screen%20quote.%20Photos%20attached.'

def head(title, description, path):
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} · Tampa Bay Screen Repair</title>
<meta name="description" content="{description}">
<meta name="theme-color" content="#1f1e1b">
<meta property="og:title" content="{title} · Tampa Bay Screen Repair">
<meta property="og:description" content="{description}">
<meta property="og:type" content="website">
<script>document.documentElement.classList.add('js')</script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:ital,wght@0,700;0,800&family=Public+Sans:ital,wght@0,400;0,500;0,600;0,700;1,400&display=swap" rel="stylesheet">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' fill='%23f0f0eb'/%3E%3Crect x='8' y='8' width='48' height='48' fill='%23ff6a1a'/%3E%3Cpath d='M8 20h48M8 32h48M8 44h48M20 8v48M32 8v48M44 8v48' stroke='%231b1b1a' stroke-width='3'/%3E%3C/svg%3E">
<link rel="stylesheet" href="styles.css">
</head>
<body>
<a class="sr-only" href="#main">Skip to content</a>

<header class="nav">
  <a class="wordmark" href="index.html" aria-label="Tampa Bay Screen Repair, home">Tampa Bay <b>Screen Repair</b></a>
  <nav class="links" aria-label="Main">
    <a href="services.html"{' aria-current="page"' if path == 'services' else ''}>Services</a>
    <a href="index.html#how">How it works</a>
    <a href="screen-guide.html"{' aria-current="page"' if path == 'guide' else ''}>Screen guide</a>
    <a href="areas.html"{' aria-current="page"' if path == 'areas' else ''}>Areas</a>
  </nav>
  <a class="button" href="index.html#quote">Get a quote{STRIPE(14)}</a>
  <button class="menu-btn" aria-expanded="false" aria-controls="sheet-menu">Menu</button>
</header>
<div class="sheet-menu" id="sheet-menu">
  <a href="services.html">Services</a>
  <a href="index.html#how">How it works</a>
  <a href="screen-guide.html">Screen guide</a>
  <a href="areas.html">Areas</a>
  <a href="index.html#quote">Get a quote</a>
  <a href="tel:+18135165619">Call (813) 516-5619</a>
</div>

<main id="main">
'''

FOOT = f'''
</main>

<footer class="back">
  {STRIPE_DIV(160)}
  <div class="panel" data-reveal>
    <div class="signoff">
      <h2>Call Jerry.</h2>
      <p>Or text a photo of the damage and go back to your evening. You will have a written price before you go to bed, and it is the price you will pay.</p>
    </div>
    <div class="address">
      <a href="tel:+18135165619">(813) 516-5619</a>
      <a href="mailto:TampaBayScreenRepair@gmail.com">TampaBayScreenRepair@gmail.com</a>
      <a href="areas.html">Plant City, FL 33565</a>
      <a href="https://www.facebook.com/p/TAMPA-BAY-Screen-Repair-100049211145599/" rel="noopener">Facebook</a>
    </div>
    <figure class="stamp"><img src="assets/plant-city-fl-downtown-comm-dist05.jpg" width="1920" height="1440" alt="A brick corner building with striped awnings in downtown Plant City" loading="lazy" decoding="async" style="object-position:62% 60%"></figure>
    <p class="imprint">© 2026 Tampa Bay Screen Repair · Plant City, Florida · <a href="index.html">Home</a> · <a href="services.html">Services</a> · <a href="screen-guide.html">Screen guide</a> · <a href="areas.html">Areas</a></p>
  </div>
  <p class="credits">Photographs show Florida pool cages and places, not this company's own jobs. Full credits on the <a href="index.html#credits">home page</a>.</p>
</footer>

<nav class="thumb-bar" aria-label="Call or text">
  <a href="tel:+18135165619">Call</a>
  <a href="{SMS}">Text a photo</a>
</nav>

<script src="main.js" defer></script>
</body>
</html>
'''

def page_head(h1, support, extra=''):
    return f'''
<section class="page-head" aria-label="Introduction">
  <div class="card">
    {STRIPE_DIV(160).replace('stripe thin', 'stripe')}
    <div class="card-body">
      <h1 data-rise style="--i:0">{h1}</h1>
      <p class="support" data-rise style="--i:1">{support}</p>
      {extra}
    </div>
  </div>
</section>
'''

QUOTE_BTN = f'<a class="button" href="index.html#quote" data-rise style="--i:2">Count your panels{STRIPE(22)}</a>'

# ---------- services ----------
SERVICES = [
  dict(id='panels', img='pool-screen-repair.jpg', w=1920, h=1080, alt='Fitting a new mesh panel into a white pool enclosure frame',
       title='Screen panel repair', price='Typical: wall panels from $45, roof panels from $75',
       text='A branch, a dog, a ball, or twelve Florida summers. We cut the old spline out, fit new mesh tight enough that there are no ripples, and match the colour of what is already there. Most single panels are done the day we arrive, and you do not need to be home.',
       bullets=['Wall, roof and door panels, any size', 'Charcoal 18×14 fibreglass as standard; no-see-um, pet screen and Florida Glass on request', 'New spline every time, never re-used', 'Loose neighbouring panels retightened while we are there']),
  dict(id='rescreen', img='sarasota-house-from-back-yard-2010.jpg', w=1023, h=629, alt='A Florida house with a full pool cage over the back patio under oak trees',
       title='Complete pool cage rescreen', price='Typical: from $1,200 for a single-story cage, priced as one job',
       text='When more panels are torn than whole, it is cheaper to do the lot and the mesh will all age together. Every panel comes out, every screw and anchor gets looked at, and the frame is cleaned before the new mesh goes on. A single story is usually two days; a two-story cage takes three or four.',
       bullets=['Every panel, walls and roof', 'Screws replaced throughout; rusted anchors swapped in the same hole', 'Pressure wash of the frame while the mesh is off, on request', 'Doors rescreened and rehung with new sweeps']),
  dict(id='lanai', img='seminole-saturday-spring-swim.jpg', w=1024, h=576, alt='A dark-framed pool cage at dusk with hedges and palms beyond',
       title='Lanai and porch screens', price='Typical: a standard lanai rescreen is a one-day job',
       text='Lanais, screened porches and patio rooms. We rescreen walls and ceilings, replace roof panels that have sagged after a leak, and fit privacy or no-see-um mesh where you need it. If the roof has been holding water, say so when you send the photos and we bring the right panels.',
       bullets=['Walls, ceilings and kick plates', 'Sagging or water-filled roof panels replaced', 'Privacy mesh and Florida Glass on the neighbour side', 'Screened-in porch built onto an existing roof, by quote']),
  dict(id='doors', img='quarters-no-9-unit-3-interior-screened.jpg', w=1920, h=1550, alt='A screened porch with white-painted frames and a screen door, archive photograph',
       title='Screen doors and hardware', price='Typical: door rescreen from $95, handle and latch set from $65, pet door from $140',
       text='Doors that drag, slam or will not latch. New handles, latches, closers and bug sweeps, or a whole new door hung square. We also cut pet doors into the screen door or a low panel so the dog stops going through the mesh.',
       bullets=['Rescreen with new bug sweep', 'Handles, latches, closers, hinges', 'New aluminium screen doors, hung and adjusted', 'Pet doors in the door or a low panel']),
  dict(id='anchors', img='pool-screen-repair-estimate.jpg', w=1920, h=1080, alt='A worker standing on the roof frame of a screen enclosure with a tape measure',
       title='Anchors, bolts and roof panels', price='Typical: anchor bolts from $12 each, fitted',
       text='Rusted anchor bolts are what fail first in a storm, and most cages over fifteen years old have a few. We replace them in the same hole with stainless, not a new hole next to it, and tighten the cage back down. Roof panels are measured from above and fitted from the walk boards.',
       bullets=['Anchor and tapcon replacement, same hole', 'Loose or missing screws throughout the frame', 'Roof panels of any size, fitted from walk boards', 'A pre-season check before June, by request']),
]

def services_page():
    out = head('Services', 'Screen panel repair, complete pool cage rescreens, lanai and porch screens, screen doors and hardware, anchors and roof panels. Plant City and East Hillsborough.', 'services')
    out += page_head('One panel or the whole cage', 'Everything we do to a pool cage, lanai or porch, with typical prices. Your written quote comes from Jerry after he sees the photos, and the bill matches it.', QUOTE_BTN)
    out += '<section class="page-body" aria-label="Services">\n'
    for s in SERVICES:
        li = ''.join(f'<li>{b}</li>' for b in s['bullets'])
        out += f'''  <article class="service" id="{s['id']}">
    <figure data-reveal="settle">
      <img src="assets/{s['img']}" width="{s['w']}" height="{s['h']}" alt="{s['alt']}" loading="lazy" decoding="async">
      <figcaption>Archive photograph of a Florida enclosure. Jerry's own job photos go here.</figcaption>
    </figure>
    <div class="text" data-reveal style="--i:1">
      <h2>{s['title']}</h2>
      <p>{s['text']}</p>
      <ul>{li}</ul>
      <p class="price">{s['price']}</p>
      <a class="button" href="index.html#quote">Get a written quote{STRIPE(22)}</a>
    </div>
  </article>
'''
    out += '''  <article class="service" id="extras">
    <figure data-reveal="settle">
      <img src="assets/sarasota-swimming-pool-in-new-home-1994.jpg" width="1020" height="636" alt="Inside a Florida pool cage, the mesh walls and roof framing the back yard" loading="lazy" decoding="async">
      <figcaption>Archive photograph, 1994.</figcaption>
    </figure>
    <div class="text" data-reveal style="--i:1">
      <h2>While we are up there</h2>
      <p>If we are on your ladder anyway, a few things cost little or nothing to add. Say so when you send the photos.</p>
      <ul><li>Gutters cleared</li><li>Branches that will tear the mesh again cut back</li><li>Frame pressure washed with a rescreen</li><li>A look at the cage for anything you have not noticed yet</li></ul>
      <p class="price">Ask. Often included.</p>
    </div>
  </article>
</section>
'''
    return out + FOOT

# ---------- areas ----------
TOWNS = [
  ('Plant City', 'Home base, zip 33565. Same-day for single panels most of the year. No trip charge anywhere in town.'),
  ('Brandon', 'Twenty minutes down I-4 and 60. Big cages on the older streets off Lumsden; we are there most weeks.'),
  ('Valrico', 'Two-story lanai cages are common here, and that is the job the 3½-day review was about. No trip charge.'),
  ('Seffner and Dover', 'Next door to Plant City. Often the same day you text, if the photo comes in the morning.'),
  ('Riverview', 'The newer cages have thinner spline and go first. We carry the right sizes. No trip charge.'),
  ('Lithia and FishHawk', 'Oak branches and squirrels are the usual culprits. Pet screen on the low panels pays for itself here.'),
  ('Thonotosassa', 'Lakeside houses mean no-see-ums; we recommend 20×20 mesh on the roof and the water side.'),
  ('Lakeland', 'West Polk, up to Lake Parker. No trip charge west of Florida Avenue; past that Jerry will say in the quote.'),
  ('Tampa', 'East of the river and south to Brandon Boulevard. Further west by arrangement, usually bundled with another job nearby.'),
  ('Wesley Chapel and Zephyrhills', 'By arrangement. Ask, and Jerry will tell you honestly whether the drive makes sense for the job.'),
]

def areas_page():
    out = head('Service areas', 'Pool cage and lanai screen repair in Plant City, Brandon, Valrico, Seffner, Dover, Riverview, Lithia, Thonotosassa, Lakeland and Tampa. No trip charge in East Hillsborough.', 'areas')
    out += page_head('Where we go', 'Based in Plant City and working across East Hillsborough and West Polk. No trip charge inside that area; outside it, Jerry says so in the quote before anyone drives.', f'<a class="button" href="{SMS}" data-rise style="--i:2">Text a photo{STRIPE(22)}</a>')
    out += '<section class="page-body" aria-label="Service areas">\n  <div class="towns-grid">\n'
    for i, (t, d) in enumerate(TOWNS):
        out += f'    <div data-reveal style="--i:{i % 5}"><h2>{t}</h2><p>{d}</p></div>\n'
    out += '''  </div>
  <div>
    <div class="strip-head" data-reveal><h2 class="head">The town we work from</h2><p>Plant City: brick, striped awnings, the CSX line through the middle, and the Strawberry Festival grounds. Most mornings start here and head west on I-4 or south on 39.</p></div>
    <div class="photo-strip">
      <figure data-reveal="settle" style="--i:0"><img src="assets/plant-city-fl-downtown-comm-dist05.jpg" width="1920" height="1440" alt="A brick corner building with striped awnings at Evers Street, downtown Plant City" loading="lazy" decoding="async"><figcaption><b>Evers Street</b>Downtown commercial district. Photo: Ebyabe, CC BY-SA 3.0.</figcaption></figure>
      <figure data-reveal="settle" style="--i:1"><img src="assets/plant-city-fl-downtown-comm-dist02.jpg" width="1920" height="1440" alt="Red brick shopfronts with green awnings in downtown Plant City" loading="lazy" decoding="async"><figcaption><b>Downtown</b>Shopfronts on the historic blocks. Photo: Ebyabe, CC BY-SA 3.0.</figcaption></figure>
      <figure data-reveal="settle" style="--i:2"><img src="assets/19970917-09-csx-plant-city-florida-6064973647.jpg" width="1800" height="1110" alt="A CSX freight locomotive on the line through Plant City, 1997" loading="lazy" decoding="async"><figcaption><b>The CSX line</b>Through the middle of town, 1997. Photo: David Wilson, CC BY 2.0.</figcaption></figure>
      <figure data-reveal="settle" style="--i:3"><img src="assets/florida-strawberry-festival-from-fl-574-2.jpg" width="1920" height="1440" alt="Buildings of the Florida Strawberry Festival grounds seen from State Road 574" loading="lazy" decoding="async"><figcaption><b>Strawberry Festival grounds</b>From State Road 574. Photo: DanTD, CC BY-SA 4.0.</figcaption></figure>
    </div>
  </div>
  <figure data-reveal="settle">
    <img src="assets/map-of-hillsborough-county-florida-loc-2012592403.jpg" width="1920" height="1446" alt="An 1882 survey map of Hillsborough County, Florida" loading="lazy" decoding="async">
    <figcaption class="small muted" style="margin-top:.6rem;max-width:70ch">Map of Hillsborough County, Florida, 1882. Florida Land and Improvement Co., Library of Congress, public domain. Plant City was founded three years later, where the railroad crosses the map's eastern edge.</figcaption>
  </figure>
  <div class="prose" data-reveal>
    <h2 class="head">Hours</h2>
    <p style="margin-top:1rem">Monday to Saturday, 8 am to 7 pm. Sunday by arrangement. Jerry is on a job most of the day, so text a photo any time and expect a written quote the same evening.</p>
    <p><a class="phone link-plain" href="tel:+18135165619">(813) 516-5619</a> · <a class="link-plain" href="mailto:TampaBayScreenRepair@gmail.com">TampaBayScreenRepair@gmail.com</a></p>
  </div>
</section>
'''
    return out + FOOT

# ---------- screen guide ----------
def guide_page():
    out = head('Screen guide', 'Which mesh for a Florida pool cage: standard 18×14, no-see-um 20×20, pet screen, Florida Glass. When to repair and when to rescreen. What to check before hurricane season.', 'guide')
    out += page_head('Which mesh, and when', 'Four kinds of screen do almost every job in Florida. Here is what each one is for, what it adds to the price, and how to tell whether your cage needs a panel or the lot.', QUOTE_BTN)
    out += '''<section class="page-body" aria-label="Screen guide">
  <div data-reveal>
    <h2 class="head">The four meshes</h2>
    <table class="guide-table" style="margin-top:1.5rem">
      <thead data-reveal style="--i:1"><tr><th>Mesh</th><th>Weave</th><th>What it is for</th><th>Where to use it</th><th>Per panel</th></tr></thead>
      <tbody>
        <tr data-reveal style="--i:1"><td>Standard fibreglass</td><td class="nums">18 × 14</td><td>What most Florida cages have. Best airflow, lasts seven to ten years in the sun.</td><td>Walls and roof</td><td class="nums">included</td></tr>
        <tr data-reveal style="--i:2"><td>No-see-um</td><td class="nums">20 × 20</td><td>A tighter weave that stops the tiny biting midges. Slightly less breeze.</td><td>Roof, and walls near pasture or water</td><td class="nums">+ $6</td></tr>
        <tr data-reveal style="--i:3"><td>Pet screen</td><td class="nums">17 × 20</td><td>Vinyl-coated polyester, about three times as tough as standard.</td><td>Low panels and screen doors</td><td class="nums">+ $15</td></tr>
        <tr data-reveal style="--i:4"><td>Florida Glass</td><td class="nums">18 × 14, laminated</td><td>Privacy, and it keeps mower clippings and dust out.</td><td>Lower panels only, never on a roof</td><td class="nums">+ $12</td></tr>
      </tbody>
    </table>
    <p class="small muted" style="margin-top:.8rem">Typical figures per panel on top of the panel price. Confirmed in your written quote.</p>
    <div class="photo-strip" style="margin-top:2.5rem">
      <figure data-reveal="settle" style="--i:0"><img src="assets/sarasota-swimming-pool-2010.jpg" width="1024" height="628" alt="A bright Florida pool cage with standard charcoal mesh" loading="lazy" decoding="async"><figcaption><b>Standard 18×14</b>The everyday cage: airflow first, charcoal so it disappears.</figcaption></figure>
      <figure data-reveal="settle" style="--i:1"><img src="assets/seminole-saturday-spring-swim.jpg" width="1024" height="576" alt="A pool cage at dusk beside hedges and palms" loading="lazy" decoding="async"><figcaption><b>No-see-um 20×20</b>Dusk by water or pasture is when the midges come. Use it on the roof and that side.</figcaption></figure>
      <figure data-reveal="settle" style="--i:2"><img src="assets/pool-screen-repair.jpg" width="1920" height="1080" alt="New mesh being fitted to the low wall panels of a pool enclosure" loading="lazy" decoding="async"><figcaption><b>Pet screen</b>The low panels and the door, where paws and branches hit.</figcaption></figure>
      <figure data-reveal="settle" style="--i:3"><img src="assets/quarters-no-9-unit-3-interior-screened.jpg" width="1920" height="1550" alt="A screened porch with a solid lower wall, archive photograph" loading="lazy" decoding="async"><figcaption><b>Florida Glass</b>Privacy on the neighbour side, lower panels only.</figcaption></figure>
    </div>
  </div>
  <div class="service">
    <figure data-reveal="settle">
      <img src="assets/window-screen-2878481856.jpg" width="1280" height="960" alt="Fibreglass mesh close up against an evening sky" loading="lazy" decoding="async">
      <figcaption>Photograph: "Window Screen" by daryl_mitchell, CC BY-SA 2.0, via Wikimedia Commons.</figcaption>
    </figure>
    <div class="text" data-reveal style="--i:1">
      <h2>Repair or rescreen?</h2>
      <p>Press a thumb into a panel that looks fine. If the mesh feels dry and papery, or a corner tears when you push, it is brittle and the rest is not far behind. If more than a third of the panels are torn or brittle, a full rescreen is cheaper per panel and the mesh will all age together.</p>
      <p>If the frame is sound and most panels still give and spring back, repair the torn ones and keep your money. Jerry will tell you which it is from the photos, and he will say so if a repair is the better deal.</p>
    </div>
  </div>
  <div class="service">
    <figure data-reveal="settle">
      <img src="assets/pool-screen-repair-estimate.jpg" width="1920" height="1080" alt="Measuring the roof of a screen enclosure from the top frame" loading="lazy" decoding="async">
      <figcaption>Archive photograph.</figcaption>
    </figure>
    <div class="text" data-reveal style="--i:1">
      <h2>Before June</h2>
      <p>Loose panels and rusted anchors are what fail first in a storm. A spring check takes an hour and is cheaper than a cage on the pool deck in September.</p>
      <ul>
        <li>Anchor bolts: rust streaks at the base of a post mean they are going. Replace in the same hole.</li>
        <li>Screws along the roof beams: any that spin or are missing.</li>
        <li>Panels that flap: a loose panel pulls the spline out of its neighbours.</li>
        <li>Doors: a door that does not latch will swing in the wind and tear the panel beside it.</li>
      </ul>
      <p class="price">Pre-season check: ask when you text</p>
      <a class="button" href="index.html#quote">Count your panels''' + STRIPE(22) + '''</a>
    </div>
  </div>
</section>
'''
    return out + FOOT

if __name__ == '__main__':
    (ROOT / 'services.html').write_text(services_page())
    (ROOT / 'areas.html').write_text(areas_page())
    (ROOT / 'screen-guide.html').write_text(guide_page())
    print('wrote services.html, areas.html, screen-guide.html')
