%global source0_hash 2984c8c78e2ed0bb020c3fe46fd936becb43a76092953a1319ccb6275bee8c59a7dafd0d8bcd562889a6a00a15948ced427c0f6aac4e7d8f7772e1b7dae4759b

%global __brp_mangle_shebangs_exclude_from ^%{_texmf_main}/doc/.*$
%global __requires_exclude_from ^%{_texmf_main}/doc/.*$
%global tl_version 2025

Name:           texlive-collection-langitalian
Epoch:          12
Version:        svn72943
Release:        3%{?dist}
Summary:        Italian

License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
# Main collection source
%global source2_hash 9178b17bedc53957118083a78ead56f9fdaf9fd6a60ea0ebdbeee6c87254e7567b47b61bad1f9bda2554f471f79c28f3df7c3d2b9858faad65c3d110664ec4c8
%global source3_hash eb23cb624c4cf6283b8f777911d102953d31dc8da04392d7023694fed02ee1b8a8a49365fe0f1cba9682e911405f04afc982b6cc9cf9699a4d76ec8dca6a471c
%global source4_hash 6bc869e3cf11a9521ff883e9b8cd227a267d28291124c0f268556ea576bc0af8ea4eaa145e45d1de84709df08182fc83946d80fd0f116a8656a35d75ca83eef5
%global source5_hash 814539a2a82601c930097113a9baca5166fcf68d1b0c4dcf25d8afa8991e667619517879bc415ff114b9e86664b9ff5e25a7bcf1bb04160b9297cbfabb4a639d
%global source6_hash 17631e2d6306887236f11eed586454a784f256c36c14955be1eb30377f1f73b189686b37ba6c95188fda2e0b0aac9a1f40469a32bc7787b5d4c244de9a01ccdf
%global source7_hash 2d35f87da43f957d7ec3d1e61d052d14b4dc207207fc2e6dc4de08b699e5211db17a84f0305888294ae163691e4dee2d067fb1c3a29fadcc34214033fe8e22eb
%global source8_hash 02dea55dcd6eb3a3763c2966054825373add8f690675d276123ae7314b0e06b1b247fdc3d38fc12a94fd1cd05bbb52644a7049d1dca29398d75aa36e974e9945
%global source9_hash 8e1284b853480604792438a927cd21c7e3d08e252f3bbe4be050c9fe5f8147e28dbe3454c758711c9c1e8ca42aa54877228fbbb0aa073ea710d72ce48557bc76
%global source10_hash 0b7eb3f2b8115c8b4b170cdf7b0d16d465d20aac5f38c76716a206e63cb2c7e72365465843bd3a7bd5ddb95389be43346ddc450e009e69b43ceb52ba69deb6e5
%global source11_hash 653beb998363e5c0659127299d7e50bfa0e8f6c95f6a810f7571b9f5e349917f9b8575d27ec434bc4642e531bb4d509dfad2a6a4e58460d852ad4aa714a808fe
%global source12_hash 5b4e8c708019f98b9ef04255c0f1f1892996920bc9f480e9f216f6cb57167c753f6a208be0a7128c1057e3a0e17bdd9e2ea29d9557a226606a819221ef0a6a7f
%global source13_hash dd63f74941051fc4e17262f28b3071b5745d0c294df4b592155f0434150ac11250fd0e67abc27f8d98d1141ca57172effac3251294351246975a021349420e0e
%global source14_hash 7c93841ceadbb7bbfc9846d281fdbd84b7f284117344e1c4fd984e746186403e9be3e2048cfca53f6690a1e20b7471224b8d30ed1358959053111c22d3f15191
%global source15_hash 7b0c13252796be7d584d3e5dad65711229cf916ce7c8e89e423805183629f161b3d4e4f47d6c9488ab32ff8b52723b0fbc4252f2ca99e965f4d7c4409881b67d
%global source16_hash 6899f3c11ed4a8f7476fe954166ea7576446b670d0b22737766927fcd29eb24e6143ff3031b974856562a7ff55e68f208164729618a4d28d28b856919f2a666b
%global source17_hash cda5ff0581545e4eca9787b27dddcdad226b5dc9a630773b13073e9248b7b30b985fa5f5fc1bc5380e5a0d96f06c666d4e7e73168afbc2fa4ed0dd202967dafa
%global source18_hash f392c0edc17148fee811b088ecd59cf87babf4b1c5c4beea8fd812769f33d31c22ff742fc78c68825d2c1ff57fa30460d2318532f712be46584164c78998f201
%global source19_hash 920ae1ba377ae137051c510b5772deef771673144a824e1897d429e74fb332c229c71c6528b11e3ca9203947372d17b02f4969d2b2fd0699ae9697a477ee71cf
%global source20_hash 51ea564250bc55b4860f3b57536c218ea87036fd55c70c750c8552e01c87d80965e1894af0c7d164fbe755a2badb0881f99fe7aca6ab3c88f12846b0e2405d04
%global source21_hash f52ce79b4ab53b21859baf2f7f824b4fa79635c04d93cc9e928fd47ab1f6b99f8ab065e379cf299a24940ad871b98256ee6cdb7955d2c17cb301a2daaf8c15b3
%global source22_hash 3919040b226d049fcf14aea73e9f91584aae7924d71cf37955e986beeb2caee7f84e36c5c2634e261401c88b67d392cc01c587c2ff0ba6cf0062e45d064ab6cd
%global source23_hash f2374407043bc90a334c60d3fe0c1a11b239f2ea20a2c0211133ed79cd48e7846a5895c4b71f4bab0560f3040e1ae41b21d1f00ad5c64e76a0dc6437e6b4bd8f
%global source24_hash f80b06ec2909caec29a13e2cfe7e2c146ae4b8b02910d7e15f9db3c9712431086bc8a47f14eded1de14c8a1b914f42df4a2a511014486c6401ef3cad1b0eddc6
%global source25_hash 691d8936d71ca825da3a5fb193f8f7067480981b1b9bc93100f54834a7f9500e66785a216110cb1eb5cdd41b538333b693dab8e0e855e546a3eab90c43c48630
%global source26_hash c0c527bc7e9e71038316be5c6a57f4200ed69e7ed6fa0f066923cb14d14e20e90213cf0b989d3ba746bdb3e2263cf1daba56db3073017a0d7582e40640d35fd3
%global source27_hash 849b0e0fbd15b45cb31ed4856b0eaa190c26437a1965da2c860af62b65cbb000b590320611e96c5a6c4cc63c029c31fb352ec44d96e0704eb52c70ee460abcd3
%global source28_hash b4333e1361b352689dfd67e13a694a304449eac61ef8189957356bd94e5745f4c15fa38bc21219c8a21805dbecd44a51e719bbcd884b850ba1276759bdebeb94
%global source29_hash 7c3e21f50b8d02af3bbfe140693b0311f08288d0aa70f8c9adb7502b069dc6117528162ef49a3d4bef20502681917d62842d932809d27fded1bfef598d37f6fd
%global source30_hash eea88eaef52fa8ce5519f42e0de0367ba4f3240d6cd8d23ef774d70b37ba61f2a87074e9f47e4b1fe412a2868125b0c23f5af871a11219a2f68d1e3a1266a008
%global source31_hash 4d26f0191ffbbe7fa6a9aae1ece6e72739925b59a1a1db5ad3cbe8f2b3ece92ec8265f008e91fcabfe2e04863300db833eff3104486e9c33985ce5c7f8dd7543
%global source32_hash 7a513ff265d259adfbaee9ffb47856602004f19679dad1316f04d36848f2e22bff8c3164ba9b045e7a4a57df76c2ad17b071a9cac68d4b92cff57a29f1e99f55
%global source33_hash 22874afcd046572176439818fd3a1c2200d00c0e184adc4fcbfa90b2ecc88dac7f5b28eb95c74bd546fd7472fcfdb2c5b74e5b1b5d08ffe4d4a5aa5f924da698
%global source34_hash 0c0d3585bb2c12476751bc5dafb5ea5e10dcaf5149b98e823e607d7a99e5bd9dfd698d73950ecb1efe353435ba2f88be2c45e18c6cde2245df90cebfdbad4417
%global source35_hash 6d818ae04ab69cc5f1639916f15469f2b36b22b5db85a8c6e3b0b278a1a54f3a5c76bb6a7cf29133fc8cbe8ced4f4a343062f979ee6aa60a3cf7e5e4dbf4f23f
%global source36_hash 94b5448729a83fb0449621f078314cc06227698fec3d2c21c9418027f8d6b8c0a5d53dc6bed953b429f21413c59eba874fb66108237aa941d7b3bdaf67f0dafe

Source0:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/collection-langitalian.tar.xz#/collection-langitalian.or11.tar.xz

# License texts
Source1:        texlive-licenses.tar.xz

Source2:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/amsldoc-it.tar.xz#/amsldoc-it.or11.tar.xz
Source3:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/amsldoc-it.doc.tar.xz#/amsldoc-it.doc.or11.tar.xz
Source4:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/amsmath-it.tar.xz#/amsmath-it.or11.tar.xz
Source5:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/amsmath-it.doc.tar.xz#/amsmath-it.doc.or11.tar.xz
Source6:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/amsthdoc-it.tar.xz#/amsthdoc-it.or11.tar.xz
Source7:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/amsthdoc-it.doc.tar.xz#/amsthdoc-it.doc.or11.tar.xz
Source8:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/antanilipsum.tar.xz#/antanilipsum.or11.tar.xz
Source9:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/antanilipsum.doc.tar.xz#/antanilipsum.doc.or11.tar.xz
Source10:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/babel-italian.tar.xz#/babel-italian.or11.tar.xz
Source11:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/babel-italian.doc.tar.xz#/babel-italian.doc.or11.tar.xz
Source12:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/biblatex-accursius.tar.xz#/biblatex-accursius.or11.tar.xz
Source13:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/biblatex-accursius.doc.tar.xz#/biblatex-accursius.doc.or11.tar.xz
Source14:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/codicefiscaleitaliano.tar.xz#/codicefiscaleitaliano.or11.tar.xz
Source15:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/codicefiscaleitaliano.doc.tar.xz#/codicefiscaleitaliano.doc.or11.tar.xz
Source16:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/fancyhdr-it.tar.xz#/fancyhdr-it.or11.tar.xz
Source17:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/fancyhdr-it.doc.tar.xz#/fancyhdr-it.doc.or11.tar.xz
Source18:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/fixltxhyph.tar.xz#/fixltxhyph.or11.tar.xz
Source19:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/fixltxhyph.doc.tar.xz#/fixltxhyph.doc.or11.tar.xz
Source20:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/frontespizio.tar.xz#/frontespizio.or11.tar.xz
Source21:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/frontespizio.doc.tar.xz#/frontespizio.doc.or11.tar.xz
Source22:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/hyphen-italian.tar.xz#/hyphen-italian.or11.tar.xz
Source23:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/itnumpar.tar.xz#/itnumpar.or11.tar.xz
Source24:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/itnumpar.doc.tar.xz#/itnumpar.doc.or11.tar.xz
Source25:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/latex4wp-it.tar.xz#/latex4wp-it.or11.tar.xz
Source26:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/latex4wp-it.doc.tar.xz#/latex4wp-it.doc.or11.tar.xz
Source27:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/layaureo.tar.xz#/layaureo.or11.tar.xz
Source28:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/layaureo.doc.tar.xz#/layaureo.doc.or11.tar.xz
Source29:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/lshort-italian.tar.xz#/lshort-italian.or11.tar.xz
Source30:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/lshort-italian.doc.tar.xz#/lshort-italian.doc.or11.tar.xz
Source31:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/psfrag-italian.tar.xz#/psfrag-italian.or11.tar.xz
Source32:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/psfrag-italian.doc.tar.xz#/psfrag-italian.doc.or11.tar.xz
Source33:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/texlive-it.tar.xz#/texlive-it.or11.tar.xz
Source34:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/texlive-it.doc.tar.xz#/texlive-it.doc.or11.tar.xz
Source35:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/verifica.tar.xz#/verifica.or11.tar.xz
Source36:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/verifica.doc.tar.xz#/verifica.doc.or11.tar.xz
BuildRequires:  texlive-base
Requires:       texlive-base
Requires:       texlive-amsldoc-it
Requires:       texlive-amsmath-it
Requires:       texlive-amsthdoc-it
Requires:       texlive-antanilipsum
Requires:       texlive-babel-italian
Requires:       texlive-biblatex-accursius
Requires:       texlive-codicefiscaleitaliano
Requires:       texlive-collection-basic
Requires:       texlive-fancyhdr-it
Requires:       texlive-fixltxhyph
Requires:       texlive-frontespizio
Requires:       texlive-hyphen-italian
Requires:       texlive-itnumpar
Requires:       texlive-latex4wp-it
Requires:       texlive-layaureo
Requires:       texlive-lshort-italian
Requires:       texlive-psfrag-italian
Requires:       texlive-texlive-it
Requires:       texlive-verifica

%description
Support for Italian.

%package -n texlive-amsldoc-it
Summary:        Italian translation of amsldoc
Version:        svn45662
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-amsldoc-it-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-amsldoc-it-doc <= 11:%{version}

%description -n texlive-amsldoc-it
Italian translation of amsldoc

%package -n texlive-amsmath-it
Summary:        Italian translations of some old amsmath documents
Version:        svn22930
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-amsmath-it-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-amsmath-it-doc <= 11:%{version}

%description -n texlive-amsmath-it
The documents are: diffs-m.txt of December 1999, and amsmath.faq of March 2000.

%package -n texlive-amsthdoc-it
Summary:        Italian translation of amsthdoc: Using the amsthm package
Version:        svn45662
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-amsthdoc-it-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-amsthdoc-it-doc <= 11:%{version}

%description -n texlive-amsthdoc-it
Italian translation of amsthdoc: Using the amsthm package

%package -n texlive-antanilipsum
Summary:        Generate sentences in the style of "Amici miei"
Version:        svn77161
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(xparse.sty)
Provides:       tex(antanilipsum.sty) = %{tl_version}

%description -n texlive-antanilipsum
This package is an italian blind text generator that outputs supercazzole,
mocking nonsense phrases from the movie series Amici Miei ("My friends"),
directed by Mario Monicelli.

%package -n texlive-babel-italian
Summary:        Babel support for Italian text
Version:        svn77371
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(italian.ldf) = %{tl_version}

%description -n texlive-babel-italian
The package provides language definitions for use in babel.

%package -n texlive-biblatex-accursius
Summary:        Citing features for Italian jurists
Version:        svn72942
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       biber
Requires:       tex(ext-verbose-trad1.bbx)
Requires:       tex(verbose-trad1.cbx)
Provides:       tex(accursius.bbx) = %{tl_version}
Provides:       tex(accursius.cbx) = %{tl_version}

%description -n texlive-biblatex-accursius
This style is primarily aimed at Italian legal jurists and provides them with
the ability to cite legal materials, such as legislative acts, regulations,
soft law, treaties and case law. Additionally, the style codifies the most
prevalent citation practices amongst Italian legal scholars. Specifically, with
regard to the citation of legal materials, this style, instead of developing
the entry types @jurisdiction, @legal, and @legislation, creates a new one:
@itprov, which can describe a wide range of legal sources. Furthermore, it
creates a second new entry type: @notetoprov, which is used specifically to
cite so-called "note a sentenza" (notes to judgement), which closely mirrors
@itprov, but is literature and, therefore, is intended to have the same
treatment as standard entry types. The citation commands are the standard ones.
The @itprov entry type comprises the list institution to indicate which
authority adopted the cited act; the kindprov, nprov, provtitle (or
titleparties) fields to indicate the minimal 'ID' of the act and many others.
Finally, the entry type allows to specify where the cited act was consulted,
whether from an official bulletin (the ofbull field), an official portal or a
private database (the ofportal field), or a journal or collection.

%package -n texlive-codicefiscaleitaliano
Summary:        Test the consistency of the Italian personal Fiscal Code
Version:        svn29803
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(codicefiscaleitaliano.sty) = %{tl_version}

%description -n texlive-codicefiscaleitaliano
The alphanumeric string that forms the Italian personal Fiscal Code is prone to
be misspelled thus rendering a legal document invalid. The package quickly
verifies the consistency of the fiscal code string, and can therefore be useful
for lawyers and accountants that use fiscal codes very frequently.

%package -n texlive-fancyhdr-it
Summary:        Italian translation of fancyhdr documentation
Version:        svn21912
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-fancyhdr-it-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-fancyhdr-it-doc <= 11:%{version}

%description -n texlive-fancyhdr-it
The translation is of documentation provided with the fancyhdr package.

%package -n texlive-fixltxhyph
Summary:        Allow hyphenation of partially-emphasised substrings
Version:        svn73227
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(etoolbox.sty)
Provides:       tex(fixltxhyph.sty) = %{tl_version}

%description -n texlive-fixltxhyph
The package fixes the problem of TeX failing to hyphenate letter strings that
seem (to TeX) to be words, but which are followed by an apostrophe and then an
emphasis command. The cause of the problem is not the apostrophe, but the font
change in the middle of the string. The problem arises in Catalan, French,
Italian and Romansh.

%package -n texlive-frontespizio
Summary:        Create a frontispiece for Italian theses
Version:        svn24054
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(afterpage.sty)
Requires:       tex(atbegshi.sty)
Requires:       tex(environ.sty)
Requires:       tex(geometry.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(ifpdf.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(inputenc.sty)
Requires:       tex(xcolor.sty)
Provides:       tex(frontespizio.sty) = %{tl_version}

%description -n texlive-frontespizio
Typesetting a frontispiece independently of the layout of the main document is
difficult. This package provides a solution by producing an auxiliary TeX file
to be typeset on its own and the result is automatically included at the next
run. The markup necessary for the frontispiece is written in the main document
in a frontespizio environment. Documentation is mainly in Italian, as the style
is probably apt only to theses in Italy.

%package -n texlive-hyphen-italian
Summary:        Italian hyphenation patterns.
Version:        svn73410
License:        LPPL-1.3c OR MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Provides:       tex(hyph-it.tex) = %{tl_version}
Provides:       tex(hyph-quote-it.tex) = %{tl_version}
Provides:       tex(loadhyph-it.tex) = %{tl_version}

%description -n texlive-hyphen-italian
Hyphenation patterns for Italian in ASCII encoding. Compliant with the
Recommendation UNI 6461 on hyphenation issued by the Italian Standards
Institution (Ente Nazionale di Unificazione UNI).

%package -n texlive-itnumpar
Summary:        Spell numbers in words (Italian)
Version:        svn15878
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       tex(itnumpar.sty) = %{tl_version}

%description -n texlive-itnumpar
Sometimes we need to say "Capitolo primo" or "Capitolo uno" instead of
"Capitolo 1", that is, spelling the number in words instead of the usual digit
form. This package provides support for spelling out numbers in Italian words,
both in cardinal and in ordinal form.

%package -n texlive-latex4wp-it
Summary:        LaTeX guide for word processor users, in Italian
Version:        svn36000
License:        GFDL-1.3-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-latex4wp-it-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-latex4wp-it-doc <= 11:%{version}

%description -n texlive-latex4wp-it
The package provides a version of the document in Italian

%package -n texlive-layaureo
Summary:        A package to improve the A4 page layout
Version:        svn19087
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Requires:       tex(calc.sty)
Requires:       tex(geometry.sty)
Requires:       tex(keyval.sty)
Provides:       tex(layaureo.sty) = %{tl_version}

%description -n texlive-layaureo
This package produces a wide page layout for documents that use A4 paper size.
Moreover, LayAureo provides both a simple hook for leaving an empty space which
is required if pages are bundled by a press binding (use option
binding=length), and an option called big which it forces typearea to become
maximum.

%package -n texlive-lshort-italian
Summary:        Introduction to LaTeX in Italian
Version:        svn57038
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-lshort-italian-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-lshort-italian-doc <= 11:%{version}

%description -n texlive-lshort-italian
This is the Italian translation of the Short Introduction to LaTeX2e.

%package -n texlive-psfrag-italian
Summary:        PSfrag documentation in Italian
Version:        svn15878
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-psfrag-italian-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-psfrag-italian-doc <= 11:%{version}

%description -n texlive-psfrag-italian
This is a translation of the documentation that comes with the psfrag
documentation.

%package -n texlive-texlive-it
Summary:        TeX Live manual (Italian)
Version:        svn58653
License:        LicenseRef-Fedora-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-texlive-it-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-texlive-it-doc <= 11:%{version}

%description -n texlive-texlive-it
TeX Live manual (Italian)

%package -n texlive-verifica
Summary:        Typeset (Italian high school) exercises
Version:        svn75682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-verifica
This class provides various environments and commands to produce the typical
exercises contained in a test. It is mainly intended for Italian high school
teachers, as the style is probably more in line with Italian high school tests.

%post -n texlive-hyphen-italian
if [ $1 -gt 0 ]; then
sed --follow-symlinks -i '/italian.*/d' %{_texmf_main}/tex/generic/config/language.dat
echo "italian loadhyph-it.tex" >> %{_texmf_main}/tex/generic/config/language.dat
sed --follow-symlinks -i '/\\addlanguage{italian}.*/d' %{_texmf_main}/tex/generic/config/language.def
echo "\addlanguage{italian}{loadhyph-it.tex}{}{2}{2}" >> %{_texmf_main}/tex/generic/config/language.def
fi
:

%postun -n texlive-hyphen-italian
if [ $1 == 0 ] ; then
sed --follow-symlinks -i '/italian.*/d' %{_texmf_main}/tex/generic/config/language.dat > /dev/null 2>&1
sed --follow-symlinks -i '/\\addlanguage{italian}.*/d' %{_texmf_main}/tex/generic/config/language.def > /dev/null 2>&1
fi
:

%prep
test "%{source2_hash}" = "none" || { f="%{SOURCE2}"; test -f "$f" || { echo "oreon: missing Source2 $f" >&2; exit 1; }; h_expected="%{source2_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source2_hash}" || { echo "oreon: Source2 hash mismatch" >&2; exit 1; }; }
test "%{source3_hash}" = "none" || { f="%{SOURCE3}"; test -f "$f" || { echo "oreon: missing Source3 $f" >&2; exit 1; }; h_expected="%{source3_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source3_hash}" || { echo "oreon: Source3 hash mismatch" >&2; exit 1; }; }
test "%{source4_hash}" = "none" || { f="%{SOURCE4}"; test -f "$f" || { echo "oreon: missing Source4 $f" >&2; exit 1; }; h_expected="%{source4_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source4_hash}" || { echo "oreon: Source4 hash mismatch" >&2; exit 1; }; }
test "%{source5_hash}" = "none" || { f="%{SOURCE5}"; test -f "$f" || { echo "oreon: missing Source5 $f" >&2; exit 1; }; h_expected="%{source5_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source5_hash}" || { echo "oreon: Source5 hash mismatch" >&2; exit 1; }; }
test "%{source6_hash}" = "none" || { f="%{SOURCE6}"; test -f "$f" || { echo "oreon: missing Source6 $f" >&2; exit 1; }; h_expected="%{source6_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source6_hash}" || { echo "oreon: Source6 hash mismatch" >&2; exit 1; }; }
test "%{source7_hash}" = "none" || { f="%{SOURCE7}"; test -f "$f" || { echo "oreon: missing Source7 $f" >&2; exit 1; }; h_expected="%{source7_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source7_hash}" || { echo "oreon: Source7 hash mismatch" >&2; exit 1; }; }
test "%{source8_hash}" = "none" || { f="%{SOURCE8}"; test -f "$f" || { echo "oreon: missing Source8 $f" >&2; exit 1; }; h_expected="%{source8_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source8_hash}" || { echo "oreon: Source8 hash mismatch" >&2; exit 1; }; }
test "%{source9_hash}" = "none" || { f="%{SOURCE9}"; test -f "$f" || { echo "oreon: missing Source9 $f" >&2; exit 1; }; h_expected="%{source9_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source9_hash}" || { echo "oreon: Source9 hash mismatch" >&2; exit 1; }; }
test "%{source10_hash}" = "none" || { f="%{SOURCE10}"; test -f "$f" || { echo "oreon: missing Source10 $f" >&2; exit 1; }; h_expected="%{source10_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source10_hash}" || { echo "oreon: Source10 hash mismatch" >&2; exit 1; }; }
test "%{source11_hash}" = "none" || { f="%{SOURCE11}"; test -f "$f" || { echo "oreon: missing Source11 $f" >&2; exit 1; }; h_expected="%{source11_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source11_hash}" || { echo "oreon: Source11 hash mismatch" >&2; exit 1; }; }
test "%{source12_hash}" = "none" || { f="%{SOURCE12}"; test -f "$f" || { echo "oreon: missing Source12 $f" >&2; exit 1; }; h_expected="%{source12_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source12_hash}" || { echo "oreon: Source12 hash mismatch" >&2; exit 1; }; }
test "%{source13_hash}" = "none" || { f="%{SOURCE13}"; test -f "$f" || { echo "oreon: missing Source13 $f" >&2; exit 1; }; h_expected="%{source13_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source13_hash}" || { echo "oreon: Source13 hash mismatch" >&2; exit 1; }; }
test "%{source14_hash}" = "none" || { f="%{SOURCE14}"; test -f "$f" || { echo "oreon: missing Source14 $f" >&2; exit 1; }; h_expected="%{source14_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source14_hash}" || { echo "oreon: Source14 hash mismatch" >&2; exit 1; }; }
test "%{source15_hash}" = "none" || { f="%{SOURCE15}"; test -f "$f" || { echo "oreon: missing Source15 $f" >&2; exit 1; }; h_expected="%{source15_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source15_hash}" || { echo "oreon: Source15 hash mismatch" >&2; exit 1; }; }
test "%{source16_hash}" = "none" || { f="%{SOURCE16}"; test -f "$f" || { echo "oreon: missing Source16 $f" >&2; exit 1; }; h_expected="%{source16_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source16_hash}" || { echo "oreon: Source16 hash mismatch" >&2; exit 1; }; }
test "%{source17_hash}" = "none" || { f="%{SOURCE17}"; test -f "$f" || { echo "oreon: missing Source17 $f" >&2; exit 1; }; h_expected="%{source17_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source17_hash}" || { echo "oreon: Source17 hash mismatch" >&2; exit 1; }; }
test "%{source18_hash}" = "none" || { f="%{SOURCE18}"; test -f "$f" || { echo "oreon: missing Source18 $f" >&2; exit 1; }; h_expected="%{source18_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source18_hash}" || { echo "oreon: Source18 hash mismatch" >&2; exit 1; }; }
test "%{source19_hash}" = "none" || { f="%{SOURCE19}"; test -f "$f" || { echo "oreon: missing Source19 $f" >&2; exit 1; }; h_expected="%{source19_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source19_hash}" || { echo "oreon: Source19 hash mismatch" >&2; exit 1; }; }
test "%{source20_hash}" = "none" || { f="%{SOURCE20}"; test -f "$f" || { echo "oreon: missing Source20 $f" >&2; exit 1; }; h_expected="%{source20_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source20_hash}" || { echo "oreon: Source20 hash mismatch" >&2; exit 1; }; }
test "%{source21_hash}" = "none" || { f="%{SOURCE21}"; test -f "$f" || { echo "oreon: missing Source21 $f" >&2; exit 1; }; h_expected="%{source21_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source21_hash}" || { echo "oreon: Source21 hash mismatch" >&2; exit 1; }; }
test "%{source22_hash}" = "none" || { f="%{SOURCE22}"; test -f "$f" || { echo "oreon: missing Source22 $f" >&2; exit 1; }; h_expected="%{source22_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source22_hash}" || { echo "oreon: Source22 hash mismatch" >&2; exit 1; }; }
test "%{source23_hash}" = "none" || { f="%{SOURCE23}"; test -f "$f" || { echo "oreon: missing Source23 $f" >&2; exit 1; }; h_expected="%{source23_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source23_hash}" || { echo "oreon: Source23 hash mismatch" >&2; exit 1; }; }
test "%{source24_hash}" = "none" || { f="%{SOURCE24}"; test -f "$f" || { echo "oreon: missing Source24 $f" >&2; exit 1; }; h_expected="%{source24_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source24_hash}" || { echo "oreon: Source24 hash mismatch" >&2; exit 1; }; }
test "%{source25_hash}" = "none" || { f="%{SOURCE25}"; test -f "$f" || { echo "oreon: missing Source25 $f" >&2; exit 1; }; h_expected="%{source25_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source25_hash}" || { echo "oreon: Source25 hash mismatch" >&2; exit 1; }; }
test "%{source26_hash}" = "none" || { f="%{SOURCE26}"; test -f "$f" || { echo "oreon: missing Source26 $f" >&2; exit 1; }; h_expected="%{source26_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source26_hash}" || { echo "oreon: Source26 hash mismatch" >&2; exit 1; }; }
test "%{source27_hash}" = "none" || { f="%{SOURCE27}"; test -f "$f" || { echo "oreon: missing Source27 $f" >&2; exit 1; }; h_expected="%{source27_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source27_hash}" || { echo "oreon: Source27 hash mismatch" >&2; exit 1; }; }
test "%{source28_hash}" = "none" || { f="%{SOURCE28}"; test -f "$f" || { echo "oreon: missing Source28 $f" >&2; exit 1; }; h_expected="%{source28_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source28_hash}" || { echo "oreon: Source28 hash mismatch" >&2; exit 1; }; }
test "%{source29_hash}" = "none" || { f="%{SOURCE29}"; test -f "$f" || { echo "oreon: missing Source29 $f" >&2; exit 1; }; h_expected="%{source29_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source29_hash}" || { echo "oreon: Source29 hash mismatch" >&2; exit 1; }; }
test "%{source30_hash}" = "none" || { f="%{SOURCE30}"; test -f "$f" || { echo "oreon: missing Source30 $f" >&2; exit 1; }; h_expected="%{source30_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source30_hash}" || { echo "oreon: Source30 hash mismatch" >&2; exit 1; }; }
test "%{source31_hash}" = "none" || { f="%{SOURCE31}"; test -f "$f" || { echo "oreon: missing Source31 $f" >&2; exit 1; }; h_expected="%{source31_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source31_hash}" || { echo "oreon: Source31 hash mismatch" >&2; exit 1; }; }
test "%{source32_hash}" = "none" || { f="%{SOURCE32}"; test -f "$f" || { echo "oreon: missing Source32 $f" >&2; exit 1; }; h_expected="%{source32_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source32_hash}" || { echo "oreon: Source32 hash mismatch" >&2; exit 1; }; }
test "%{source33_hash}" = "none" || { f="%{SOURCE33}"; test -f "$f" || { echo "oreon: missing Source33 $f" >&2; exit 1; }; h_expected="%{source33_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source33_hash}" || { echo "oreon: Source33 hash mismatch" >&2; exit 1; }; }
test "%{source34_hash}" = "none" || { f="%{SOURCE34}"; test -f "$f" || { echo "oreon: missing Source34 $f" >&2; exit 1; }; h_expected="%{source34_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source34_hash}" || { echo "oreon: Source34 hash mismatch" >&2; exit 1; }; }
test "%{source35_hash}" = "none" || { f="%{SOURCE35}"; test -f "$f" || { echo "oreon: missing Source35 $f" >&2; exit 1; }; h_expected="%{source35_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source35_hash}" || { echo "oreon: Source35 hash mismatch" >&2; exit 1; }; }
test "%{source36_hash}" = "none" || { f="%{SOURCE36}"; test -f "$f" || { echo "oreon: missing Source36 $f" >&2; exit 1; }; h_expected="%{source36_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source36_hash}" || { echo "oreon: Source36 hash mismatch" >&2; exit 1; }; }
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h_expected="%{source0_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

# Extract license files
tar -xf %{SOURCE1}

%build
# Nothing to build

%install
mkdir -p %{buildroot}%{_texmf_main}

tar -xf %{SOURCE2} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE3} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE4} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE5} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE6} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE7} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE8} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE9} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE10} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE11} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE12} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE13} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE14} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE15} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE16} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE17} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE18} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE19} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE20} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE21} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE22} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE23} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE24} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE25} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE26} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE27} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE28} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE29} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE30} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE31} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE32} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE33} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE34} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE35} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE36} -C %{buildroot}%{_texmf_main}

# Remove tlpobj files
rm -rf %{buildroot}%{_texmf_main}/tlpkg/tlpobj/*.tlpobj

# Main collection metapackage (empty)
%files

%files -n texlive-amsldoc-it
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/latex/amsldoc-it/

%files -n texlive-amsmath-it
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/latex/amsmath-it/

%files -n texlive-amsthdoc-it
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/latex/amsthdoc-it/

%files -n texlive-antanilipsum
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/antanilipsum/
%doc %{_texmf_main}/doc/latex/antanilipsum/

%files -n texlive-babel-italian
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/babel-italian/
%doc %{_texmf_main}/doc/generic/babel-italian/

%files -n texlive-biblatex-accursius
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/biblatex-accursius/
%doc %{_texmf_main}/doc/latex/biblatex-accursius/

%files -n texlive-codicefiscaleitaliano
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/codicefiscaleitaliano/
%doc %{_texmf_main}/doc/latex/codicefiscaleitaliano/

%files -n texlive-fancyhdr-it
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/latex/fancyhdr-it/

%files -n texlive-fixltxhyph
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/fixltxhyph/
%doc %{_texmf_main}/doc/latex/fixltxhyph/

%files -n texlive-frontespizio
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/frontespizio/
%doc %{_texmf_main}/doc/latex/frontespizio/

%files -n texlive-hyphen-italian
%license lppl1.3c.txt
%license mit.txt
%{_texmf_main}/tex/generic/hyph-utf8/

%files -n texlive-itnumpar
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/itnumpar/
%doc %{_texmf_main}/doc/latex/itnumpar/

%files -n texlive-latex4wp-it
%license fdl.txt
%doc %{_texmf_main}/doc/latex/latex4wp-it/

%files -n texlive-layaureo
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/layaureo/
%doc %{_texmf_main}/doc/latex/layaureo/

%files -n texlive-lshort-italian
%license gpl2.txt
%doc %{_texmf_main}/doc/latex/lshort-italian/

%files -n texlive-psfrag-italian
%license gpl2.txt
%doc %{_texmf_main}/doc/latex/psfrag-italian/

%files -n texlive-texlive-it
%license pd.txt
%doc %{_texmf_main}/doc/texlive/texlive-it/

%files -n texlive-verifica
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/verifica/
%doc %{_texmf_main}/doc/latex/verifica/

%changelog
%autochangelog
