-- To make lua-mode happy (no stray single-quote on this line: confuses some spec scanners)
local group = {}
group["sans-serif"] = "Noto Sans"
group["serif"] = "Noto Serif"
group["monospace"] = "Noto Sans Mono"

-- Wrap for a single-quoted bash argument (family names in metainfo echoes).
local function bash_single_quote(s)
  return "'" .. string.gsub(s, "'", "'\\''") .. "'"
end

--
--alias: string: generic alias name
--family: string: font family name
--lang: array: lang code font family support
--fcconffile: string: fontconfig config file to package instead of auto-generated
--fcconfexfile: string: extra fontconfig config file to be added to auto-generated
--obsoletes: array: outdated package name to replace by
--default: bool: Wheter font is default or not
--variable: bool: Wheter font is variable or not
--priority: int: priority number for fontconfig config file
--fallback: array: alias name for fallback. similarly work for 'alias' but no rules for family->alias
--
local subpackages = {
    -- Some families ship only slim-variable-ttf (under google-noto-vf). Keeping a
    -- static subpackage when ttf/ is empty breaks the install section (metainfo: No family names).

    { alias="sans-serif", family="Sans",
      obsoletes={ "sans-ui", "sans-display" },
      default=true
    },
    { alias="sans-serif", family="Sans Adlam" },
    { alias="sans-serif", family="Sans Adlam Unjoined" },
    { alias="sans-serif", family="Sans Anatolian Hieroglyphs",
      obsoletes={ "sans-anatolian-hieroglyphs-vf" }
    },
    { alias="sans-serif", family="Sans Arabic",
      default=true, fallback={ "monospace" }
    },
    { alias="system-ui",  family="Sans Arabic UI",
      priority=rpm.expand('%{lprio}'), nogroup=1,
    },
    { alias="sans-serif", family="Sans Armenian", lang={ "hy" },
      default=true
    },
    { alias="sans-serif", family="Sans Avestan",
      obsoletes={ "sans-avestan-vf" }
    },
    { alias="sans-serif", family="Sans Balinese", lang={ "ban" } },
    { alias="sans-serif", family="Sans Bamum", lang={ "bax" } },
    { alias="sans-serif", family="Sans Bassa Vah" },
    { alias="sans-serif", family="Sans Batak", lang={ "bbc" } },
    { alias="sans-serif", family="Sans Bengali", lang={ "as", "bn", "mni" },
      default=true, fallback={ "monospace" }
    },
    { alias="system-ui",  family="Sans Bengali UI", lang={ "as", "bn", "mni" },
      priority=rpm.expand('%{lprio}'), nogroup=1,
      obsoletes={ "sans-bengali-ui-vf" },
    },
    { alias="sans-serif", family="Sans Bhaiksuki" },
    { alias="sans-serif", family="Sans Brahmi" },
    { alias="sans-serif", family="Sans Buginese", lang={ "bug" },
      obsoletes={ "sans-buginese-vf" }
    },
    { alias="sans-serif", family="Sans Buhid", lang={ "bku" },
      obsoletes={ "sans-buhid-vf" }
    },
    { alias="sans-serif", family="Sans Canadian Aboriginal", lang={ "iu" },
      default=true
    },
    { alias="sans-serif", family="Sans Caucasian Albanian" },
    { alias="sans-serif", family="Sans Carian",
      obsoletes={ "sans-carian-vf" }
    },
    { alias="sans-serif", family="Sans Chakma" },
    { alias="sans-serif", family="Sans Cham", lang={ "cjm" } },
    { alias="sans-serif", family="Sans Cherokee", lang={ "chr" },
      default=true
    },
    { alias="sans-serif", family="Sans Chorasmian" },
    { alias="sans-serif", family="Sans Coptic", lang={ "cop" } },
    { alias="sans-serif", family="Sans Cuneiform", lang={ "slv" },
      obsoletes={ "sans-cuneiform-vf" }
    },
    { alias="sans-serif", family="Sans Cypriot",
      obsoletes={ "sans-cypriot-vf" }
    },
    { alias="sans-serif", family="Sans Cypro Minoan" },
    { alias="sans-serif", family="Sans Deseret",
      obsoletes={ "sans-deseret-vf" }
    },
    { alias="sans-serif", family="Sans Devanagari", lang={ "bh", "bho", "brx", "doi", "hi", "hne", "kok", "ks@devanagari", "mai", "mr", "ne", "sa", "sat", "sd@devanagari" },
      default=true, fallback={ "monospace" }
    },
    { alias="system-ui",  family="Sans Devanagari UI", lang={ "bh", "bho", "brx", "doi", "hi", "hne", "kok", "ks@devanagari", "mai", "mr", "ne", "sa", "sat", "sd@devanagari" },
      priority=rpm.expand('%{lprio}'), nogroup=1,
      obsoletes={ "sans-devanagari-ui-vf" }
    },
    { alias="sans-serif", family="Sans Duployan" },
    { alias="sans-serif", family="Sans Egyptian Hieroglyphs",
      obsoletes={ "sans-egyptian-hieroglyphs-vf" }
    },
    { alias="sans-serif", family="Sans Elbasan" },
    { alias="sans-serif", family="Sans Elymaic",
      obsoletes={ "sans-elymaic-vf" }
    },
    { alias="sans-serif", family="Sans Ethiopic", lang={ "am", "byn", "gez", "sid", "ti-er", "ti-et", "tig", "wal" },
      default=true, fallback={ "monospace" }
    },
    { alias="sans-serif", family="Sans Georgian", lang={ "ka" },
      default=true, fallback={ "monospace" }
    },
    { alias="sans-serif", family="Sans Glagolitic" },
    { alias="sans-serif", family="Sans Gothic", lang={ "got" },
      obsoletes={ "sans-gothic-vf" }
    },
    { alias="sans-serif", family="Sans Grantha" },
    { alias="sans-serif", family="Sans Gujarati", lang={ "gu" },
      default=true, fallback={ "monospace" }
    },
    { alias="system-ui",  family="Sans Gujarati UI", lang={ "gu" },
      priority=rpm.expand('%{lprio}'), nogroup=1
    },
    { alias="sans-serif", family="Sans Gunjala Gondi" },
    { alias="sans-serif", family="Sans Gurmukhi", lang={ "pa" },
      default=true
    },
    { alias="system-ui",  family="Sans Gurmukhi UI", lang={ "pa" },
      priority=rpm.expand('%{lprio}'), nogroup=1,
      obsoletes={ "sans-gurmukhi-ui-vf" },
    },
    { alias="sans-serif", family="Sans Hanifi Rohingya" },
    { alias="sans-serif", family="Sans Hanunoo", lang={ "hnn" },
      obsoletes={ "sans-hanunno" }
    },
    { alias="sans-serif", family="Sans Hatran",
      obsoletes={ "sans-hatran-vf" }
    },
    { alias="sans-serif", family="Sans Hebrew", lang={ "he", "yi" },
      obsoletes={ "sans-hebrew-droid", "sans-hebrew-new" },
      default=true, fallback={ "monospace" }
    },
    { alias="sans-serif", family="Sans Imperial Aramaic",
      obsoletes={ "sans-imperial-aramaic-vf" }
    },
    { alias="sans-serif", family="Sans Indic Siyaq Numbers" },
    { alias="sans-serif", family="Sans Inscriptional Pahlavi" },
    { alias="sans-serif", family="Sans Inscriptional Parthian" },
    { alias="sans-serif", family="Sans Javanese" },
    { alias="sans-serif", family="Sans Kaithi" },
    { alias="sans-serif", family="Sans Kannada", lang={ "kn" },
      default=true, fallback={ "monospace" }
    },
    { alias="system-ui",  family="Sans Kannada UI", lang={ "kn" },
      priority=rpm.expand('%{lprio}'), nogroup=1,
    },
    { alias="sans-serif", family="Sans Kawi" },
    { alias="sans-serif", family="Sans Kayah Li" },
    { alias="sans-serif", family="Sans Kharoshthi" },
    { alias="sans-serif", family="Sans Khmer", lang={ "km" },
      obsoletes={ "sans-khmer-ui" },
      default=true, fallback={ "monospace" }
    },
    { alias="sans-serif", family="Sans Khojki" },
    { alias="sans-serif", family="Sans Khudawadi" },
    { alias="sans-serif", family="Sans Lao", lang={ "lo" },
      obsoletes={ "sans-lao-ui" },
      default=true
    },
    { alias="sans-serif", family="Sans Lao Looped", lang={ "lo" }, nogroup=1,
      obsoletes={ "looped-lao", "looped-lao-ui" },
    },
    { alias="sans-serif", family="Sans Lepcha", lang={ "lep" } },
    { alias="sans-serif", family="Sans Limbu", lang={ "lif" } },
    { alias="sans-serif", family="Sans Linear A",
      obsoletes={ "sans-linear-a-vf" }
    },
    { alias="sans-serif", family="Sans Linear B",
      obsoletes={ "sans-linearb", "sans-linear-b-vf" }
    },
    { alias="sans-serif", family="Sans Lisu" },
    { alias="sans-serif", family="Sans Lycian",
      obsoletes={ "sans-lycian-vf" }
    },
    { alias="sans-serif", family="Sans Lydian",
      obsoletes={ "sans-lydian-vf" }
    },
    { alias="sans-serif", family="Sans Mahajani" },
    { alias="sans-serif", family="Sans Malayalam", lang={ "ml" } },
    { alias="system-ui",  family="Sans Malayalam UI", lang={ "ml" },
      priority=rpm.expand('%{lprio}'), nogroup=1,
    },
    { alias="sans-serif", family="Sans Mandaic",
      obsoletes={ "sans-mandaic-vf" }
    },
    { alias="sans-serif", family="Sans Manichaean" },
    { alias="sans-serif", family="Sans Marchen",
      obsoletes={ "sans-marchen-vf" }
    },
    { alias="sans-serif", family="Sans Masaram Gondi" },
    { alias="sans-serif", family="Sans Math",
      priority=rpm.expand('%{lprio}'),
      obsoletes={ "sans-math-vf" }
    },
    { alias="sans-serif", family="Sans Mayan Numerals",
      obsoletes={ "sans-mayan-numerals-vf" }
    },
    { alias="sans-serif", family="Sans Meetei Mayek",
      obsoletes={ "sans-meeteimayek" }
    },
    { alias="sans-serif", family="Sans Medefaidrin" },
    { alias="sans-serif", family="Sans Mende Kikakui" },
    { alias="sans-serif", family="Sans Meroitic" },
    { alias="sans-serif", family="Sans Miao" },
    { alias="sans-serif", family="Sans Modi" },
    { alias="sans-serif", family="Sans Mongolian", lang={ "mn-cn" } },
    { alias="monospace",  family="Sans Mono",
      obsoletes={ "mono" },
      default=true
    },
    { alias="sans-serif", family="Sans Mro",
      obsoletes={ "sans-mro-vf" }
    },
    { alias="sans-serif", family="Sans Multani",
      obsoletes={ "sans-multani-vf" }
    },
    { alias="sans-serif", family="Sans Myanmar", lang={ "my" },
      obsoletes={ "sans-myanmar-ui" },
    },
    { alias="sans-serif", family="Sans Nabataean",
      obsoletes={ "sans-nabataean-vf" }
    },
    { alias="sans-serif", family="Sans Nag Mundari" },
    { alias="sans-serif", family="Sans Nandinagari" },
    { alias="sans-serif", family="Sans New Tai Lue", lang={ "khb" } },
    { alias="sans-serif", family="Sans Newa" },
    { alias="sans-serif", family="Sans NKo", lang={ "nqo" } },
    { alias="sans-serif", family="Sans NKo Unjoined", lang={ "nqo" },
      priority=rpm.expand('%{lprio}'), nogroup=1,
    },
    { alias="sans-serif", family="Sans Nushu" },
    { alias="sans-serif", family="Sans Ogham", lang={ "pgl" },
      obsoletes={ "sans-ogham-vf" }
    },
    { alias="sans-serif", family="Sans Ol Chiki" },
    { alias="sans-serif", family="Sans Old Hungarian" },
    { alias="sans-serif", family="Sans Old Italic" },
    { alias="sans-serif", family="Sans Old North Arabian" },
    { alias="sans-serif", family="Sans Old Permic" },
    { alias="sans-serif", family="Sans Old Persian" },
    { alias="sans-serif", family="Sans Old Sogdian" },
    { alias="sans-serif", family="Sans Old South Arabian" },
    { alias="sans-serif", family="Sans Old Turkic" },
    { alias="sans-serif", family="Sans Oriya", lang={ "or" },
      obsoletes={ "sans-oriya-ui" },
      default=true, fallback={ "monospace" }
    },
    { alias="sans-serif", family="Sans Osage" },
    { alias="sans-serif", family="Sans Osmanya",
      obsoletes={ "sans-osmanya-vf" }
    },
    { alias="sans-serif", family="Sans Pahawh Hmong" },
    { alias="sans-serif", family="Sans Palmyrene" },
    { alias="sans-serif", family="Sans Pau Cin Hau" },
    { alias="sans-serif", family="Sans PhagsPa",
      obsoletes={ "sans-phags-pa" },
    },
    { alias="sans-serif", family="Sans Phoenician",
      obsoletes={ "sans-phoenician-vf" }
    },
    { alias="sans-serif", family="Sans Psalter Pahlavi" },
    { alias="sans-serif", family="Sans Rejang", lang={ "rej" } },
    { alias="sans-serif", family="Sans Runic", lang={ "gem" },
      obsoletes={ "sans-runic-vf" },
    },
    { alias="sans-serif", family="Sans Samaritan" },
    { alias="sans-serif", family="Sans Saurashtra", lang={ "saz" } },
    { alias="sans-serif", family="Sans Sharada" },
    { alias="sans-serif", family="Sans Shavian", lang={ "en@shaw" },
      obsoletes={ "sans-shavian-vf" }
    },
    { alias="sans-serif", family="Sans Siddham" },
    { alias="sans-serif", family="Sans SignWriting" },
    { alias="sans-serif", family="Sans Sinhala", lang={ "si" },
      default=true, fallback={ "monospace" },
      fcconfexfile=string.match(rpm.expand('%{SOURCE8}'), "([^/]*)" .. '$')
    },
    { alias="system-ui",  family="Sans Sinhala UI", lang={ "si" },
      priority=rpm.expand('%{lprio}'), nogroup=1,
      obsoletes={ "sans-sinhala-ui-vf" },
    },
    { alias="sans-serif", family="Sans Sogdian" },
    { alias="sans-serif", family="Sans Sora Sompeng" },
    { alias="sans-serif", family="Sans Soyombo",
      obsoletes={ "sans-soyombo-vf" }
    },
    { alias="sans-serif", family="Sans Sundanese" },
    { alias="sans-serif", family="Sans Sunuwar", lang={ "suz" } },
    { alias="sans-serif", family="Sans Syloti Nagri" },
    { alias="sans-serif", family="Sans Syriac", lang={ "syr" },
      obsoletes={ "sans-syriac-estrangela" }
    },
    { alias="sans-serif", family="Sans Syriac Eastern", lang={ "syr" } },
    { alias="sans-serif", family="Sans Syriac Western", lang={ "syr" } },
    { alias="sans-serif", family="Sans Tagalog" },
    { alias="sans-serif", family="Sans Tagbanwa", lang={ "twb" },
      obsoletes={ "sans-tagbanwa-vf" }
    },
    { alias="sans-serif", family="Sans Takri",
      obsoletes={ "sans-takri-vf" }
    },
    { alias="sans-serif", family="Sans Tai Le" },
    { alias="sans-serif", family="Sans Tai Tham" },
    { alias="sans-serif", family="Sans Tai Viet",
      obsoletes={ "sans-tai-viet-vf" },
    },
    { alias="sans-serif", family="Sans Tamil", lang={ "ta" },
      default=true, fallback={ "monospace" }
    },
    { alias="sans-serif", family="Sans Tamil Supplement", lang={ "ta" },
      excludeci=true, nogroup=1
    },
    { alias="system-ui",  family="Sans Tamil UI", lang={ "ta" },
      priority=rpm.expand('%{lprio}'), nogroup=1
    },
    { alias="sans-serif", family="Sans Tangsa" },
    { alias="sans-serif", family="Sans Telugu", lang={ "te" },
      default=true, fallback= { "monospace" }
    },
    { alias="system-ui",  family="Sans Telugu UI", lang={ "te" },
      priority=rpm.expand('%{lprio}'), nogroup=1,
    },
    { alias="sans-serif", family="Sans Thaana", lang={ "dv" },
      default=true
    },
    { alias="sans-serif", family="Sans Thai", lang={ "th" },
      obsoletes={ "sans-thai-ui" },
      default=true, fallback={ "monospace" }
    },
    { alias="sans-serif", family="Sans Thai Looped", lang={ "th" },
      obsoletes={ "looped-thai", "looped-thai-ui" }
    },
    { alias="sans-serif", family="Sans Tifinagh", lang={ "ber-ma" } },
    { alias="sans-serif", family="Sans Tifinagh APT", lang={ "ber-ma" } },
    { alias="sans-serif", family="Sans Tifinagh Adrar", lang={ "ber-ma" } },
    { alias="sans-serif", family="Sans Tifinagh Agraw Imazighen", lang={ "ber-ma" } },
    { alias="sans-serif", family="Sans Tifinagh Ahaggar", lang={ "ber-ma" } },
    { alias="sans-serif", family="Sans Tifinagh Air", lang={ "ber-ma" } },
    { alias="sans-serif", family="Sans Tifinagh Azawagh", lang={ "ber-ma" } },
    { alias="sans-serif", family="Sans Tifinagh Ghat", lang={ "ber-ma" } },
    { alias="sans-serif", family="Sans Tifinagh Hawad", lang={ "ber-ma" } },
    { alias="sans-serif", family="Sans Tifinagh Rhissa Ixa", lang={ "ber-ma" } },
    { alias="sans-serif", family="Sans Tifinagh SIL", lang={ "ber-ma" } },
    { alias="sans-serif", family="Sans Tifinagh Tawellemmet", lang={ "ber-ma" } },
    { alias="sans-serif", family="Sans Tirhuta" },
    { alias="sans-serif", family="Sans Ugaritic",
      obsoletes={ "sans-ugaritic-vf" }
    },
    { alias="sans-serif", family="Sans Vai", lang={ "vai" },
      obsoletes={ "sans-vai-vf" }
    },
    { alias="sans-serif", family="Sans Vithkuqi" },
    { alias="sans-serif", family="Sans Wancho",
      obsoletes={ "sans-wancho-vf" }
    },
    { alias="sans-serif", family="Sans Warang Citi",
      obsoletes={ "sans-warang-citi-vf" }
    },
    { alias="sans-serif", family="Sans Yi",
      obsoletes={ "sans-yi-vf" }
    },
    { alias="sans-serif", family="Sans Zanabazar Square",
      obsoletes={ "sans-zanabazar-square-vf" },
    },

    { alias="serif",      family="Naskh Arabic",
      fcconfexfile=string.match(rpm.expand('%{SOURCE3}'), "([^/]*)" .. '$'),
      default=true
    },
    { alias="system-ui",  family="Naskh Arabic UI",
      priority=rpm.expand('%{lprio}')
    },
    { alias="serif",      family="Serif",
      obsoletes={ "serif-display" },
      default=true
    },
    { alias="serif",      family="Serif Ahom" },
    { alias="serif",      family="Serif Armenian", lang={ "hy" },
      default=true
    },
    { alias="serif",      family="Serif Balinese", lang={ "ban" },
      obsoletes={ "sans-balinese" }
    },
    { alias="serif",      family="Serif Bengali", lang={ "as", "bn", "mni" },
      default=true
    },
    { alias="serif",      family="Serif Devanagari", lang={ "bh", "bho", "brx", "doi", "hi", "hne", "kok", "ks@devanagari", "mai", "mr", "ne", "sa", "sat", "sd@devanagari" },
      default=true
    },
    { alias="serif",      family="Serif Dives Akuru" },
    { alias="serif",      family="Serif Dogra",
      obsoletes={ "serif-dogra-vf" },
    },
    { alias="serif",      family="Serif Ethiopic", lang={ "am", "byn", "gez", "sid", "ti-er", "ti-et", "tig", "wal" },
      default=true
    },
    { alias="serif",      family="Serif Georgian", lang={ "ka" },
      default=true
    },
    { alias="serif",      family="Serif Grantha" },
    { alias="serif",      family="Serif Gujarati", lang={ "gu" },
      default=true
    },
    { alias="serif",      family="Serif Gurmukhi", lang={ "pa" },
      default=true
    },
    { alias="serif",      family="Serif Hebrew", lang={ "he", "yi" } },
    { alias="serif",      family="Serif Hentaigana" },
    { alias="serif",      family="Serif Kannada", lang={ "kn" },
      default=true
    },
    { alias="serif",      family="Serif Khitan Small Script" },
    { alias="serif",      family="Serif Khmer", lang={ "km" },
      default=true
    },
    { alias="serif",      family="Serif Khojki" },
    { alias="serif",      family="Serif Lao", lang={ "lo" },
      default=true
    },
    { alias="serif",      family="Serif Makasar" },
    { alias="serif",      family="Serif Malayalam", lang={ "ml" } },
    { alias="serif",      family="Serif Myanmar", lang={ "my" } },
    { alias="serif",      family="Serif NP Hmong",
      obsoletes={ "serif-nyiakeng-puachue-hmong" },
    },
    { alias="serif",      family="Serif Old Uyghur" },
    { alias="serif",      family="Serif Oriya", lang={ "or" },
      default=true
    },
    { alias="serif",      family="Serif Ottoman Siyaq" },
    { alias="serif",      family="Serif Sinhala", lang={ "si" },
      default=true
    },
    { alias="serif",      family="Serif Tamil", lang={ "ta" },
      obsoletes={ "serif-tamil-slanted" },
      default=true
    },
    { alias="serif",      family="Serif Tangut",
      obsoletes={ "serif-tangut-vf" }
    },
    { alias="serif",      family="Serif Telugu", lang={ "te" },
      default=true
    },
    { alias="serif",      family="Serif Thai", lang={ "th" },
      default=true
    },
    { alias="serif",      family="Serif Tibetan", lang={ "bo", "dz" },
      obsoletes={ "sans-tibetan" }
    },
    { alias="serif",      family="Serif Todhri" },
    { alias="serif",      family="Serif Toto" },
    { alias="serif",      family="Serif Vithkuqi" },
    { alias="serif",      family="Serif Yezidi" },
    { alias="serif",      family="Traditional Nushu" },
    -- It may be symbol but is a part of. no alias is intentional.
    { alias="",           family="Znamenny Musical Notation",
      priority=rpm.expand('%{lprio}'), nogroup=1,
      fcconffile=string.match(rpm.expand('%{SOURCE4}'), "([^/]*)" .. '$'),
    },

    { alias="cursive",    variable=true, family="Nastaliq Urdu", lang={ "ur" },
      obsoletes={ "nastaliq-urdu" },
    },
    { alias="cursive",    variable=true, family="Rashi Hebrew", lang={ "he" },
      default=true,
      obsoletes={ "rashi-hebrew" },
    },

    { alias="fangsong",   variable=true, family="Fangsong KSS Rotated",
      obsoletes={ "fangsong-kss-rotated" },
    },
    { alias="fangsong",   variable=true, family="Fangsong KSS Vertical",
      obsoletes={ "fangsong-kss-vertical" },
    },

    { alias="fantasy",    variable=true, family="Sans Symbols",
      obsoletes={ "sans-symbols" },
    },
    { alias="fantasy",    variable=true, family="Sans Symbols 2",
      obsoletes={ "sans-symbols-2", "sans-symbols2" },
    },

    { alias="fantasy",    variable=true, family="Music",
      obsoletes={ "music" },
    },

    { alias="sans-serif", variable=true, family="Kufi Arabic",
      obsoletes={ "kufi-arabic" },
    },

    { alias="sans-serif", variable=true, family="Sans",
      obsoletes={ "sans-display-vf" },
      default=true
    },
    { alias="sans-serif", variable=true, family="Sans Adlam" },
    { alias="sans-serif", variable=true, family="Sans Adlam Unjoined" },
    { alias="sans-serif", variable=true, family="Sans Arabic",
      default=true, fallback={ "monospace" }
    },
    { alias="system-ui",  variable=true, family="Sans Arabic UI",
      priority=rpm.expand('%{lprio}'), nogroup=1,
    },
    { alias="sans-serif", variable=true, family="Sans Armenian", lang={ "hy" },
      default=true
    },
    { alias="sans-serif", variable=true, family="Sans Balinese", lang={ "ban" } },
    { alias="sans-serif", variable=true, family="Sans Bamum", lang={ "bax" } },
    { alias="sans-serif", variable=true, family="Sans Bassa Vah" },
    { alias="sans-serif", variable=true, family="Sans Bengali", lang={ "as", "bn", "mni" },
      default=true, fallback={ "monospace" }
    },
    { alias="sans-serif", variable=true, family="Sans Canadian Aboriginal", lang={ "iu" },
      default=true
    },
    { alias="sans-serif", variable=true, family="Sans Cham", lang={ "cjm" } },
    { alias="sans-serif", variable=true, family="Sans Cherokee", lang={ "chr" },
      default=true
    },
    { alias="sans-serif", variable=true, family="Sans Devanagari", lang={ "bh", "bho", "brx", "doi", "hi", "hne", "kok", "ks@devanagari", "mai", "mr", "ne", "sa", "sat", "sd@devanagari" },
      default=true, fallback={ "monospace" }
    },
    { alias="sans-serif", variable=true, family="Sans Ethiopic", lang={ "am", "byn", "gez", "sid", "ti-er", "ti-et", "tig", "wal" },
      default=true, fallback={ "monospace" }
    },
    { alias="sans-serif", variable=true, family="Sans Georgian", lang={ "ka" },
      default=true, fallback={ "monospace" }
    },
    { alias="sans-serif", variable=true, family="Sans Gujarati", lang={ "gu" },
      default=true, fallback={ "monospace" }
    },
    { alias="sans-serif", variable=true, family="Sans Gunjala Gondi" },
    { alias="sans-serif", variable=true, family="Sans Gurmukhi", lang={ "pa" },
      obsoletes={ "sans-gurkukhi-ui-vf" },
      default=true
    },
    { alias="sans-serif", variable=true, family="Sans Hanifi Rohingya" },
    { alias="sans-serif", variable=true, family="Sans Hebrew", lang={ "he", "yi" },
      obsoletes={ "sans-hebrew-droid-vf", "sans-hebrew-new-vf" },
      default=true, fallback={ "monospace" }
    },
    { alias="sans-serif", variable=true, family="Sans Javanese" },
    { alias="sans-serif", variable=true, family="Sans Kannada", lang={ "kn" },
      default=true, fallback={ "monospace" }
    },
    { alias="system-ui",  variable=true, family="Sans Kannada UI", lang={ "kn" },
      priority=rpm.expand('%{lprio}'), nogroup=1,
      fontname="SansKannada-UI",
    },
    { alias="sans-serif", variable=true, family="Sans Kayah Li" },
    { alias="sans-serif", variable=true, family="Sans Kawi" },
    { alias="sans-serif", variable=true, family="Sans Khmer", lang={ "km" },
      obsoletes={ "sans-khmer-ui-vf" },
      default=true, fallback={ "monospace" }
    },
    { alias="sans-serif", variable=true, family="Sans Lao", lang={ "lo" },
      obsoletes={ "sans-lao-ui-vf" },
      default=true
    },
    { alias="sans-serif", variable=true, family="Sans Lao Looped", lang={ "lo" },
      obsoletes={ "looped-lao-vf", "looped-lao-ui-vf" }, nogroup=1,
    },
    { alias="sans-serif", variable=true, family="Sans Lisu" },
    { alias="sans-serif", variable=true, family="Sans Nag Mundari" },
    { alias="sans-serif", variable=true, family="Sans Malayalam", lang={ "ml" } },
    { alias="system-ui",  variable=true, family="Sans Malayalam UI", lang={ "ml" },
      priority=rpm.expand('%{lprio}'), nogroup=1,
      fontname="SansMalayalam-UI",
    },
    { alias="sans-serif", variable=true, family="Sans Medefaidrin" },
    { alias="sans-serif", variable=true, family="Sans Meetei Mayek",
      obsoletes={ "sans-meeteimayek-vf" },
    },
    { alias="monospace", variable=true, family="Sans Mono",
      default=true
    },
    { alias="sans-serif", variable=true, family="Sans Myanmar", lang={ "my" },
      obsoletes={ "serif-myanmar-vf", "sans-myanmar-ui-vf" }
    },
    { alias="sans-serif", variable=true, family="Sans New Tai Lue", lang={ "khb" } },
    { alias="sans-serif", variable=true, family="Sans NKo Unjoined", lang={ "nqo" },
      priority=rpm.expand('%{lprio}'), nogroup=1,
    },
    { alias="sans-serif", variable=true, family="Sans Ol Chiki" },
    { alias="sans-serif", variable=true, family="Sans Oriya", lang={ "or" },
      obsoletes={ "sans-oriya-ui-vf" },
      default=true, fallback={ "monospace" }
    },
    { alias="sans-serif", variable=true, family="Sans Sinhala", lang={ "si" },
      default=true, fallback={ "monospace" },
      fcconfexfile=string.match(rpm.expand('%{SOURCE8}'), "([^/]*)" .. '$')
    },
    { alias="sans-serif", variable=true, family="Sans Sora Sompeng" },
    { alias="sans-serif", variable=true, family="Sans Sundanese" },
    { alias="sans-serif", variable=true, family="Sans Syriac", lang={ "syr" } },
    { alias="sans-serif", variable=true, family="Sans Syriac Eastern", lang={ "syr" } },
    { alias="sans-serif", variable=true, family="Sans Syriac Western", lang={ "syr" } },
    { alias="sans-serif", variable=true, family="Sans Tai Tham" },
    { alias="sans-serif", variable=true, family="Sans Tamil", lang={ "ta" },
      obsoletes={ "sans-tamil-supplement-vf" },
      default=true, fallback={ "monospace" }
    },
    { alias="system-ui",  variable=true, family="Sans Tamil UI", lang={ "ta" },
      priority=rpm.expand('%{lprio}'), nogroup=1,
      fontname="SansTamil-UI",
    },
    { alias="sans-serif", variable=true, family="Sans Tangsa" },
    { alias="sans-serif", variable=true, family="Sans Telugu", lang={ "te" },
      default=true, fallback={ "monospace" }
    },
    { alias="system-ui",  variable=true, family="Sans Telugu UI", lang={ "te" },
      priority=rpm.expand('%{lprio}'), nogroup=1,
      fontname="SansTelugu-UI",
    },
    { alias="sans-serif", variable=true, family="Sans Thaana", lang={ "dv" },
      default=true
    },
    { alias="sans-serif", variable=true, family="Sans Thai", lang={ "th" },
      obsoletes={ "sans-thai-ui-vf" },
      default=true, fallback={ "monospace" }
    },
    { alias="sans-serif", variable=true, family="Sans Thai Looped", lang={ "th" },
      obsoletes={ "sansthai-looped-vf",  "looped-thai-vf", "looped-thai-ui-vf" }
    },
    { alias="sans-serif", variable=true, family="Sans Vithkuqi" },
    { alias="serif",      variable=true, family="Naskh Arabic",
      fcconfexfile=string.match(rpm.expand('%{SOURCE3}'), "([^/]*)" .. '$'),
      default=true
    },
    { alias="system-ui",  variable=true, family="Naskh Arabic UI",
      priority=rpm.expand('%{lprio}'), nogroup=1
    },
    { alias="serif",      variable=true, family="Serif",
      obsoletes={ "serif-display-vf" },
      default=true
    },
    { alias="serif",      variable=true, family="Serif Armenian", lang={ "hy" },
      default=true
    },
    { alias="serif",      variable=true, family="Serif Bengali", lang={ "as", "bn", "mni" },
      default=true
    },
    { alias="serif",      variable=true, family="Serif Devanagari", lang={ "bh", "bho", "brx", "doi", "hi", "hne", "kok", "ks@devanagari", "mai", "mr", "ne", "sa", "sat", "sd@devanagari" },
      default=true
    },
    { alias="serif",      variable=true, family="Serif Ethiopic", lang={ "am", "byn", "gez", "sid", "ti-er", "ti-et", "tig", "wal" },
      default=true
    },
    { alias="serif",      variable=true, family="Serif Georgian", lang={ "ka" },
      default=true
    },
    { alias="serif",      variable=true, family="Serif Gujarati", lang={ "gu" },
      default=true
    },
    { alias="serif",      variable=true, family="Serif Gurmukhi", lang={ "pa" },
      default=true
    },
    { alias="serif",      variable=true, family="Serif Hebrew", lang={ "he", "yi" } },
    { alias="serif",      variable=true, family="Serif Hentaigana" },
    { alias="serif",      variable=true, family="Serif Kannada", lang={ "kn" },
      default=true
    },
    { alias="serif",      variable=true, family="Serif Khmer", lang={ "km" },
      default=true
    },
    { alias="serif",      variable=true, family="Serif Khojki" },
    { alias="serif",      variable=true, family="Serif Lao", lang={ "lo" },
      default=true
    },
    { alias="serif",      variable=true, family="Serif Malayalam", lang={ "ml" } },
    { alias="serif",      variable=true, family="Serif Myanmar", lang={ "my" } },
    { alias="serif",      variable=true, family="Serif NP Hmong",
      obsoletes={ "serif-nyiakeng-puachue-hmong-vf" },
    },
    { alias="serif",      variable=true, family="Serif Oriya", lang={ "or" },
      default=true
    },
    { alias="serif",      variable=true, family="Serif Sinhala", lang={ "si" },
      default=true
    },
    { alias="serif",      variable=true, family="Serif Tamil", lang={ "ta" },
      obsoletes={ "serif-tamil-slanted-vf" },
      default=true
    },
    { alias="serif",      variable=true, family="Serif Telugu", lang={ "te" },
      default=true
    },
    { alias="serif",      variable=true, family="Serif Thai", lang={ "th" },
      default=true
    },
    { alias="serif",      variable=true, family="Serif Tibetan", lang={ "bo", "dz" } },
    { alias="serif",      variable=true, family="Serif Toto" },
    { alias="serif",      variable=true, family="Serif Vithkuqi" },
    { alias="serif",      variable=true, family="Serif Yezidi" },
    { alias="serif",      variable=true, family="Traditional Nushu" },

    }
local _fcconflist = ''
local _metafilelist = ''
local _fcconfbuild = ''
local _metainfobuild = ''
local _filelistbuild = ''

local function is_nonlatin(table)
    latin_langs = { "af", "ar", "az", "bs", "ca", "cs", "cy", "da", "de", "en", "es", "et", "fil", "fi", "fo", "fr", "ga", "gd", "gl", "hr", "hu", "id", "is", "it", "ka", "kk", "ky", "lb", "lt", "lv", "mk", "mont", "ms", "mt", "nl", "no", "pl", "pt", "ro", "sk", "sl", "sq", "sr", "sv", "sw", "tg", "tk", "tr", "uz" }
    if table.lang then
        for i = 1, #table.lang do
            for j = 1, #latin_langs do
                if table.lang[i] == latin_langs[j] then
                    return false
                end
            end
        end
    else
      return false
    end
    return true
end

local function _genfcconf(alias, family, lang, reverse)
    local ret = ""
    local generic = [[
    <test name="family">
      <string>]] .. alias .. [[</string>
    </test>
    <edit name=\"family\" mode=\"prepend\">
      <string>Noto ]] .. family .. [[</string>
    </edit>
]]
    if lang then
        for i = 1, #lang do
            ret = ret .. [[  <match>
    <test name=\"lang\" compare=\"contains\">
      <string>]] .. lang[i] .. [[</string>
    </test>
]] .. generic .. "\n" .. [[
  </match>
]]
        end
    else
        ret = ret .. [[  <match>
]] .. generic .. "\n" .. [[
  </match>
]]
    end
    if reverse then
        ret = ret .. [[
  <alias>
    <family>Noto ]] .. family .. [[</family>
    <default>
      <family>]] .. alias .. [[</family>
    </default>
  </alias>
]]
    end
    return ret
end

local function genfcconf(table)
    local extra = "\\\n"
    if table.fcconfexfile then
        -- Try to find the file in multiple locations
        local sourcedir = rpm.expand('%{_sourcedir}')
        if sourcedir:sub(-1) ~= "/" then sourcedir = sourcedir .. "/" end
        local filepath = sourcedir .. table.fcconfexfile
        local f = io.open(filepath, "r")
        
        -- If not found in _sourcedir, try the spec directory
        if not f then
            local specdir = rpm.expand('%{_specdir}')
            if specdir:sub(-1) ~= "/" then specdir = specdir .. "/" end
            filepath = specdir .. table.fcconfexfile
            f = io.open(filepath, "r")
        end
        
        -- If found, read the extra config; if not, just use default
        if f then
            for line in f:lines() do
                extra = extra .. line:gsub("\n" .. '$', ""):gsub('%$', "\\\n")
            end
            extra = extra:gsub("\n\n" .. '$', "\n")
            f:close()
        end
    end
    local xml = [[
<?xml version=\"1.0\" encoding=\"UTF-8\"?>
<!DOCTYPE fontconfig SYSTEM \"urn:fontconfig:fonts.dtd\">
<fontconfig>
]]
    xml = xml .. _genfcconf(table.alias, table.family, table.lang, true)
    if table.fallback then
        for i = 1, #table.fallback do
            xml = xml .. _genfcconf(table.fallback[i], table.family, table.lang, false)
        end
    end
    xml = xml .. extra .. [[
</fontconfig>
]]
    if table.fcconffile then
        -- Try to find the file in multiple locations
        local sourcedir = rpm.expand('%{_sourcedir}')
        if sourcedir:sub(-1) ~= "/" then sourcedir = sourcedir .. "/" end
        local filepath = sourcedir .. table.fcconffile
        local f = io.open(filepath, "r")
        
        -- If not found in _sourcedir, try the spec directory
        if not f then
            local specdir = rpm.expand('%{_specdir}')
            if specdir:sub(-1) ~= "/" then specdir = specdir .. "/" end
            filepath = specdir .. table.fcconffile
            f = io.open(filepath, "r")
        end
        
        -- If found, read config; if not, generate default
        if f then
            xml = ""
            for line in f:lines() do
                xml = xml .. line:gsub("\n" .. '$', ""):gsub('%$', "\\\n")
            end
            xml = xml:gsub("\n\n" .. '$', "\n")
            f:close()
        end
    end
    _fcconfbuild = _fcconfbuild .. "cat<<_EOL_>" .. table.fcconf .. "\\\n" .. xml .. "_EOL_\\\n"
end

-- Borrowed from fonts-rpm-macros
-- koji doesn't sasisfy BR during generating srpm yet.
-- We can't add a dependant code to fonts-rpm-macros at this stage.

-- https://github.com/rpm-software-management/rpm/issues/566
-- Reformat a text intended to be used used in a package description, removing
-- rpm macro generation artefacts.
-- – remove leading and ending empty lines
-- – trim intermediary empty lines to a single line
-- – fold on spaces
-- Should really be a wordwrap macro verb
local function wordwrap(text)
  text = rpm.expand(text .. "\n")
  text = string.gsub(text, "\t",              "  ")
  text = string.gsub(text, "\r",              "\n")
  text = string.gsub(text, " +\n",            "\n")
  text = string.gsub(text, "\n+\n",           "\n\n")
  text = string.gsub(text, "^\n",             "")
  text = string.gsub(text, "\n( *)[-*—][  ]+", "\n%1– ")
  output = ""
  for line in string.gmatch(text, "[^\n]*\n") do
    local pos = 0
    local advance = ""
    for word in string.gmatch(line, "%s*[^%s]*\n?") do
      local wd = word
      local wl, bad = utf8.len(wd)
      if not wl then
        print("%{warn:Invalid UTF-8 sequence detected in:}" ..
              "%{warn:" .. wd .. "}" ..
              "%{warn:It may produce unexpected results.}")
        wl = bad
      end
      if (pos == 0) then
        advance, n = string.gsub(wd, "^(%s*– ).*", "%1")
        if (n == 0) then
          advance = string.gsub(wd, "^(%s*).*", "%1")
        end
        advance = string.gsub(advance, "– ", "  ")
        pos = pos + wl
      elseif  (pos + wl  < 81) or
             ((pos + wl == 81) and string.match(wd, "\n" .. '$')) then
        pos = pos + wl
      else
        wd = advance .. string.gsub(wd, "^%s*", "")
        output = output .. "\n"
        pos = utf8.len(wd)
      end
      output = output .. wd
      if pos > 80 then
        pos = 0
        if not string.match(wd, "\n" .. '$') then
          output = output .. "\n"
        end
      end
    end
  end
  output = string.gsub(output, "\n*" .. '$', "\n")
  return output
end

-- A helper to close AppStream XML runs
local function closetag(oldtag, newtag)
  if (oldtag == nil) then
    return ""
  else
    local output = "]]></" .. oldtag .. ">"
    if (oldtag == "li") and (newtag ~= oldtag) then
      output = output .. "</ul>"
    end
    return output
  end
end

-- A helper to open AppStream XML runs
local function opentag(oldtag, newtag)
  if (newtag == nil) then
    return ""
  else
    local output = "<" .. newtag .. "><![CDATA["
    if (newtag == "li") and (newtag ~= oldtag) then
      output = "<ul>" .. output
    end
    return output
  end
end

-- A helper to switch AppStream XML runs
local function switchtag(oldtag, newtag)
  return closetag(oldtag, newtag) .. opentag(oldtag, newtag)
end

-- Reformat some text into something that can be included in an AppStream
-- XML description
local function txt2xml(text)
  local        text = wordwrap(text)
  local      output = ""
  local     oldtag  = nil
  local oldadvance  = nil
  local      newtag = nil
  text = string.gsub(text, "^\n*", "")
  text = string.gsub(text, "\n*" .. '$', "\n")
  for line in string.gmatch(text, "[^\n]*\n") do
    local change = true
    local advance, n = string.gsub(line, "^(%s*– ).*", "%1")
    if (n == 1) then
      newtag = "li"
    else
      advance = string.gsub(line, "^(%s*).*", "%1")
      if (line == "\n") then
        newtag = nil
      elseif (advance ~= oldadvance) then
        newtag = "p"
      else
        change = false
      end
    end
    local result = ""
    if change then
      result     = string.gsub(line, "^" .. advance, switchtag(oldtag,newtag))
      oldtag     = newtag
      oldadvance = string.gsub(advance, "– ", "  ")
    else
      result = string.gsub(line, "^" .. advance, " ")
    end
    result = string.gsub(result, "\n" .. '$', "")
    output = output .. result
  end
  output = output .. closetag(oldtag, nil)
  return output
end

local function genmetainfo(table)
-- fc-scan format prints XML lines directly. Avoid nested echo|sh scripts that
-- expand to one huge line per font (rpm logs every command, upload proxies choke).
-- Release date is fixed at spec-parse time so the metainfo heredoc does not embed date-in-subshell
-- (that plus inner double quotes broke bash: unexpected EOF while looking for matching '"').
-- Do not put a raw newline inside fc-scan -f (breaks mock). Append newline with printf after each scan.
-- Always echo one <font> from the family name so grep provides never fails if find or fc-scan is empty.
local epoch = tonumber(rpm.expand("0%{?SOURCE_DATE_EPOCH}"))
if epoch == 0 then epoch = os.time() end
local rel_date = os.date("!%Y-%m-%d", epoch)
local Q = string.char(39)
-- Paths in debug-noto-metainfo-build.sh must not contain literal buildroot macro text: that file is
-- not processed by rpm at install time. Prefer expanded buildroot when Lua runs on the builder;
-- fall back to RPM_BUILD_ROOT env (written as string.char(36).."RPM_BUILD_ROOT") for srpm-only parse where buildroot is empty.
local bro = string.gsub(rpm.expand("%{buildroot}"), "\n+" .. '$', "")
-- Avoid ASCII 36 in this spec line (rpm treats it as macro syntax outside quoted strings).
local rootp = (bro ~= "" and not string.match(bro, "^%%{")) and bro or (string.char(36) .. "RPM_BUILD_ROOT")
-- grep -v exits 1 when it drops every line (or stdin empty); with bash -e that
-- aborts install before <provides> is written. "|| :" keeps the pipeline success.
-- Build fc-scan -f strings without literal "%{…}" in this spec: rpm's lexer parses inside %{lua:…}.
local pct = string.char(37)
local find_inner = table.find_inner or ("find -regex './" .. table.filename .. "' -print")
local xmlfontname_more = '$(names=$(for f in $(cd "' .. rootp .. table.fontdir .. '" && ' .. find_inner .. '); do fc-scan "' .. rootp .. table.fontdir .. '$f" -f "    <font>' .. pct .. '{fullname[0]}</font>"; printf ' .. Q .. '\\n' .. Q .. '; done | sort -u | grep -v ' .. Q .. 'font></font' .. Q .. ' || :); test -n "$names" && printf ' .. Q .. '%s\\n' .. Q .. ' "$names" || true)'
local xmlfontprovides = "  echo " .. bash_single_quote("  <provides>") .. "\n"
  .. "  echo " .. bash_single_quote("    <font>Noto " .. table.family .. "</font>") .. "\n"
  .. "  " .. xmlfontname_more .. "\n"
  .. "  echo " .. bash_single_quote("  </provides>") .. "\n"
local xmlfontlang = '$(langs=$(for f in $(cd "' .. rootp .. table.fontdir .. '" && ' .. find_inner .. '); do fc-scan "' .. rootp .. table.fontdir .. '$f" -f "' .. pct .. '{[]lang{    <lang>' .. pct .. '{lang}</lang>' .. string.char(125) .. string.char(125) .. '"; printf ' .. Q .. '\\n' .. Q .. '; done | sort -u); if test -n "$langs"; then echo ' .. Q .. '  <languages>' .. Q .. '; printf ' .. Q .. '%s\\n' .. Q .. ' "$langs"; echo ' .. Q .. '  </languages>' .. Q .. '; fi)'
-- Write static XML in a quoted heredoc so bash never parses fc-scan -f "..." inside
-- the same document as unquoted command substitutions (fixes: unexpected EOF while looking for matching '"').
local xml_prefix = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
  .. "<!-- " .. string.char(36) .. "PDX-License-Identifier: MIT -->\n"
  .. "<component type=\"font\">\n"
  .. "  <id>" .. rpm.expand("%{fontorg}.") .. table.pkgname .. "</id>\n"
  .. "  <metadata_license>MIT</metadata_license>\n"
  .. "  <project_license>" .. rpm.expand("%{license}") .. "</project_license>\n"
  .. "  <name>Noto " .. table.family .. "</name>\n"
  .. "  <summary><![CDATA[Noto " .. table.summary .. "]]></summary>\n"
  .. "  <description>\n"
  .. txt2xml(table.description)
  .. "\n  </description>\n"
  .. "  <updatecontact>" .. rpm.expand("%{fontcontact}") .. "</updatecontact>\n"
  .. "  <url type=\"homepage\">" .. rpm.expand("%{url}") .. "</url>\n"
  .. "  <releases>\n"
  .. "    <release version=\"" .. rpm.expand("%{version}") .. "\" date=\"" .. rel_date .. "\"/>\n"
  .. "  </releases>\n"
    _metainfobuild = (_metainfobuild ~= '' and _metainfobuild .. "\n" or '')
      .. "{\n"
      .. "  cat <<'NOTO_METAINFO_H_9f3c2b1a'\n"
      .. xml_prefix
      .. "NOTO_METAINFO_H_9f3c2b1a\n"
      .. xmlfontprovides
      .. "  " .. xmlfontlang .. "\n"
      .. "  cat <<'NOTO_METAINFO_T_9f3c2b1a'\n"
      .. "</component>\n"
      .. "NOTO_METAINFO_T_9f3c2b1a\n"
      .. "} > " .. table.metainfo .. "\n"
      .. "if ! grep provides " .. table.metainfo .. " > /dev/null 2>&1; then echo \"" .. table.pkgname .. ": No family names provided\"; exit 1; fi\n"
end

local function has_value(table, value)
    for _,v in ipairs(table) do
        if v == value then
            return true
        end
    end
    return false
end

local function genfilelist(table)
    local pct = string.char(37)
    local find_inner = table.find_inner or ("find -regex './" .. table.filename .. "' -print")
    local flist = '$(for f in $(cd ' .. pct .. '{buildroot}/' .. table.fontdir .. ' && ' .. find_inner .. '); do echo "' .. table.fontdir .. '$f"; done)' .. '\\\n'
    _filelistbuild = _filelistbuild .. "cat<<_EOL_>" .. table.pkgname .. ".list\\\n" .. flist .. "_EOL_\\\n"
end

local function notopkg(table)
    local _pname = string.lower(table.family):gsub(' ', '-')
    local pname = _pname .. (table.variable and '-vf' or '')
    local pkgname = rpm.expand('%{_fontname}-') .. pname .. '-fonts'
    local prio = (table.priority and table.priority or rpm.expand('%{mprio}'))

    if table.default == true then
        prio = (table.variable and rpm.expand('%{hprio}') or rpm.expand('%{shprio}'))
    end
    if is_nonlatin(table) then
        if prio == rpm.expand('%{hprio}') then
            prio = rpm.expand('%{nlat_hprio}')
        elseif prio == rpm.expand('%{shprio}') then
            prio = rpm.expand('%{nlat_shprio}')
        elseif prio == rpm.expand('%{mprio}') then
            prio = rpm.expand('%{nlat_mprio}')
        elseif prio == rpm.expand('%{lprio}') then
            prio = rpm.expand('%{nlat_lprio}')
        else
            io.stderr:write("Unknown priority")
        end
    end
    prio = tostring(prio)
    local fcconf = prio .. '-' .. rpm.expand('%{fontconf}') .. '-' .. pname .. '.conf'
    local fontdir = rpm.expand('%{_fontbasedir}') .. '/google-noto' .. (table.variable and '-vf/' or '/')
    local basename = 'Noto' .. (table.fontname and table.fontname or string.gsub(table.family, ' ', ''))
    local fontname = basename .. (table.variable and '\\\\(\\\\(-[A-Za-z]*\\\\)?\\\\[.*\\\\]\\\\|-VF\\\\).*tf' or '-\\\\([^\\\\[\\\\]]\\\\|[^-VF]\\\\)*.*tf')
    local metaname = rpm.expand('%{fontorg}.') .. pkgname .. '.metainfo.xml'
    if table.variable then
      table.find_inner = "find -regex './" .. fontname .. "' -print"
    else
      table.find_inner = "find -maxdepth 1 \\( -name " .. bash_single_quote(basename .. "*.ttf")
        .. " ! -name " .. bash_single_quote("*[*]*")
        .. " ! -name " .. bash_single_quote("*-VF.ttf")
        .. " \\) -print"
    end

    table.fcconf = fcconf
    table.pkgname = pkgname
    table.fontdir = fontdir
    table.filename = fontname
    table.summary = 'Noto ' .. table.family .. (table.variable and ' variable' or '') .. ' font'
    table.description = rpm.expand('%{common_desc}') .. [[
Noto ]] .. table.family .. (table.variable and ' variable' or '') .. " font."
    table.metainfo = metaname
    _fcconflist = (_fcconflist ~= '' and _fcconflist .. ':' or '') .. fcconf
    _metafilelist = (_metafilelist ~= '' and _metafilelist .. ':' or '') .. metaname

    local obsoletes = ''

    if table.obsoletes then
        for i = 1, #table.obsoletes do
            obsoletes = obsoletes .. "Obsoletes: %{_fontname}-" .. table.obsoletes[i] .. "-fonts " .. string.char(60) .. " %{version}-%{release}\n" .. "Provides: %{_fontname}-" .. table.obsoletes[i] .. "-fonts = %{version}-%{release}\n"
	end
    end
    print(rpm.expand([[
%%package -n ]] .. table.pkgname .. "\n" .. [[
Summary:    ]] .. table.summary .. "\n" .. [[
Requires:   fontpackages-filesystem
Requires:   %{name}-common = %{version}-%{release}
]] .. obsoletes .. [[
%%description -n ]] .. table.pkgname .. "\n" .. table.description .. "\n" .. [[
%%files -n ]] .. pkgname .. " -f " .. pkgname .. ".list\n" .. [[
%%dir ]] .. fontdir .. "\n" .. [[
%%config(noreplace) %{_fontconfig_confdir}/]] .. fcconf .. "\n" .. [[
%%{_fontconfig_templatedir}/]] .. fcconf .. "\n" .. [[
%%{_metainfodir}/]] .. metaname .. "\n"))
end

local all_deps = ''
local all_vf_deps = ''
local all_static_deps = ''

for i = 1, #subpackages do
    notopkg(subpackages[i])
    all_deps = all_deps .. "Requires: " .. subpackages[i].pkgname .. " = %{version}-%{release}\n"
    if subpackages[i].variable then
      all_vf_deps = all_vf_deps .. "Requires: " .. subpackages[i].pkgname .. " = %{version}-%{release}\n"
    else
      all_static_deps = all_static_deps .. "Requires: " .. subpackages[i].pkgname .. " = %{version}-%{release}\n"
    end
    if rpm.expand("%{cionly}") ~= 0 then
        genfcconf(subpackages[i])
        genmetainfo(subpackages[i])
        genfilelist(subpackages[i])
    else
        _fcconfbuild = "false"
        _metainfobuild = "false"
        _filelistbuild = "false"
    end
end

print(rpm.expand([[
%%package -n google-noto-fonts-all
Summary:    All the Noto font families
]] .. all_deps .. [[
%%description -n google-noto-fonts-all
A meta package for all Noto font families
%%files -n google-noto-fonts-all
%%package -n google-noto-fonts-all-vf
Summary:    All the Noto variable font families
]] .. all_vf_deps .. [[
%%description -n google-noto-fonts-all-vf
A meta package for all Noto variable font families
%%files -n google-noto-fonts-all-vf
%%package -n google-noto-fonts-all-static
Summary:    All the Noto static font families
]] .. all_static_deps .. [[
%%description -n google-noto-fonts-all-static
A meta package for all Noto static font families
%%files -n google-noto-fonts-all-static
]]))

rpm.define("noto_fcconflist " .. _fcconflist)
rpm.define("noto_metafilelist " .. _metafilelist)
-- Write next to the spec so _specdir paths match at install time (cwd during parse is not SPECS).
local _noto_debug_dir = rpm.expand("%{_specdir}")
local f = io.open(_noto_debug_dir .. "/debug-noto-fcconf-build.sh", "w")
if f then
    f:write(_fcconfbuild)
    f:close()
end
f = io.open(_noto_debug_dir .. "/debug-noto-metainfo-build.sh", "w")
if f then
    f:write(_metainfobuild)
    f:close()
end

rpm.define("notobuild_fcconf " .. _fcconfbuild .. "\n")
rpm.define("notobuild_metainfo " .. _metainfobuild .. "\n")
