%global source0_hash d31a36733913c83597e7409a932b2eb0ddbc20eb93dbe70eb2d5de34cbc04ec5

%global upstream_name translate_toolkit
Name:           translate-toolkit
Version:        3.18.0
Release:        2%{?dist}
Summary:        Tools to assist with translation and software localization
License:        GPL-2.0-or-later
URL:            http://toolkit.translatehouse.org/
Source0:        https://github.com/translate/translate/releases/download/%{version}/%{upstream_name}-%{version}.tar.gz
Source1:        pocommentclean.1
Source2:        pocompendium.1
Source3:        pocount.1
Source4:        pomigrate2.1
Source5:        popuretext.1
Source6:        poreencode.1
Source7:        posplit.1
Source8:        tmserver.1

BuildArch:      noarch

BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pip
BuildRequires:	python3-setuptools_scm
BuildRequires:  python3-wheel
BuildRequires:	pyproject-rpm-macros

BuildRequires: 	python3-sphinx
BuildRequires: 	python3-sphinx-copybutton
BuildRequires: 	python3-sphinxext-opengraph
BuildRequires: 	python3-furo

BuildRequires:  python3-aeidon
BuildRequires:  python3-beautifulsoup4
BuildRequires:  python3-chardet
BuildRequires:  python3-enchant
BuildRequires:  python3-iniparse
BuildRequires:  python3-Levenshtein
BuildRequires:  python3-lxml
BuildRequires:  python3-phply
BuildRequires:  python3-pycountry
BuildRequires:  python3-ruamel-yaml
BuildRequires:  python3-simplejson
BuildRequires:  python3-six
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx-copybutton
BuildRequires:  python3-sphinxext-opengraph
BuildRequires:  python3-furo
BuildRequires:  python3-unicode-segmentation-rs
BuildRequires:  python3-vobject

Requires:       gettext
Requires:       python3-aeidon
Requires:       python3-beautifulsoup4
Requires:       python3-chardet
Requires:       python3-cheroot
Requires:       python3-enchant
Requires:       python3-iniparse
Requires:       python3-Levenshtein
Requires:       python3-lxml
Requires:       python3-phply
Requires:       python3-pycountry
Requires:       python3-ruamel-yaml
Requires:       python3-simplejson
Requires:       python3-six
Requires:       python3-unicode-segmentation-rs
Requires:       python3-vobject

%description
A set of tools for managing translation and software localization via Gettext
PO or XLIFF format files.

Including:
  * Convertors: convert from various formats to PO or XLIFF
  * Formats:
    * Core localization formats - XLIFF and Gettext PO
    * Other localization formats - TMX, TBX, Qt Linguist (.ts),
           Java .properties, Wordfast TM, OmegaT glossary
    * Compiled formats: Gettext MO, Qt .qm
    * Other formats - OpenDocument Format (ODF), text, HTML, CSV, INI,
            wiki (MediaWiki, DokuWiki), iCal
    * Specialised - OpenOffice.org GSI/SDF, PHP,
            Mozilla (.dtd, .properties, etc), Symbian,
            Innosetup, tikiwiki, subtitles
  * Tools: count, search, debug, segment and pretranslate localization
            files. Extract terminology. Pseudo-localize
  * Checkers: validate translations with over 45 checks

%package        docs
Summary:        Documentation for %{name}
Requires:       %{name} = %{version}-%{release}
# added during F26 cycle
Obsoletes:      %{name}-devel < %{version}-%{release}

%description    docs
This package contains Translate Toolkit documentation, including API docs
for developers  wishing to build new tools for the toolkit or to use
the libraries in other localization tools.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{upstream_name}-%{version}
# Remove version limit from lxml
sed -i 's/"lxml.*"/"lxml"/' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires

%build
LANG=C.utf8
%pyproject_wheel

%install
LANG=C.utf8
%pyproject_install

# create manpages
mkdir -p %{buildroot}%{_mandir}/man1
for prog in %{buildroot}%{_bindir}/*; do
    progname=$(basename $prog)
    case ${progname} in
      build_tmdb|buildxpi.py|get_moz_enUS.py|l20n2po|po2l20n|pydiff)
        ;;
      pocommentclean|pocompendium|pocount|pomigrate2|popuretext|poreencode|posplit|tmserver)
        cp -p %{_sourcedir}/${progname}.1 %{buildroot}%{_mandir}/man1/
        ;;
      *)
        PYTHONPATH=. $prog --manpage >  %{buildroot}%{_mandir}/man1/${progname}.1 || :
        grep -q .SH %{buildroot}%{_mandir}/man1/${progname}.1 || rm -f %{buildroot}%{_mandir}/man1/${progname}.1
        ;;
    esac
done

%files
%doc COPYING
%{_bindir}/*
%{_mandir}/man1/*
%{python3_sitelib}/translate*

%changelog
%autochangelog
