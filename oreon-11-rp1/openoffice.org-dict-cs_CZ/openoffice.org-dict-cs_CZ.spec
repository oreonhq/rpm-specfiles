%global hunspelldir %{_datadir}/hunspell
%global hyphendir %{_datadir}/hyphen

Name: openoffice.org-dict-cs_CZ
Version: 20080822
Release: 27%{?dist}
Summary: Czech spellchecker and hyphenation dictionaries for LibreOffice
License: GPL-1.0-or-later
URL: http://extensions.services.openoffice.org/en/project/dict-cs
Source0: http://downloads.sourceforge.net/aoo-extensions/dict-cs-2.0.oxt
BuildArch: noarch

BuildRequires: dos2unix

# rhbz#1173776
Patch0: cs_CZ.aff.patch

%description
This package contains the Czech hyphenation dictionaries for the LibreOffice
application suite.

%package -n hunspell-cs
Summary: Czech hunspell dictionary
Requires: hunspell

%description -n hunspell-cs
This package contains the Czech dictionary for the hunspell spellchecker.

%package -n hyphen-cs
Summary: Czech hyphenation rules
Requires: hyphen

%description -n hyphen-cs
Czech hyphenation rules.

%prep
%setup -q -c -n %{name}
%patch -P0 -p4
dos2unix README_*.txt

%build

%install
mkdir -p $RPM_BUILD_ROOT%{hunspelldir}
install -m 644 cs* $RPM_BUILD_ROOT%{hunspelldir}
mkdir -p $RPM_BUILD_ROOT%{hyphendir}
install -m 644 hyph*.dic $RPM_BUILD_ROOT%{hyphendir}

%files -n hyphen-cs
%doc README_cs.txt README_en.txt
%{hyphendir}/hyph_cs*

%files -n hunspell-cs
%doc README_cs.txt README_en.txt
%{hunspelldir}/cs*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 20080822-27
- Prepare for Oreon 11 (RP1)
