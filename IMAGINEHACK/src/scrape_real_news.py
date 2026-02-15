# -*- coding: utf-8 -*-
"""
real news dataset by scraping url links
"""

# src/scrape_real_news.py
from newspaper import Article
import pandas as pd

urls = [
    'https://www.thestar.com.my/news/nation/2025/06/21/malaysian-embassy-in-iran-to-temporarily-cease-operations',
    'https://www.thestar.com.my/aseanplus/aseanplus-news/2025/06/21/staff-at-second-hand-luxury-stores-in-hong-kong-fear-for-safety-after-robbery',
    'https://www.thestar.com.my/news/nation/2025/06/21/body-of-foreign-woman-found-with-head-injuries-in-bandar-tasik-puteri-cops-open-murder-probe',
    'https://www.thestar.com.my/aseanplus/aseanplus-news/2025/06/21/man-dies-after-collapsing-at-singapore039s-national-day-parade-rehearsal',
    'https://www.thestar.com.my/news/true-or-not/2023/07/12/quickcheck-does-eating-durian-increase-your-cholesterol-levels',
    'https://www.thestar.com.my/news/nation/2025/06/21/whatsapp-to-the-rescue-lost-teens-found-after-sharing-location-with-bomba',
    'https://www.thestar.com.my/aseanplus/aseanplus-news/2025/06/21/chinese-teams-edible-fruit-coating-can-more-than-double-shelf-life-paper',
    'https://www.thestar.com.my/news/nation/2025/06/21/34-firemen-nine-fire-engines-deployed-to-battle-masai-oil-storage-facility-blaze',
    'https://www.thestar.com.my/sport/hockey/2025/06/21/malaysia-suffer-first-ever-defeat-to-wales-and-finish-sixth-in-nations-cup',
    'https://www.thestar.com.my/news/nation/2025/06/21/expansion-of-sst-burdens-people-and-raises-prices-says-dr-wee',
    'https://www.thestar.com.my/aseanplus/aseanplus-news/2025/06/21/indonesia-evacuates-100-citizens-from-iran-and-israel-amid-regional-tensions',
    'https://www.thestar.com.my/news/nation/2025/06/21/actress-singer-fazura-prefers-to-leave-legal-issues-to-lawyers-prefers-to-concentrate-on-new-single-composed-by-indonesian-ace-ade-govinda',
    'https://www.thestar.com.my/news/nation/2025/06/21/more-than-10000-given-community-service-orders-from-2008-to-2024-says-nancy-shukri',
    'https://www.thestar.com.my/news/nation/2025/06/21/klang-fatal-shooting-i-thought-it-was-a-crow-shooting-operation-says-shop-owner',
    'https://www.thestar.com.my/news/nation/2025/06/21/fire-destroys-oil-storage-facility-in-masai',
    'https://www.thestar.com.my/news/nation/2025/06/21/viral-video-of-bullying-at-school-prompts-police-investigation',
    'https://www.thestar.com.my/news/nation/2025/06/21/over-400kg-of-rubbish-collected-in-teluk-likas-beach-cleanup',
    'https://www.thestar.com.my/news/nation/2025/06/21/woman-killed-husband-injured-in-petrol-stall-fire-in-beluran',
    'https://www.thestar.com.my/news/nation/2025/06/21/boy-injured-in-bukit-rambai-tragedy-discharged',
    'https://www.thestar.com.my/news/nation/2025/06/21/accident-claims-life-of-14-year-old-pillion-rider-in-ulu-tiram',
    'https://www.thestar.com.my/news/nation/2025/06/21/perak-mentri-besar-urges-calm-over-mysterious-tremors',
    'https://www.thestar.com.my/news/nation/2025/06/21/fire-destroys-80-of-factory-in-kampung-lembah-kinrara',
    'https://www.thestar.com.my/news/nation/2025/06/21/retired-factory-worker-loses-rm733300-to-online-investment-scam',
    'https://www.thestar.com.my/news/nation/2025/06/21/perak-seeks-comprehensive-upgrade-of-east-west-highway',
    'https://www.thestar.com.my/news/nation/2025/06/21/couple-held-for-series-of-housebreakings-robberies-since-january',
    'https://www.thestar.com.my/news/nation/2025/06/21/do-not-take-israel-iran-conflict-lightly-says-defence-minister',
    'https://www.thestar.com.my/news/nation/2025/06/21/gof-foils-attempt-to-smuggle-19000kg-of-white-rice-from-thailand',
    'https://www.thestar.com.my/news/nation/2025/06/21/klia-aerotrain-set-to-resume-service-on-july-1',
    'https://www.thestar.com.my/news/nation/2025/06/21/three-malaysian-haj-pilgrims-die-from-heart-attacks-in-saudi',
    'https://www.thestar.com.my/news/nation/2025/06/21/police-nab-man-who-drove-off-with-special-needs-girl-in-penaga',
    'https://www.thestar.com.my/news/nation/2025/06/21/dr-wee-officiates-the-launch-of-malaysian-business-law-review-20252026-edition',
    'https://www.thestar.com.my/news/nation/2025/06/21/20-years-of-make-up-neglect-proves-a-skin-credible-mistake',
    'https://www.thestar.com.my/news/nation/2025/06/21/schoolkids-do-malaysia-proud',
    'https://www.thestar.com.my/news/nation/2025/06/21/wild-jumbo-captured-relocated',
    'https://www.malaymail.com/news/malaysia/2025/06/21/fatwa-cant-bind-sis-forum-as-a-company-says-court-case-focused-on-administrative-powers-not-islamic-tenets-says-chief-justice/181183',
    'https://www.malaymail.com/news/malaysia/2025/06/21/as-police-look-on-student-demonstraters-take-to-kk-streets-to-call-for-reform-video/181204',
    'https://www.malaymail.com/news/malaysia/2025/06/21/thick-smoke-and-explosions-reported-as-johor-baru-factory-burns-video/181200',
    'https://www.malaymail.com/news/malaysia/2025/06/21/police-probe-bullying-case-at-klang-school-after-toilet-assault-video-goes-viral/181202',
    'https://www.malaymail.com/news/malaysia/2025/06/21/pms-office-delivers-assistance-to-cancer-stricken-single-mother-in-kampung-tebing-tinggi/181196',
    'https://www.malaymail.com/news/malaysia/2025/06/21/penang-to-continue-vape-industry-talks-before-deciding-on-possible-ban-says-state-exco/181193',
    'https://www.malaymail.com/news/malaysia/2025/06/21/after-deadly-bus-crash-perak-mb-urges-federal-support-for-east-west-highway-and-gerik-hospital-upgrades-in-13mp/181191',
    'https://www.malaymail.com/news/malaysia/2025/06/21/perak-mb-orders-full-probe-after-mysterious-explosions-tremors-rattle-ipoh-residents-again/181185',
    'https://www.malaymail.com/news/malaysia/2025/06/21/klang-fatal-shooting-i-thought-it-was-a-crow-shooting-operation-says-witness-after-man-found-dead-in-pickup/181189',
    'https://www.malaymail.com/news/malaysia/2025/06/21/serdang-hospital-gives-pm-anwar-clean-bill-of-health-after-annual-check-up/181174',
    'https://www.malaymail.com/news/malaysia/2025/06/21/metmalaysia-issues-thunderstorm-and-strong-wind-warning-for-seven-states-and-labuan-until-5pm-today/181175',
    'https://www.malaymail.com/news/malaysia/2025/06/21/rukun-tetangga-turns-50-with-fresh-focus-on-youth-unity-and-volunteerism-says-deputy-unity-minister/181178',
    'https://www.malaymail.com/news/malaysia/2025/06/20/man-found-dead-in-vehicle-outside-klang-motorcycle-shop-believed-to-be-shot/181098',
    'https://www.malaymail.com/news/malaysia/2025/06/21/klia-aerotrain-to-resume-service-for-travellers-on-july-1-transport-ministry-announces/181134',
    'https://www.malaymail.com/news/malaysia/2025/06/21/factory-fire-guts-80pc-of-building-in-puchongs-kampung-lembah-kinrara-no-casualties-reported/181163',
    'https://www.malaymail.com/news/world/2025/06/21/pakistan-to-nominate-trump-for-nobel-peace-prize-calls-him-a-genuine-peacemaker-with-stellar-statesmanship/181197',
    'https://www.malaymail.com/news/world/2025/06/21/thai-pm-will-continue-to-perform-her-duty-is-not-resigning-or-dissolving-parliament-ruling-party-official-says/181201',
    'https://www.malaymail.com/news/world/2025/06/21/israel-claims-killing-of-iranian-commander-who-allegedly-helped-fund-arm-hamas/181179',
    'https://www.malaymail.com/news/showbiz/2025/06/21/barbie-hsus-widower-dj-koo-rumoured-to-be-shopping-for-new-home-closer-to-her-grave/181192',
    'https://www.malaymail.com/news/world/2025/06/21/india-says-indus-treaty-with-pakistan-will-never-be-restored-vows-to-divert-river-flow/181188',
    'https://www.malaymail.com/news/showbiz/2025/06/21/a-meeting-of-old-friends-fans-thrilled-to-see-carina-lau-sharing-pic-with-stephen-chow/181195',
    'https://www.nst.com.my/news/nation/2025/06/1234083/27-homes-near-kota-puteri-industrial-park-evacuated',
    'https://www.nst.com.my/news/nation/2025/06/1234070/blaze-destroys-three-factories-15-vehicles-johor-industrial-park',
    'https://www.nst.com.my/news/nation/2025/06/1234067/penang-mourns-passing-co-founder-iconic-air-itam-sister-curry-mee',
    'https://www.nst.com.my/world/region/2025/06/1234065/cambodia-reports-fifth-bird-flu-death-year',
    "https://www.nst.com.my/news/nation/2025/06/1232064/flawed-bus-seat-design-puts-passengers-risk-expert-warns",
    "https://www.nst.com.my/news/nation/2025/06/1232062/violent-crime-fears-rise-homicide-rate-stays-low",
    "https://www.nst.com.my/news/nation/2025/06/1232036/malaysians-living-longer-not-healthier-says-pm",
    "https://www.malaymail.com/news/malaysia/2025/06/19/trade-nuclear-energy-tech-deals-dpm-fadillah-heads-to-uzbekistan-russia-to-deepen-bilateral-ties/180887",
    "https://www.malaymail.com/news/malaysia/2025/06/19/anwar-malaysia-us-tariff-talks-going-excellent-urges-fair-deal-for-asean-too/180883",
    "https://www.malaymail.com/news/malaysia/2025/06/18/ai-blockchain-tech-can-either-fight-corruption-or-fuel-it-says-macc-chief/180805",
    "https://www.malaymail.com/news/malaysia/2025/06/18/johor-mb-over-rm2-million-allocated-to-upgrade-digital-systems-at-state-land-office-to-ease-transactions/180803",
    "https://www.malaymail.com/news/malaysia/2025/06/18/govt-to-evacuate-malaysians-in-iran-this-friday-says-fahmi-as-middle-east-tensions-worsen/180797",
    "https://www.malaymail.com/news/malaysia/2025/06/18/now-everyone-can-get-5pc-discount-on-penangs-overhang-properties-says-chief-minister/180785",
    "https://www.malaymail.com/news/malaysia/2025/06/18/online-scams-dominate-kelantans-commercial-crime-list-over-rm14m-lost-this-year/180784",
    "https://www.malaymail.com/news/malaysia/2025/06/18/melaka-teen-charged-with-murdering-mum-and-brother-injuring-younger-sibling-in-family-tragedy/180777",
    "http://malaymail.com/news/malaysia/2025/06/18/two-sabah-assemblymen-one-civilian-to-be-charged-in-mining-graft-case-this-month-says-macc-chief/180770",
    "https://www.malaymail.com/news/malaysia/2025/06/17/thai-woman-found-dead-in-front-of-puchong-shop-police-rule-out-foul-play/180692",
    "https://www.malaymail.com/news/malaysia/2025/06/17/in-johor-three-men-claim-trial-to-bribing-senior-immigration-officer-after-nightclub-raid/180690",
    "https://www.malaymail.com/news/malaysia/2025/06/17/bnm-food-prices-up-175pc-since-2020-but-wages-lag-fuelling-malaysias-cost-of-living-strain/180677",
    "https://www.malaymail.com/news/malaysia/2025/06/16/tiger-returns-to-kampung-ulu-dingin-leaving-villagers-fearful-after-latest-livestock-attack/180604",
    "https://www.malaymail.com/news/malaysia/2025/06/16/why-malaysias-smallest-bear-matters-and-what-we-need-to-do-to-save-them/179593",
    "https://www.malaymail.com/news/malaysia/2025/06/15/sabah-cm-hints-at-possible-state-polls-announcement-after-late-july-party-meet/180491",
    "https://www.malaymail.com/news/malaysia/2025/06/15/ampang-cop-taken-off-duty-pending-probe-into-alleged-lewd-act-in-viral-clip/180494",
    "https://www.malaymail.com/news/malaysia/2025/06/15/anwar-hails-progress-on-lcs-project-stresses-importance-of-good-governance/180487",
    "https://www.malaymail.com/news/malaysia/2025/06/15/all-must-play-a-role-in-strengthening-unity-raja-of-perlis-decrees/180489",
    "https://www.malaymail.com/news/malaysia/2025/06/15/king-and-queen-honour-all-dads-calls-them-backbone-of-the-family-in-fathers-day-message/180402",
    "https://www.thestar.com.my/news/nation/2025/05/23/two-chinese-nationals-killed-in-accident-on-highway-in-pahang",
    "https://www.thestar.com.my/news/nation/2025/05/23/pkr-polls-incoming-pkr-deputy-president-nurul-izzah-to-focus-on-party-unity-and-reforms",
    "https://www.thestar.com.my/news/nation/2025/05/23/pm-anwar-wins-pkr-president-post-unchallenged",
    "https://www.thestar.com.my/news/nation/2025/05/23/pm-anwar-defends-macc-chief039s-extension-highlights-anti-corruption-efforts",
    "https://www.thestar.com.my/news/nation/2025/05/23/pkr-polls-nurul-izzah-announced-as-new-pkr-deputy-president",
    "https://www.thestar.com.my/news/nation/2025/05/23/viral-video-case-melaka-to-ensure-welfare-of-disabled-elderly-man-guaranteed",
    "https://www.thestar.com.my/news/nation/2025/05/23/rafizi-ramli-makes-late-entrance-at-pkr-national-congress",
    "https://www.thestar.com.my/news/nation/2025/05/23/candidates-aligned-with-nurul-izzah-rafizi-succeed-in-pkr-elections",
    "https://www.thestar.com.my/news/nation/2025/05/23/statements-from-24-individuals-recorded-in-connection-with-hazardous-cargo-imported-through-klia",
    "https://www.thestar.com.my/news/nation/2025/05/23/ktmb-postpones-signal-upgrade-works-for-asean-summit",
    "https://www.thestar.com.my/news/nation/2025/05/23/rally-in-kl-to-go-ahead-on-may-24-with-police-presence",
    "https://www.thestar.com.my/news/nation/2025/05/23/harvard-club-of-malaysia-backs-alma-maters-stand-amid-trump-move-to-block-international-students",
    "https://www.thestar.com.my/news/nation/2025/05/23/sabahs-20-oil-royalty-request-still-stands-says-former-cm-salleh",
    "https://www.thestar.com.my/news/nation/2025/05/23/johor-water-crisis-a-lesson-to-avoid-future-incidents-says-exco-rep",
    "https://www.thestar.com.my/news/nation/2025/05/23/amanah-expels-58-members-for-joining-other-political-parties",
    "https://www.thestar.com.my/aseanplus/aseanplus-news/2025/06/21/china-offers-to-be-peacemaker-in-iran-israel-war-but-is-unlikely-to-intervene",
    "https://www.thestar.com.my/lifestyle/health/2025/06/21/gen-z-stop-procrastinating-your-bedtime",
    "https://www.thestar.com.my/news/nation/2025/05/25/asean-renews-call-to-uphold-international-law-in-gaza",
    "https://www.thestar.com.my/news/nation/2025/05/25/kuwaiti-crown-prince-arrives-in-kl-for-asean-gcc-asean-gcc-china-summits",
    "https://www.thestar.com.my/news/nation/2025/05/25/malaysia-holds-bilateral-talks-with-cambodia-bahrain-at-asean-summit",
    "https://www.thestar.com.my/news/nation/2025/05/25/wei-chong-kai-wun039s-victory-reflects-bright-future-for-national-badminton-says-ahmad-zahid",
    "https://www.thestar.com.my/news/nation/2025/05/25/kelantan-cops-collect-samples-from-rubber-factory-in-acid-attack-probe",
    "https://www.thestar.com.my/news/nation/2025/05/25/manhunt-on-for-four-who-kidnapped-goldsmith-in-kelantan",
    "https://www.thestar.com.my/news/nation/2025/05/25/suspect-in-puchong-attack-detained-with-accomplices",
    "https://www.thestar.com.my/news/nation/2025/05/25/sabah-polls-grs-eyes-52-seats-21-to-national-parties-says-banah",
    "https://www.thestar.com.my/news/nation/2025/05/25/malaysia-egypt-agree-on-usim-as-gateway-for-al-azhar-medical-studies",
    "https://www.thestar.com.my/news/nation/2025/05/25/engagement-with-all-sides-in-myanmar-marks-key-step-towards-peace-says-anwar",
    "https://www.thestar.com.my/news/nation/2025/05/25/heavy-rainfall-thunderstorms-expected-in-11-states-till-6pm",
    "https://www.thestar.com.my/news/nation/2025/05/29/mustapha-to-continue-leading-sabah-pkr",
    "https://www.thestar.com.my/news/nation/2025/05/29/johor-cops-bust-job-scam-syndicate-targeting-russians",
    "https://www.thestar.com.my/news/world/2025/06/13/russia-says-it-tests-new-laser-defences-against-drones",
    "https://www.thestar.com.my/aseanplus/aseanplus-news/2025/06/13/china-approves-worlds-biggest-amphibious-plane-ag600-for-mass-production",
    "https://www.thestar.com.my/news/world/2025/06/13/from-a-russian-prison-us-schoolteacher-tells-lawyers-he-was-grabbed-by-moscow039s-soldiers",
    "https://www.thestar.com.my/news/world/2025/06/13/coordinated-protests-against-tourism-levels-planned-in-spain-portugal-and-italy",
    "https://www.thestar.com.my/news/world/2025/06/13/austrian-shooter-posted-online-just-before-school-massacre-media-say",
    "https://www.thestar.com.my/aseanplus/aseanplus-news/2025/06/13/china-us-officials-agree-to-framework-that-will-need-approvals-by-xi-trump",
    "https://www.thestar.com.my/aseanplus/aseanplus-news/2025/06/13/cambodia-orders-troops-on-039alert039-in-thai-border-spat",
    "https://www.thestar.com.my/news/world/2025/06/13/air-india-crash-survivor-says-he-escaped-through-broken-emergency-exit",
    "https://www.thestar.com.my/news/world/2025/06/13/ukrainians-face-painful-wait-to-learn-if-loved-ones-are-among-returned-bodies",
    "https://www.thestar.com.my/news/world/2025/06/13/china-builds-giant-radio-telescope-in-xinjiang",
    "https://www.thestar.com.my/news/world/2025/06/13/israel-attacks-iran039s-capital-with-explosions-booming-across-tehran",
    "https://www.thestar.com.my/news/world/2025/06/13/japan-upper-house-election-set-for-july-20-asahi-reports",
    "https://www.thestar.com.my/news/world/2025/06/13/russia039s-putin-calls-for-quick-development-of-drone-forces",
    "https://www.thestar.com.my/news/world/2025/06/13/americans-split-on-trump039s-use-of-military-in-immigration-protests...",
    "https://www.thestar.com.my/news/nation/2025/06/21/six-year-old-autistic-boy-reported-missing-near-kinabatangan-riverbank",
    "https://www.thestar.com.my/news/nation/2025/06/21/nurul-izzah-saifuddin-nasution-appointed-pkr039s-election-directors-says-fahmi",
    "https://www.thestar.com.my/news/nation/2025/06/21/ktmb-restores-services-on-kampar-slim-river-route-apologises-for-disruption",
    "https://www.thestar.com.my/news/nation/2025/06/21/melaka-education-activist-is-first-m039sian-to-co-chair-international-young-scientists-platform",
    "https://www.thestar.com.my/news/nation/2025/06/21/actress-singer-fazura-prefers-to-leave-legal-issues-to-lawyers-prefers-to-concentrate-on-new-single-composed-by-indonesian-ace-ade-govinda",
    "https://www.thestar.com.my/news/nation/2025/06/21/more-than-10000-given-community-service-orders-from-2008-to-2024-says-nancy-shukri"
]


data = []

for url in urls:
    try:
        article = Article(url)
        article.download()
        article.parse()

        data.append({
            "title": article.title,
            "text": article.text,
            "label": "REAL"
        })

    except Exception as e:
        print(f"Error with {url}: {e}")

# Save to CSV
df = pd.DataFrame(data)
df.to_csv("real_news_malaysia.csv", index=False)
print("Saved real_news_malaysia.csv")
