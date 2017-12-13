from paaf import db
from paaf.models import park, asset, value_generating_practice, value_domain, asset_value_domain_attributes

def seed_asset1():
    assets=[]
    a=asset('Biophysical', 'the biotic and abiotic attributes present within the boundaries of the PA')
    db.session.add(a)
    db.session.commit()

    b = asset('Scenic beauty',description="",parent_id=a.id)
    db.session.add(b)
    db.session.commit()
    assets.append(asset('Vistas and panoramas',"",b.id))

    c = asset('Natural Features and formations',"",a.id)
    db.session.add(c)
    db.session.commit()
    assets.append(asset('Topographic',"waterfalls, white water mountain ranges",c.id))
    assets.append(asset('Geomorphic',"cliffs, caves, inselbergs etc.",c.id))

    d = asset('Natural spectacles',"",a.id)
    db.session.add(d)
    db.session.commit()
    assets.append(asset('Biotic',"mating aggregations, congregations, predator - prey interactions, autumn colours.",d.id))
    assets.append(asset('Abiotic',"Geysers, volcanic eruptions.",d.id))

    e = asset('Renewable Natural Resources',"",a.id)
    db.session.add(e)
    db.session.commit()

    assets.append(asset('Biodiversity / Genetic resources',"e.g.species diversity, for bio - prospecting or ancestors of crops or domestic animals, etc.",e.id))
    assets.append(asset('Non Timber Products',"medicinal plants, foods, resins, fruits, fungi, etc.",e.id))
    assets.append(asset('Timber',"",e.id))
    assets.append(asset('Fish and Game',"",e.id))
    assets.append(asset('Carbon stocks',"",e.id))
    assets.append(asset('Wind for wind power',"",e.id))
    assets.append(asset('River flows for hydro - power',"",e.id))

    f = asset('Non - renewable Natural resources',"",a.id)
    db.session.add(f)
    db.session.commit()
    assets.append(asset('Minerals',"",f.id))
    assets.append(asset('Oil, Gas, coal',"",f.id))
    assets.append(asset('Fossils',"",f.id))

    g = asset('Species Assets',"",a.id)
    db.session.add(g)
    db.session.commit()
    assets.append(asset('Iconic and emblematic species or individuals',"famous animals, state symbols, brands, etc.",g.id))
    assets.append(asset('Species of conservation importance',"rare species, endemic species, keystone species, etc.",g.id))
    assets.append(asset('Species of recreational importance',"e.g. recreational fisheries, etc.",g.id))
    assets.append(asset('Species of economical importance',"",g.id))

    h = asset('Ecosystem Assets',"",a.id)
    db.session.add(h)
    db.session.commit()
    assets.append(asset('Habitat / ecosystem diversity',"",h.id))
    assets.append(asset('Habitat of highly restricted / endangered species',"",h.id))
    assets.append(asset('Ecosystem functions that create supporting ecosystem services',"nutrient recycling, primary production, soil formation, pollination",h.id))
    assets.append(asset('Ecosystem functions that create regulating ecosystem services',"Carbon sequestration, Hydrological cycling / watershed, Decomposition, Predation, Population cycling",h.id))


    i = asset('Outdoor recreation assetsfeatures',"e.g.white - water, climbable cliff - face, ski - slope, etc.",a.id)
    db.session.add(i)
    db.session.commit()

    j = asset('Agricultural land, water and soil resource',"'.",a.id)
    db.session.add(j)
    db.session.commit()

    assets.append(asset('Existing agricultural or pasture lands',"",j.id))
    assets.append(asset('Existing fisheries or aquaculture',"",j.id))
    assets.append(asset('Existing fisheries or aquaculture',"Land or waters with suitability for existing agriculture or aquaculture",j.id))

    for at in assets:
        db.session.add(at)
    db.session.commit()

def seed_asset2():
    assets=[]

    a = asset('Human Assets',"the groups of people associated with the protected area with knowledge and / or skills that enable the conservation of PA assets and the generation and capture of value from these assets.")
    db.session.add(a)
    db.session.commit()

    b = asset('Park technical and management staff',"",a.id)
    db.session.add(b)
    db.session.commit()
    assets.append(asset('Permanent',"e.g. government employees",b.id))
    assets.append(asset('Temporary',"e.g. contract staff",b.id))

    c = asset('Park rangers',"",a.id)
    db.session.add(c)
    db.session.commit()

    c = asset('Guides',"",a.id)
    db.session.add(c)
    db.session.commit()

    c = asset('Park volunteers',"members of Friends Groups",a.id)
    db.session.add(c)
    db.session.commit()

    c = asset('Researchers',"",a.id)
    db.session.add(c)
    db.session.commit()

    c = asset('Traditional peoples with local ecological and resource use knowledge',"e.g.artisanal fishermen, herbalists, Shamans / Caciques, etc.",a.id)
    db.session.add(c)
    db.session.commit()

    c = asset('Researchers',"e.g.birdwatchers, cavers, etc.",a.id)
    db.session.add(c)
    db.session.commit()

    c = asset('Fireman',"",a.id)
    db.session.add(c)
    db.session.commit()

    for at in assets:
        db.session.add(at)
    db.session.commit()

def seed_asset3():
    assets = []

    a = asset('Infrastructure Assets',"the facilities that have been constructed in, around or to the PA that enable value generation and capture.")
    db.session.add(a)
    db.session.commit()

    b = asset('Private Transport Access (to PA)',"",a.id)
    db.session.add(b)
    db.session.commit()
    assets.append(asset('Roads',"",b.id))
    assets.append(asset('Carparks or marinas',"",b.id))

    b = asset('Public transport access (to PA)',"",a.id)
    db.session.add(b)
    db.session.commit()
    assets.append(asset('Bus service (to the PA)',"",b.id))
    assets.append(asset('Ferry service (to the PA)',"",b.id))
    assets.append(asset('Rail service (to the nearest town)',"",b.id))
    assets.append(asset('Taxi service (car or boat)',"",b.id))
    assets.append(asset('Airstrip',"",b.id))

    b = asset('PA Visitor infrastructure',"",a.id)
    db.session.add(b)
    db.session.commit()
    assets.append(asset('Trail systems',"e.g.trails, viewpoints, signage",b.id))
    assets.append(asset('Bridges and walkways',"",b.id))
    assets.append(asset('Internal PA transport',"cable car, tram, etc.",b.id))
    assets.append(asset('Accommodation',"hotels, hostels, homestays",b.id))
    assets.append(asset('Camp sites',"",b.id))
    assets.append(asset('Visitor amenities',"(e.g.information centre, cafe, toilets, shops, picnic sites)",b.id))
    assets.append(asset('Zoological and botanical gardens, museums',"",b.id))

    b = asset('Park management assets',"",a.id)
    db.session.add(b)
    db.session.commit()
    assets.append(asset('Offices and workshops',"",b.id))
    assets.append(asset('Other property / buildings',"e.g.staff accommodation, derelict houses, etc.",b.id))
    assets.append(asset('Vehicles ',"e.g.cars, tractors",b.id))
    assets.append(asset('Major equipment ',"e.g.radio station, fire towers",b.id))
    assets.append(asset('Plant nursery and captive breeding facilities',"",b.id))


    b = asset('Public utilities available to the park',"",a.id)
    db.session.add(b)
    db.session.commit()
    assets.append(asset('Electricity',"",b.id))
    assets.append(asset('Potable water',"",b.id))
    assets.append(asset('Sewerage',"",b.id))
    assets.append(asset('Telephone',"",b.id))
    assets.append(asset('Broadband',"",b.id))


    b = asset('Emergency services accessible to PA users',"e.g.helicopter evacuation, paramedic ambulance",a.id)
    db.session.add(b)
    db.session.commit()

    b = asset('Research infrastructure',"e.g.permanent plot, canopy tower, herbarium, library, etc.",a.id)
    db.session.add(b)
    db.session.commit()

    b = asset('Built monument and public artwork',"e.g.sculpture, religious shrine",a.id)
    db.session.add(b)
    db.session.commit()

    b = asset('Dams',"",a.id)
    db.session.add(b)
    db.session.commit()

    for at in assets:
        db.session.add(at)
    db.session.commit()

def seed_asset4():
    assets = []

    a = asset('Institutional Assets',
                   "the legal frameworks that construct a PA and the structures and contractual agreements that conserve assets and enable value generation and capture from them.")
    db.session.add(a)
    db.session.commit()

    b = asset('Conservation designations', "", a.id)
    db.session.add(b)
    db.session.commit()
    assets.append(asset('National PA designations (e.g.SNUC type, RPPN)',"",b.id))
    assets.append(asset('International PA designations (Ramsar, World heritage, Biosphere reserve)',"",b.id))
    assets.append(asset('NGO site designations (e.g.KBA, IBA, AZA, etc.)',"",b.id))

    b = asset('Decision making structure', "", a.id)
    db.session.add(b)
    db.session.commit()
    assets.append(asset('Management plans',"",b.id))
    assets.append(asset('Zonation plans',"",b.id))
    assets.append(asset('Governance entities ',"e.g.advisory boards, stakeholder group)",b.id))

    b = asset('Partnership and commercial agreements', "", a.id)
    db.session.add(b)
    db.session.commit()
    assets.append(asset('Community and co-management agreements',"",b.id))
    assets.append(asset('PES contracts',"e.g.REDD agreement",b.id))
    assets.append(asset('Commercial sponsorship agreements',"",b.id))
    assets.append(asset('Concessionaire agreements ',"ecotourism and recreation companies, visitor amenity providers",b.id))
    assets.append(asset('Budget supplement agreement ',"e.g.ICMS_Ecologico agreement with municipality",b.id))
    assets.append(asset('Research agreement ',"e.g.university partner",b.id))
    assets.append(asset('Other agreements ',"e.g.Governance - partners to solve land invasion",b.id))

    for at in assets:
        db.session.add(at)
    db.session.commit()

def seed_asset5():
    assets = []

    a = asset('Cultural Assets',
                   "the interactions between the PA and wider cultural practices and narratives that create a public identity for the PA.")
    db.session.add(a)
    db.session.commit()

    b = asset('Brand / emblem based on biophysical PA asset', "e.g.manatee", a.id)
    db.session.add(b)
    db.session.commit()
    assets.append(asset('e.g.manateePublic ', "e.g.municipality)",b.id))
    assets.append(asset('Commercial', "",b.id))
    assets.append(asset('Civil society ', "NGO, sportclub, etc.)",b.id))

    b = asset('Creative interpretations', "", a.id)
    db.session.add(b)
    db.session.commit()
    assets.append(asset('Iconic imagery ', "e.g.classic landscape photos)",b.id))
    assets.append(asset('Other artistic interpretations ', "e.g.paintings, lyrics, novels",b.id))


    b = asset('Cultural events', "e.g. fairs and festivals", a.id)
    db.session.add(b)
    db.session.commit()

    b = asset('Media representations', "e.g.manatee", a.id)
    db.session.add(b)
    db.session.commit()
    assets.append(asset('Print media',"e.g.guide books, coffee table books",b.id))
    assets.append(asset('Audio-visual',"e.g.TV documentaries",b.id))
    assets.append(asset('Digital presence',"e.g.websites, social networks, etc.",b.id))

    b = asset('Myths and legends associated with the PA', "e.g.folk myths, associations with famous events", a.id)
    db.session.add(b)
    db.session.commit()

    b = asset('Celebrity associations', "e.g.famous person or popular celebrity", a.id)
    db.session.add(b)
    db.session.commit()

    b = asset('Recreational clubs and associations', "", a.id)
    db.session.add(b)
    db.session.commit()

    b = asset('Monuments', "e.g.monumental sculptures, cave paintings, ruins, remains of past", a.id)
    db.session.add(b)
    db.session.commit()

    b = asset('Buildings of architectural value', "modern or historical", a.id)
    db.session.add(b)
    db.session.commit()

    b = asset('Educational programmes', "", a.id)
    db.session.add(b)
    db.session.commit()


    for at in assets:
        db.session.add(at)
    db.session.commit()

def seed_vgps():
    assets = []

    a = value_generating_practice('Nature-based recreations',"")
    db.session.add(a)
    db.session.commit()
    assets.append(value_generating_practice('Fishing', "", a.id))
    assets.append(value_generating_practice('Hunting', "", a.id))
    assets.append(value_generating_practice('Birding', "", a.id))
    assets.append(value_generating_practice('Collecting', "mushrooms etc.", a.id))
    assets.append(value_generating_practice('Natural history', "specialists e.g botany, entymology", a.id))
    assets.append(value_generating_practice('Nature photography', "", a.id))
    assets.append(value_generating_practice('Trekking/hiking', "", a.id))


    a = value_generating_practice('Adventure recreations',"")
    db.session.add(a)
    db.session.commit()
    assets.append(value_generating_practice('Fishing', "", a.id))
    assets.append(value_generating_practice('Diving', "", a.id))
    assets.append(value_generating_practice('Rafting', "", a.id))
    assets.append(value_generating_practice('Climbing/tree climbing', "", a.id))
    assets.append(value_generating_practice('Caving/pot holing', "", a.id))
    assets.append(value_generating_practice('Para-gliding', "", a.id))
    assets.append(value_generating_practice('Canyoning', "", a.id))


    a = value_generating_practice('Activity sports',"")
    db.session.add(a)
    db.session.commit()
    assets.append(value_generating_practice('Sailing', "", a.id))
    assets.append(value_generating_practice('Canoeing/Kayaking', "", a.id))
    assets.append(value_generating_practice('Road Cycling', "", a.id))
    assets.append(value_generating_practice('Mountain biking', "", a.id))
    assets.append(value_generating_practice('Open-water swimming', "", a.id))
    assets.append(value_generating_practice('Jet-skiing', "", a.id))

    a = value_generating_practice('Touring',"")
    db.session.add(a)
    db.session.commit()
    assets.append(value_generating_practice('Safari', "", a.id))
    assets.append(value_generating_practice('Car tour/scenic drive', "", a.id))
    assets.append(value_generating_practice('Boat tour', "", a.id))
    assets.append(value_generating_practice('Educational/Cultural tours', "", a.id))

    a = value_generating_practice('Natural living',"")
    db.session.add(a)
    db.session.commit()
    assets.append(value_generating_practice('Camping/Glamping', "", a.id))
    assets.append(value_generating_practice('Picnicking/BBQ-ing', "", a.id))
    assets.append(value_generating_practice('Authentic accommodation', "", a.id))
    assets.append(value_generating_practice('Traditional dining', "", a.id))
    assets.append(value_generating_practice('Idle-ing/chilling', "", a.id))
    assets.append(value_generating_practice('Naturism', "", a.id))

    a = value_generating_practice('Volunteering', "")
    db.session.add(a)
    db.session.commit()

    a = value_generating_practice('Natural area management', "")
    db.session.add(a)
    db.session.commit()
    assets.append(value_generating_practice('Patrolling and guarding', "", a.id))
    assets.append(value_generating_practice('Habitat & species management', "", a.id))
    assets.append(value_generating_practice('Volunteering', "", a.id))


    for at in assets:
        db.session.add(at)
    db.session.commit()



def seed_domain_forms_of_value():
    assets = []

    a = value_domain('Everyday Life',"")
    db.session.add(a)
    db.session.commit()

    b = value_domain('Health', "", a.id)
    db.session.add(b)
    db.session.commit()
    assets.append(value_domain('Mental', "", b.id))
    assets.append(value_domain('Physical', "", b.id))

    b = value_domain('Belongingness', "", a.id)
    db.session.add(b)
    db.session.commit()
    assets.append(value_domain('Cameradre and sociality', "", b.id))
    assets.append(value_domain('Sence of place and identity', "", b.id))

    b = value_domain('Esteem', "", a.id)
    db.session.add(b)
    db.session.commit()
    assets.append(value_domain('Sence of purpose', "", b.id))
    assets.append(value_domain('Achieving a goal', "e.g summiting moutain", b.id))
    assets.append(value_domain('Developing a skill', "e.g bird id, skiiing", b.id))
    assets.append(value_domain('Standing in a community', "", b.id))

    b = value_domain('Self actualisation', "", a.id)
    db.session.add(b)
    db.session.commit()
    assets.append(value_domain('Spiritual and aesthetic expression', "", b.id))

    a = value_domain('Professional and organisational life', "")
    db.session.add(a)
    db.session.commit()
    assets.append(value_domain('Mission and purpose', "", a.id))
    assets.append(value_domain('Domains of expertise', "", a.id))

    b = value_domain('Careers', "", a.id)
    db.session.add(b)
    db.session.commit()
    assets.append(value_domain('Vocational careers', "", b.id))

    b = value_domain('Access to decision making forums', "", a.id)
    db.session.add(b)
    db.session.commit()

    b = value_domain('Income streams', "", a.id)
    db.session.add(b)
    db.session.commit()
    assets.append(value_domain('Membership dues', "", b.id))
    assets.append(value_domain('Philanthropy', "", b.id))
    assets.append(value_domain('Grants and trusts', "", b.id))
    assets.append(value_domain('Consultancy contracts', "", b.id))

    b = value_domain('Partnerships', "", a.id)
    db.session.add(b)
    db.session.commit()
    assets.append(value_domain('Government agencies', "", b.id))
    assets.append(value_domain('NGOs/CSOs', "", b.id))
    assets.append(value_domain('Companies', "", b.id))
    assets.append(value_domain('Communities', "", b.id))


    a = value_domain('Economy and enterprise', "")
    db.session.add(a)
    db.session.commit()
    assets.append(value_domain('Ecosystem services', "", a.id))
    assets.append(value_domain('Concessions and contracts', "", a.id))

    b = value_domain('Entreprenurial activities', "", a.id)
    db.session.add(b)
    db.session.commit()
    assets.append(value_domain('SME', "", b.id))
    assets.append(value_domain('Rural entreprenuers', "", b.id))
    assets.append(value_domain('Jobs', "", b.id))

    assets.append(value_domain('Place branding', "", a.id))
    assets.append(value_domain('Urban rural enterprise flows', "", a.id))


    a = value_domain('Poltics and Diplomacy', "")
    db.session.add(a)
    db.session.commit()

    b = value_domain('Collective identities', "", a.id)
    db.session.add(b)
    db.session.commit()
    assets.append(value_domain('National', "", b.id))
    assets.append(value_domain('Regional and local', "", b.id))
    assets.append(value_domain('Cultural', "", b.id))

    b = value_domain('International standing', "", a.id)
    db.session.add(b)
    db.session.commit()
    assets.append(value_domain('Policy leadership', "", b.id))
    assets.append(value_domain('Progressive coalitions', "", b.id))

    assets.append(value_domain('Governance of remote regions', "", a.id))
    assets.append(value_domain('Territorial integrity', "", a.id))
    assets.append(value_domain('Urban-rural flows', "", a.id))


    for at in assets:
        db.session.add(at)
    db.session.commit()

def run_seed():
    seed_asset1()
    seed_asset2()
    seed_asset3()
    seed_asset4()
    seed_asset5()
    seed_vgps()
    seed_domain_forms_of_value()