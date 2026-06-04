%global source0_hash b89049b511756599b6f004b7f8fc5df05e27b1e2ac87afd247cc6e2a4a43b6cb
%global source1_hash ec054fde139651b0c3be678b5de3ea9e6d2e586df479c962785f947adc486a0c
%global source2_hash 8fa7a956504020982f0eeace49c2dc65ba7d19f178403030474d85c5709582b1
%global source3_hash 951d028c383fc255043727ff2571410959642dbefbc3fa4a61c42bd2af604cea
%global source4_hash ebedd3dc7ece433d366d848ea8bd9cd2642a0f49c000c46a2ed1dde5b1cebc1c
%global source5_hash ada5920f0d16ea3fb6b523decb0447564c4537b2b770a9bdbb837b3ec68a3992
%global source6_hash 4451bd870e03212ea3c531156371d6cdab3a2b81e80aea7c40f8c076824740a0
%global source7_hash 526d8abdab83128a80bd2c163b4f12e0679482e7493aafaed68cec80ec2770b9
%global source8_hash bb85425c214b1056b5f0b8f3bf1478b81e89bd7d290d61c7c73289b534786897
%global source9_hash 84f0d011f0cb75aae92ff40c4d004738477d59a8dfa33abbb3441f64e6878edc
%global source10_hash c069cae12bb8bf51b31044a981d93d8cb47dc06627175f1320515d2c187d28c5
%global source11_hash e45a1162c691ee9a02d6ddff491bca444360b98bc38cf926a1b24dc1ae9143c1
%global source12_hash f4792b640008ccc637a4d0cbaab2d90b58cfc96f7f73c3d9b02f2f4481cc59e3
%global source13_hash 1cfc94bf7b3fac9aecd1032f052be8d818b680541df3f5138cddb66615522103
%global source14_hash 6d0323de249a462a8386bc8aa4a1a2b36dc18def339e460ef9e743a28d671875
%global source15_hash e853ea53389bdedf98ec83867a4d738c35af767df870783396722b0a0c50c3ec
%global source16_hash 711fa92c9559c7563fd2e359cb39a988e843d2499953742f95a29439e09e6b87
%global source17_hash 270a8d4423774acfbc903036699fd689a76384260d75827e2ef3f9ad6e35e3d3
%global source18_hash 7f2fddb30c1c8a84ace60246f3adecf645c40a03b83209380d5a78ec92e228d0
%global source19_hash b36948a2ef6226f2eea6c79ee71e581b1069fce462e08a4973b18f120e045ea8
%global source20_hash fe8136043cf4f3a9b2750066e031fee12e0a2d15724aa484abd0b4ca1fbf6f8b
%global source21_hash 1a4925b47f9d8bd6b7fe8696cb52543a181aa89dca4a4bc8bdd6650ed50c6076
%global source22_hash 604c0057aa73e47bbfddea397e1b77cb8a1a60f40ffdc547cbeb0adbbc40552e
%global source23_hash 5ed1bfe91b72a15d44f2f762d13390775b887524625f11a7b4f212dc8cc7acfa
%global source24_hash 39a2c498d55f19448ed7ac26c2143943669a0e4d99e8b804ba975889c3d86ec8
%global source25_hash 0c08809797d548a331e2dcaa09f7d0989d032a0bf441ca5008aa0d67241d3abd
%global source26_hash 47f476f35cb04419e7d12667ac6e1a656f5bb2a9496821030490fc132ad85f5b
%global source27_hash 5fac7dbcc4f8aae032705f1b63f95abbfc646267e384d4e594cd8b4b9b3b0781
%global source28_hash 122ca4e9e646f137c076ab7e07fe9d53464e97d370cbc47424fc1b361ba2926c
%global source29_hash c20f4fe5992b8b27ef1ec558b701cc53d12060a6efe3198186c3a1bd28251c68
%global source30_hash 4925597c59230ffc8ef44a080783e585df4dbd6684b319ad640ea899e485ef87
%global source31_hash c5386d17116b6a51601a25081675cc5dfb9bc8734240131fe698b5ffff8214a2
%global source32_hash 29e84a4395b61f9dc1a96b334cc1e58524173c8f9139c9b43b9a61a23df74205
%global source33_hash 78f1d71a706d96bc9f793ce9ffb71f919805fda1903ca881368cd8d117a42187
%global source34_hash 7fb50b0fe6f5fb9e63e5147804fa27853dc1d9f2319921404730447b201cde9f
%global source35_hash d42eae30f6636140f32330c773f89cc16a6fd28607fe747be629ce71706b99f5
%global source36_hash 7dd9f8d9e53ecd1dac44ac5de0cf9fea5e390688f790206dddc3bc9676a74b69
%global source37_hash 78660fa5e1e41386361a973e3a78cefa23393e844266424f56e88f3315f3816c
%global source38_hash 593f4702625bf32467814f182ebec8b37ab27a8b233d19523eff84e7667153bc
%global source39_hash 80bdf4104f2e126051b88d02fc5a69aa110313cbdc1d6640715565d018a1eeb4
%global source40_hash 5d1d3516a96246cfbace7457628e285a24df3b3ad77ea9d619bf8c46451ae6d6
%global source41_hash ada105278f37f41d904807856028ab4bc4b3961a75e06496a280a2ff57975d3d

%global __brp_mangle_shebangs_exclude_from ^%{_texmf_main}/doc/.*$
%global __requires_exclude_from ^%{_texmf_main}/doc/.*$
%global tl_version 2025

Name:           texlive-collection-basic
Epoch:          12
Version:        svn72890
Release:        11%{?dist}
Summary:        Essential programs and files

License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
# Main collection source
Source0:        https://mirror.ctan.org/systems/texlive/tlnet/archive/collection-basic.tar.xz

# License texts
Source1:        texlive-licenses.tar.xz

Source2:        https://mirror.ctan.org/systems/texlive/tlnet/archive/amsfonts.tar.xz
Source3:        https://mirror.ctan.org/systems/texlive/tlnet/archive/amsfonts.doc.tar.xz
Source4:        https://mirror.ctan.org/systems/texlive/tlnet/archive/cm.tar.xz
Source5:        https://mirror.ctan.org/systems/texlive/tlnet/archive/cm.doc.tar.xz
Source6:        https://mirror.ctan.org/systems/texlive/tlnet/archive/colorprofiles.tar.xz
Source7:        https://mirror.ctan.org/systems/texlive/tlnet/archive/colorprofiles.doc.tar.xz
Source8:        https://mirror.ctan.org/systems/texlive/tlnet/archive/ec.tar.xz
Source9:        https://mirror.ctan.org/systems/texlive/tlnet/archive/ec.doc.tar.xz
Source10:        https://mirror.ctan.org/systems/texlive/tlnet/archive/enctex.tar.xz
Source11:        https://mirror.ctan.org/systems/texlive/tlnet/archive/enctex.doc.tar.xz
Source12:        https://mirror.ctan.org/systems/texlive/tlnet/archive/etex.tar.xz
Source13:        https://mirror.ctan.org/systems/texlive/tlnet/archive/etex.doc.tar.xz
Source14:        https://mirror.ctan.org/systems/texlive/tlnet/archive/etex-pkg.tar.xz
Source15:        https://mirror.ctan.org/systems/texlive/tlnet/archive/etex-pkg.doc.tar.xz
Source16:        https://mirror.ctan.org/systems/texlive/tlnet/archive/graphics-def.tar.xz
Source17:        https://mirror.ctan.org/systems/texlive/tlnet/archive/graphics-def.doc.tar.xz
Source18:        https://mirror.ctan.org/systems/texlive/tlnet/archive/hyph-utf8.tar.xz
Source19:        https://mirror.ctan.org/systems/texlive/tlnet/archive/hyph-utf8.doc.tar.xz
Source20:        https://mirror.ctan.org/systems/texlive/tlnet/archive/hyphen-base.tar.xz
Source21:        https://mirror.ctan.org/systems/texlive/tlnet/archive/hyphenex.tar.xz
Source22:        https://mirror.ctan.org/systems/texlive/tlnet/archive/ifplatform.tar.xz
Source23:        https://mirror.ctan.org/systems/texlive/tlnet/archive/ifplatform.doc.tar.xz
Source24:        https://mirror.ctan.org/systems/texlive/tlnet/archive/iftex.tar.xz
Source25:        https://mirror.ctan.org/systems/texlive/tlnet/archive/iftex.doc.tar.xz
Source26:        https://mirror.ctan.org/systems/texlive/tlnet/archive/knuth-lib.tar.xz
Source27:        https://mirror.ctan.org/systems/texlive/tlnet/archive/knuth-local.tar.xz
Source28:        https://mirror.ctan.org/systems/texlive/tlnet/archive/lua-alt-getopt.tar.xz
Source29:        https://mirror.ctan.org/systems/texlive/tlnet/archive/lua-alt-getopt.doc.tar.xz
Source30:        https://mirror.ctan.org/systems/texlive/tlnet/archive/mflogo.tar.xz
Source31:        https://mirror.ctan.org/systems/texlive/tlnet/archive/mflogo.doc.tar.xz
Source32:        https://mirror.ctan.org/systems/texlive/tlnet/archive/modes.tar.xz
Source33:        https://mirror.ctan.org/systems/texlive/tlnet/archive/modes.doc.tar.xz
Source34:        https://mirror.ctan.org/systems/texlive/tlnet/archive/plain.tar.xz
Source35:        https://mirror.ctan.org/systems/texlive/tlnet/archive/tex-ini-files.tar.xz
Source36:        https://mirror.ctan.org/systems/texlive/tlnet/archive/tex-ini-files.doc.tar.xz
Source37:        https://mirror.ctan.org/systems/texlive/tlnet/archive/texlive-common.tar.xz
Source38:        https://mirror.ctan.org/systems/texlive/tlnet/archive/texlive-common.doc.tar.xz
Source39:        https://mirror.ctan.org/systems/texlive/tlnet/archive/texlive-msg-translations.tar.xz
Source40:        https://mirror.ctan.org/systems/texlive/tlnet/archive/unicode-data.tar.xz
Source41:        https://mirror.ctan.org/systems/texlive/tlnet/archive/unicode-data.doc.tar.xz

# Patches
Patch0:         etex-addlanguage-fix-bz1215257.patch
BuildRequires:  texlive-base
BuildRequires:  python3-rpm-macros
BuildRequires:  python3-devel
Requires:       texlive-base
Requires:       texlive-amsfonts
Requires:       texlive-bibtex
Requires:       texlive-cm
Requires:       texlive-colorprofiles
Requires:       texlive-dvipdfmx
Requires:       texlive-dvips
Requires:       texlive-ec
Requires:       texlive-enctex
Requires:       texlive-etex
Requires:       texlive-etex-pkg
Requires:       texlive-extractbb
Requires:       texlive-glyphlist
Requires:       texlive-graphics-def
Requires:       texlive-hyph-utf8
Requires:       texlive-hyphen-base
Requires:       texlive-hyphenex
Requires:       texlive-ifplatform
Requires:       texlive-iftex
Requires:       texlive-knuth-lib
Requires:       texlive-knuth-local
Requires:       texlive-kpathsea
Requires:       texlive-lua-alt-getopt
Requires:       texlive-luahbtex
Requires:       texlive-luatex
Requires:       texlive-makeindex
Requires:       texlive-metafont
Requires:       texlive-mflogo
Requires:       texlive-mfware
Requires:       texlive-modes
Requires:       texlive-pdftex
Requires:       texlive-plain
Requires:       texlive-tex
Requires:       texlive-tex-ini-files
Requires:       texlive-texlive-common
Requires:       texlive-texlive-en
Requires:       texlive-texlive-msg-translations
Requires:       texlive-texlive-scripts
Requires:       texlive-texlive.infra
Requires:       texlive-unicode-data
Requires:       texlive-xdvi
Provides:       tex(tex) = %{tl_version}
Provides:       tex = %{tl_version}

%description
These files are regarded as basic for any TeX system, covering plain TeX
macros, Computer Modern fonts, and configuration for common drivers; no LaTeX.


%package -n texlive-amsfonts
Summary:        TeX fonts from the American Mathematical Society
Version:        svn77682
License:        OFL-1.1
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-amsfonts-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-amsfonts-doc <= 11:%{version}

%description -n texlive-amsfonts
An extended set of fonts for use in mathematics, including: extra mathematical
symbols; blackboard bold letters (uppercase only); fraktur letters; subscript
sizes of bold math italic and bold Greek letters; subscript sizes of large
symbols such as sum and product; added sizes of the Computer Modern small caps
font; cyrillic fonts (from the University of Washington); Euler mathematical
fonts. All fonts are provided as Adobe Type 1 files, and all except the Euler
fonts are provided as Metafont source. The distribution also includes the
canonical Type 1 versions of the Computer Modern family of fonts. Basic LaTeX
support for the symbol fonts is provided by amsfonts.sty, with names of
individual symbols defined in amssymb.sty. The Euler fonts are supported by
separate packages; details can be found in the documentation.

%package -n texlive-cm
Summary:        Computer Modern fonts
Version:        svn57963
License:        Knuth-CTAN
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-cm-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-cm-doc <= 11:%{version}

%description -n texlive-cm
Knuth's final iteration of his re-interpretation of a c.19 Modern-style font
from Monotype. The family is comprehensive, offering both sans and roman
styles, and a monospaced font, together with mathematics fonts closely
integrated with the mathematical facilities of TeX itself. The base fonts are
distributed as Metafont source, but autotraced PostScript Type 1 versions are
available (one version in the AMS fonts distribution, and also the BaKoMa
distribution). The Computer Modern fonts have inspired many later families,
notably the European Computer Modern and the Latin Modern families.

%package -n texlive-colorprofiles
Summary:        Collection of free ICC profiles
Version:        svn49086
License:        LPPL-1.3c AND MIT AND LicenseRef-Public-Domain AND Zlib
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-colorprofiles
This package collects free ICC profiles that can be used by color profile aware
applications/tools like the pdfx package, as well as TeX and LaTeX packages to
access them.

%package -n texlive-ec
Summary:        Computer modern fonts in T1 and TS1 encodings
Version:        svn25033
License:        LicenseRef-ec
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-ec-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-ec-doc <= 11:%{version}

%description -n texlive-ec
The EC fonts are European Computer Modern Fonts, supporting the complete LaTeX
T1 encoding defined at the 1990 TUG conference hold at Cork/Ireland. These
fonts are intended to be stable with no changes being made to the tfm files.
The set also contains a Text Companion Symbol font, called tc, featuring many
useful characters needed in text typesetting, for example oldstyle digits,
currency symbols (including the newly created Euro symbol), the permille sign,
copyright, trade mark and servicemark as well as a copyleft sign, and many
others. Recent releases of LaTeX2e support the EC fonts. The EC fonts supersede
the preliminary version released as the DC fonts. The fonts are available in
(traced) Adobe Type 1 format, as part of the cm-super bundle. The other
Computer Modern-style T1-encoded Type 1 set, Latin Modern, is not actually a
direct development of the EC set, and differs from the EC in a number of
particulars.

%package -n texlive-enctex
Summary:        A TeX extension that translates input on its way into TeX
Version:        svn34957
License:        GPL-2.0-or-later
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-enctex-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-enctex-doc <= 11:%{version}

%description -n texlive-enctex
EncTeX is (another) TeX extension, written at the change-file level. It
provides means of translating input on the way into TeX. It allows, for
example, translation of multibyte sequences, such as utf-8 encoding.

%package -n texlive-etex
Summary:        An extended version of TeX, from the NTS project
Version:        svn77830
License:        Knuth-CTAN
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-etex-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-etex-doc <= 11:%{version}

%description -n texlive-etex
An extended version of TeX (capable of running as if it were unmodified TeX).
E-TeX has been specified by the LaTeX team as the base engine for LaTeX2e.
Thus, LaTeX programmers may assume e-TeX functionality, along with additional
extensions. The pdftex engine and others directly incorporate the e-TeX
extensions. The etex program in most distributions is an incarnation of pdftex
running in DVI mode. The development source for e-TeX is the TeX Live source
repository, although further extensions have taken place in the pdftex and
other engine sources, keeping e-TeX stable.

%package -n texlive-etex-pkg
Summary:        E-TeX support package
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-etex-pkg-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-etex-pkg-doc <= 11:%{version}

%description -n texlive-etex-pkg
The package provides support for LaTeX documents to use many of the extensions
offered by e-TeX; in particular, it modifies LaTeX's register allocation macros
to make use of the extended register range. The etextools package provides
macros that make more sophisticated use of e-TeX's facilities.

%package -n texlive-graphics-def
Summary:        Colour and graphics option files
Version:        svn76719
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-graphics-def
This bundle is a combined distribution consisting of dvips.def, pdftex.def,
luatex.def, xetex.def, dvipdfmx.def, and dvisvgm.def driver option files for
the LaTeX graphics and color packages. It is hoped that by combining their
source repositories at https://github.com/latex3/graphics-def it will be easier
to coordinate updates.

%package -n texlive-hyph-utf8
Summary:        Hyphenation patterns expressed in UTF-8
Version:        svn78069
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-hyph-utf8-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-hyph-utf8-doc <= 11:%{version}

%description -n texlive-hyph-utf8
Modern native UTF-8 engines such as XeTeX and LuaTeX need hyphenation patterns
in UTF-8 format, whereas older systems require hyphenation patterns in the
8-bit encoding of the font in use (such encodings are codified in the LaTeX
scheme with names like OT1, T2A, TS1, OML, LY1, etc). The present package
offers a collection of conversions of existing patterns to UTF-8 format,
together with converters for use with 8-bit fonts in older systems. Since
hyphenation patterns for Knuthian-style TeX systems are only read at iniTeX
time, it is hoped that the UTF-8 patterns, with their converters, will
completely supplant the older patterns.

%package -n texlive-hyphen-base
Summary:        Core hyphenation support files
Version:        svn78076
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-hyphen-base
Includes Knuth's original hyphen.tex, zerohyph.tex to disable hyphenation,
language.us which starts the autogenerated files language.dat and language.def
(and default versions of those), etc.

%package -n texlive-hyphenex
Summary:        US English hyphenation exceptions file
Version:        svn57387
License:        LicenseRef-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-hyphenex
Exceptions for American English hyphenation patterns are occasionally published
in the TeX User Group journal TUGboat. This bundle provides alternative Perl
and Bourne shell scripts to convert the source of such an article into an
exceptions file, together with a recent copy of the article and
machine-readable files.

%package -n texlive-ifplatform
Summary:        Conditionals to test which platform is being used
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-ifplatform-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-ifplatform-doc <= 11:%{version}
Requires:       tex(catchfile.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(pdftexcmds.sty)
Requires:       tex(shellesc.sty)

%description -n texlive-ifplatform
This package uses the (La)TeX extension -shell-escape to establish whether the
document is being processed on a Windows or on a Unix-like system (Mac OS X,
Linux, etc.), or on Cygwin (Unix environment over a windows system). Booleans
provided are: \ifwindows, \iflinux, \ifmacosx and \ifcygwin. The package also
preserves the output of uname on a Unix-like system, which may be used to
distinguish between various classes of Unix systems.

%package -n texlive-iftex
Summary:        Am I running under pdfTeX, XeTeX or LuaTeX?
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-iftex-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-iftex-doc <= 11:%{version}

%description -n texlive-iftex
The package, which works both for Plain TeX and for LaTeX, defines the
\ifPDFTeX, \ifXeTeX, and \ifLuaTeX conditionals for testing which engine is
being used for typesetting. The package also provides the \RequirePDFTeX,
\RequireXeTeX, and \RequireLuaTeX commands which throw an error if pdfTeX,
XeTeX or LuaTeX (respectively) is not the engine in use.

%package -n texlive-knuth-lib
Summary:        Core TeX and Metafont sources from Knuth
Version:        svn57963
License:        Knuth-CTAN
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-knuth-lib
A collection of core TeX and Metafont macro files from DEK, apart from the
plain format and base. Includes the MF logo font(s), webmac.tex, etc.

%package -n texlive-knuth-local
Summary:        Knuth's local information
Version:        svn57963
License:        LicenseRef-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-knuth-local
A collection of experimental programs and developments based on, or
complementary to, the matter in his distribution directories.

%package -n texlive-lua-alt-getopt
Summary:        Process application arguments the same way as getopt_long
Version:        svn78415
License:        MIT
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-lua-alt-getopt-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-lua-alt-getopt-doc <= 11:%{version}

%description -n texlive-lua-alt-getopt
lua_altgetopt is a MIT-licensed module for Lua, for processing application
arguments in the same way as BSD/GNU getopt_long(3) functions do. This module
is made available for Lua script writers to have consistent command line
parsing routines.

%package -n texlive-mflogo
Summary:        LaTeX support for Metafont logo fonts
Version:        svn77682
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-mflogo-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-mflogo-doc <= 11:%{version}

%description -n texlive-mflogo
LaTeX package and font definition file to access the Knuthian mflogo fonts
described in 'The Metafontbook' and to typeset Metafont logos in LaTeX
documents.

%package -n texlive-modes
Summary:        A collection of Metafont mode_def's
Version:        svn77365
License:        LicenseRef-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-modes
The modes file collects all known Metafont modes for printing or display
devices, of whatever printing technology. Special provision is made for
write-white printers, and a 'landscape' mode is available, for making suitable
fonts for printers with pixels whose aspect is non-square. The file also
provides definitions that make \specials identifying the mode in Metafont's GF
output, and put coding information and other Xerox-world information in the TFM
file.

%package -n texlive-plain
Summary:        The Plain TeX format
Version:        svn75712
License:        Knuth-CTAN
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-plain
Contains files used to build the Plain TeX format, as described in the TeXbook,
together with various supporting files (some also discussed in the book).

%package -n texlive-tex-ini-files
Summary:        Model TeX format creation files
Version:        svn78524
License:        LicenseRef-Public-Domain
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-tex-ini-files-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-tex-ini-files-doc <= 11:%{version}

%description -n texlive-tex-ini-files
This bundle provides a collection of model .ini files for creating TeX formats.
These files are commonly used to introduce distribution-dependent variations in
formats. They are also used to allow existing format source files to be used
with newer engines, for example to adapt the plain e-TeX source file to work
with XeTeX and LuaTeX.

%package -n texlive-texlive-common
Summary:        TeX Live documentation (common elements)
Version:        svn78660
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-texlive-common-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-texlive-common-doc <= 11:%{version}

%description -n texlive-texlive-common
TeX Live documentation (common elements)

%package -n texlive-texlive-msg-translations
Summary:        Translations of the TeX Live installer and TeX Live Manager
Version:        svn78661
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea

%description -n texlive-texlive-msg-translations
This package contains the translated messages of the TeX Live installer and TeX
Live Manager. For information on creating or updating translations, see
https://tug.org/texlive/doc.html#install-tl-xlate.

%package -n texlive-unicode-data
Summary:        Unicode data and loaders for TeX
Version:        svn76413
License:        LPPL-1.3c
Requires:       texlive-base
Requires:       texlive-kpathsea
Provides:       texlive-unicode-data-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-unicode-data-doc <= 11:%{version}

%description -n texlive-unicode-data
This bundle provides generic access to Unicode Consortium data for TeX use. It
contains a set of text files provided by the Unicode Consortium which are
currently all from Unicode 8.0.0, with the exception of MathClass.txt which is
not currently part of the Unicode Character Database. Accompanying these source
data are generic TeX loader files allowing this data to be used as part of TeX
runs, in particular in building format files. Currently there are two loader
files: one for general character set up and one for initialising XeTeX
character classes as has been carried out to date by unicode-letters.tex. The
source data are distributed in accordance with the license stipulated by the
Unicode Consortium. The bundle as a whole is co-ordinated by the LaTeX3 Project
as a general resource for TeX users.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }
test "%{source2_hash}" = "none" || { f="%{SOURCE2}"; test -f "$f" || { echo "oreon: missing Source2 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source2_hash}" || { echo "oreon: Source2 hash mismatch" >&2; exit 1; }; }
test "%{source3_hash}" = "none" || { f="%{SOURCE3}"; test -f "$f" || { echo "oreon: missing Source3 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source3_hash}" || { echo "oreon: Source3 hash mismatch" >&2; exit 1; }; }
test "%{source4_hash}" = "none" || { f="%{SOURCE4}"; test -f "$f" || { echo "oreon: missing Source4 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source4_hash}" || { echo "oreon: Source4 hash mismatch" >&2; exit 1; }; }
test "%{source5_hash}" = "none" || { f="%{SOURCE5}"; test -f "$f" || { echo "oreon: missing Source5 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source5_hash}" || { echo "oreon: Source5 hash mismatch" >&2; exit 1; }; }
test "%{source6_hash}" = "none" || { f="%{SOURCE6}"; test -f "$f" || { echo "oreon: missing Source6 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source6_hash}" || { echo "oreon: Source6 hash mismatch" >&2; exit 1; }; }
test "%{source7_hash}" = "none" || { f="%{SOURCE7}"; test -f "$f" || { echo "oreon: missing Source7 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source7_hash}" || { echo "oreon: Source7 hash mismatch" >&2; exit 1; }; }
test "%{source8_hash}" = "none" || { f="%{SOURCE8}"; test -f "$f" || { echo "oreon: missing Source8 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source8_hash}" || { echo "oreon: Source8 hash mismatch" >&2; exit 1; }; }
test "%{source9_hash}" = "none" || { f="%{SOURCE9}"; test -f "$f" || { echo "oreon: missing Source9 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source9_hash}" || { echo "oreon: Source9 hash mismatch" >&2; exit 1; }; }
test "%{source10_hash}" = "none" || { f="%{SOURCE10}"; test -f "$f" || { echo "oreon: missing Source10 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source10_hash}" || { echo "oreon: Source10 hash mismatch" >&2; exit 1; }; }
test "%{source11_hash}" = "none" || { f="%{SOURCE11}"; test -f "$f" || { echo "oreon: missing Source11 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source11_hash}" || { echo "oreon: Source11 hash mismatch" >&2; exit 1; }; }
test "%{source12_hash}" = "none" || { f="%{SOURCE12}"; test -f "$f" || { echo "oreon: missing Source12 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source12_hash}" || { echo "oreon: Source12 hash mismatch" >&2; exit 1; }; }
test "%{source13_hash}" = "none" || { f="%{SOURCE13}"; test -f "$f" || { echo "oreon: missing Source13 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source13_hash}" || { echo "oreon: Source13 hash mismatch" >&2; exit 1; }; }
test "%{source14_hash}" = "none" || { f="%{SOURCE14}"; test -f "$f" || { echo "oreon: missing Source14 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source14_hash}" || { echo "oreon: Source14 hash mismatch" >&2; exit 1; }; }
test "%{source15_hash}" = "none" || { f="%{SOURCE15}"; test -f "$f" || { echo "oreon: missing Source15 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source15_hash}" || { echo "oreon: Source15 hash mismatch" >&2; exit 1; }; }
test "%{source16_hash}" = "none" || { f="%{SOURCE16}"; test -f "$f" || { echo "oreon: missing Source16 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source16_hash}" || { echo "oreon: Source16 hash mismatch" >&2; exit 1; }; }
test "%{source17_hash}" = "none" || { f="%{SOURCE17}"; test -f "$f" || { echo "oreon: missing Source17 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source17_hash}" || { echo "oreon: Source17 hash mismatch" >&2; exit 1; }; }
test "%{source18_hash}" = "none" || { f="%{SOURCE18}"; test -f "$f" || { echo "oreon: missing Source18 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source18_hash}" || { echo "oreon: Source18 hash mismatch" >&2; exit 1; }; }
test "%{source19_hash}" = "none" || { f="%{SOURCE19}"; test -f "$f" || { echo "oreon: missing Source19 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source19_hash}" || { echo "oreon: Source19 hash mismatch" >&2; exit 1; }; }
test "%{source20_hash}" = "none" || { f="%{SOURCE20}"; test -f "$f" || { echo "oreon: missing Source20 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source20_hash}" || { echo "oreon: Source20 hash mismatch" >&2; exit 1; }; }
test "%{source21_hash}" = "none" || { f="%{SOURCE21}"; test -f "$f" || { echo "oreon: missing Source21 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source21_hash}" || { echo "oreon: Source21 hash mismatch" >&2; exit 1; }; }
test "%{source22_hash}" = "none" || { f="%{SOURCE22}"; test -f "$f" || { echo "oreon: missing Source22 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source22_hash}" || { echo "oreon: Source22 hash mismatch" >&2; exit 1; }; }
test "%{source23_hash}" = "none" || { f="%{SOURCE23}"; test -f "$f" || { echo "oreon: missing Source23 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source23_hash}" || { echo "oreon: Source23 hash mismatch" >&2; exit 1; }; }
test "%{source24_hash}" = "none" || { f="%{SOURCE24}"; test -f "$f" || { echo "oreon: missing Source24 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source24_hash}" || { echo "oreon: Source24 hash mismatch" >&2; exit 1; }; }
test "%{source25_hash}" = "none" || { f="%{SOURCE25}"; test -f "$f" || { echo "oreon: missing Source25 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source25_hash}" || { echo "oreon: Source25 hash mismatch" >&2; exit 1; }; }
test "%{source26_hash}" = "none" || { f="%{SOURCE26}"; test -f "$f" || { echo "oreon: missing Source26 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source26_hash}" || { echo "oreon: Source26 hash mismatch" >&2; exit 1; }; }
test "%{source27_hash}" = "none" || { f="%{SOURCE27}"; test -f "$f" || { echo "oreon: missing Source27 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source27_hash}" || { echo "oreon: Source27 hash mismatch" >&2; exit 1; }; }
test "%{source28_hash}" = "none" || { f="%{SOURCE28}"; test -f "$f" || { echo "oreon: missing Source28 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source28_hash}" || { echo "oreon: Source28 hash mismatch" >&2; exit 1; }; }
test "%{source29_hash}" = "none" || { f="%{SOURCE29}"; test -f "$f" || { echo "oreon: missing Source29 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source29_hash}" || { echo "oreon: Source29 hash mismatch" >&2; exit 1; }; }
test "%{source30_hash}" = "none" || { f="%{SOURCE30}"; test -f "$f" || { echo "oreon: missing Source30 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source30_hash}" || { echo "oreon: Source30 hash mismatch" >&2; exit 1; }; }
test "%{source31_hash}" = "none" || { f="%{SOURCE31}"; test -f "$f" || { echo "oreon: missing Source31 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source31_hash}" || { echo "oreon: Source31 hash mismatch" >&2; exit 1; }; }
test "%{source32_hash}" = "none" || { f="%{SOURCE32}"; test -f "$f" || { echo "oreon: missing Source32 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source32_hash}" || { echo "oreon: Source32 hash mismatch" >&2; exit 1; }; }
test "%{source33_hash}" = "none" || { f="%{SOURCE33}"; test -f "$f" || { echo "oreon: missing Source33 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source33_hash}" || { echo "oreon: Source33 hash mismatch" >&2; exit 1; }; }
test "%{source34_hash}" = "none" || { f="%{SOURCE34}"; test -f "$f" || { echo "oreon: missing Source34 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source34_hash}" || { echo "oreon: Source34 hash mismatch" >&2; exit 1; }; }
test "%{source35_hash}" = "none" || { f="%{SOURCE35}"; test -f "$f" || { echo "oreon: missing Source35 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source35_hash}" || { echo "oreon: Source35 hash mismatch" >&2; exit 1; }; }
test "%{source36_hash}" = "none" || { f="%{SOURCE36}"; test -f "$f" || { echo "oreon: missing Source36 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source36_hash}" || { echo "oreon: Source36 hash mismatch" >&2; exit 1; }; }
test "%{source37_hash}" = "none" || { f="%{SOURCE37}"; test -f "$f" || { echo "oreon: missing Source37 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source37_hash}" || { echo "oreon: Source37 hash mismatch" >&2; exit 1; }; }
test "%{source38_hash}" = "none" || { f="%{SOURCE38}"; test -f "$f" || { echo "oreon: missing Source38 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source38_hash}" || { echo "oreon: Source38 hash mismatch" >&2; exit 1; }; }
test "%{source39_hash}" = "none" || { f="%{SOURCE39}"; test -f "$f" || { echo "oreon: missing Source39 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source39_hash}" || { echo "oreon: Source39 hash mismatch" >&2; exit 1; }; }
test "%{source40_hash}" = "none" || { f="%{SOURCE40}"; test -f "$f" || { echo "oreon: missing Source40 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source40_hash}" || { echo "oreon: Source40 hash mismatch" >&2; exit 1; }; }
test "%{source41_hash}" = "none" || { f="%{SOURCE41}"; test -f "$f" || { echo "oreon: missing Source41 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source41_hash}" || { echo "oreon: Source41 hash mismatch" >&2; exit 1; }; }# Extract license files
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
tar -xf %{SOURCE37} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE38} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE39} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE40} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE41} -C %{buildroot}%{_texmf_main}

# disable all hyphenations (except us english)
# The prebuilt language.dat and language.def files enable all possible language hyphenations
# but we probably do not have them installed and we don't want to
cp -f %{buildroot}%{_texmf_main}/tex/generic/config/language.us %{buildroot}%{_texmf_main}/tex/generic/config/language.dat
cp -f %{buildroot}%{_texmf_main}/tex/generic/config/language.us.def %{buildroot}%{_texmf_main}/tex/generic/config/language.def

# Remove tlpobj files
rm -rf %{buildroot}%{_texmf_main}/tlpkg/tlpobj/*.tlpobj

# Clean out enctex INSTALL files (useless)
rm -rf %{buildroot}%{_texmf_main}/doc/generic/enctex/INSTALL*

# Apply etex patch
pushd %{buildroot}%{_texmf_main}/tex/plain/etex/
patch -p0 < %{_sourcedir}/etex-addlanguage-fix-bz1215257.patch
popd

# Fix Python shebangs
%py3_shebang_fix %{buildroot}%{_texmf_main}/*

# Main collection metapackage (empty)
%files

%files -n texlive-amsfonts
%license ofl.txt
%{_texmf_main}/fonts/afm/public/amsfonts/
%{_texmf_main}/fonts/map/dvips/amsfonts/
%{_texmf_main}/fonts/source/public/amsfonts/
%{_texmf_main}/fonts/tfm/public/amsfonts/
%{_texmf_main}/fonts/type1/public/amsfonts/
%{_texmf_main}/tex/latex/amsfonts/
%{_texmf_main}/tex/plain/amsfonts/
%doc %{_texmf_main}/doc/fonts/amsfonts/

%files -n texlive-cm
%license knuth.txt
%{_texmf_main}/fonts/map/dvips/cm/
%{_texmf_main}/fonts/pk/ljfour/public/
%{_texmf_main}/fonts/source/public/cm/
%{_texmf_main}/fonts/tfm/public/cm/
%doc %{_texmf_main}/doc/fonts/cm/

%files -n texlive-colorprofiles
%license lppl1.3c.txt
%license mit.txt
%license pd.txt
%license other-free.txt
%{_texmf_main}/tex/generic/colorprofiles/
%doc %{_texmf_main}/doc/generic/colorprofiles/

%files -n texlive-ec
%license other-free.txt
%{_texmf_main}/fonts/source/jknappen/ec/
%{_texmf_main}/fonts/tfm/jknappen/ec/
%doc %{_texmf_main}/doc/fonts/ec/

%files -n texlive-enctex
%license gpl2.txt
%{_texmf_main}/tex/generic/enctex/
%doc %{_texmf_main}/doc/generic/enctex/

%files -n texlive-etex
%license knuth.txt
%{_texmf_main}/fonts/source/public/etex/
%{_texmf_main}/fonts/tfm/public/etex/
%{_texmf_main}/tex/plain/etex/
%doc %{_texmf_main}/doc/etex/base/
%doc %{_texmf_main}/doc/man/man1/

%files -n texlive-etex-pkg
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/etex-pkg/
%doc %{_texmf_main}/doc/latex/etex-pkg/

%files -n texlive-graphics-def
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/graphics-def/
%doc %{_texmf_main}/doc/latex/graphics-def/

%files -n texlive-hyph-utf8
%license mit.txt
%{_texmf_main}/tex/generic/hyph-utf8/conversions/conv-utf8-ec.tex
%{_texmf_main}/tex/generic/hyph-utf8/conversions/conv-utf8-il2.tex
%{_texmf_main}/tex/generic/hyph-utf8/conversions/conv-utf8-il3.tex
%{_texmf_main}/tex/generic/hyph-utf8/conversions/conv-utf8-l7x.tex
%{_texmf_main}/tex/generic/hyph-utf8/conversions/conv-utf8-lmc.tex
%{_texmf_main}/tex/generic/hyph-utf8/conversions/conv-utf8-lth.tex
%{_texmf_main}/tex/generic/hyph-utf8/conversions/conv-utf8-qx.tex
%{_texmf_main}/tex/generic/hyph-utf8/conversions/conv-utf8-t2a.tex
%{_texmf_main}/tex/generic/hyph-utf8/conversions/conv-utf8-t8m.tex
%{_texmf_main}/tex/luatex/hyph-utf8/
%doc %{_texmf_main}/doc/generic/hyph-utf8/
%doc %{_texmf_main}/doc/luatex/hyph-utf8/

%files -n texlive-hyphen-base
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/config/
%{_texmf_main}/tex/generic/hyphen/

%files -n texlive-hyphenex
%license pd.txt
%{_texmf_main}/tex/generic/hyphenex/

%files -n texlive-ifplatform
%license lppl1.3c.txt
%{_texmf_main}/tex/latex/ifplatform/
%doc %{_texmf_main}/doc/latex/ifplatform/

%files -n texlive-iftex
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/iftex/
%doc %{_texmf_main}/doc/generic/iftex/

%files -n texlive-knuth-lib
%license knuth.txt
%{_texmf_main}/fonts/source/public/knuth-lib/
%{_texmf_main}/fonts/tfm/public/knuth-lib/
%{_texmf_main}/tex/generic/knuth-lib/
%{_texmf_main}/tex/plain/knuth-lib/

%files -n texlive-knuth-local
%license pd.txt
%{_texmf_main}/fonts/source/public/knuth-local/
%{_texmf_main}/fonts/tfm/public/knuth-local/
%{_texmf_main}/mft/knuth-local/
%{_texmf_main}/tex/plain/knuth-local/

%files -n texlive-lua-alt-getopt
%license mit.txt
%{_texmf_main}/scripts/lua-alt-getopt/
%doc %{_texmf_main}/doc/support/lua-alt-getopt/

%files -n texlive-mflogo
%license lppl1.3c.txt
%{_texmf_main}/fonts/source/public/mflogo/
%{_texmf_main}/fonts/tfm/public/mflogo/
%{_texmf_main}/tex/latex/mflogo/
%doc %{_texmf_main}/doc/latex/mflogo/

%files -n texlive-modes
%license pd.txt
%{_texmf_main}/fonts/source/public/modes/
%doc %{_texmf_main}/doc/fonts/modes/

%files -n texlive-plain
%license knuth.txt
%{_texmf_main}/makeindex/plain/
%{_texmf_main}/tex/plain/base/
%{_texmf_main}/tex/plain/config/

%files -n texlive-tex-ini-files
%license pd.txt
%{_texmf_main}/tex/generic/tex-ini-files/
%{_texmf_main}/tex/latex/tex-ini-files/
%doc %{_texmf_main}/doc/generic/tex-ini-files/

%files -n texlive-texlive-common
%license lppl1.3c.txt
%doc %{_texmf_main}/doc/texlive/

%files -n texlive-texlive-msg-translations
%license lppl1.3c.txt
%{_texmf_main}/tlpkg/translations/

%files -n texlive-unicode-data
%license lppl1.3c.txt
%{_texmf_main}/tex/generic/unicode-data/
%doc %{_texmf_main}/doc/generic/unicode-data/

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 12:svn72890-11
- Import
