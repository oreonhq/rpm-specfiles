%global source0_hash 5315491a315a5380326458a228f7cda304eb3b14c3f61bf9792efc8061925462
%global hunspelldir %{_datadir}/hunspell
%global hyphendir %{_datadir}/hyphen
Name: openoffice.org-dict-cs_CZ
Version: 20080822
Release:        1%{?dist}
Summary:        Czech spellchecker and hyphenation dictionaries for LibreOffice
License: GPL-1.0-or-later
URL: http://extensions.services.openoffice.org/en/project/dict-cs
Source0:        https://downloads.sourceforge.net/aoo-extensions/dict-cs-2.0.oxt
BuildArch: noarch
Patch0: cs_CZ.aff.patch
# oreon:deps
BuildRequires:  dos2unix
# /oreon:deps
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

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -c -n %{name}
%patch -P0 -p4
dos2unix README_*.txt

%build

%install
mkdir -p $RPM_BUILD_ROOT%{hunspelldir}
install -m 644 cs* $RPM_BUILD_ROOT%{hunspelldir}
mkdir -p $RPM_BUILD_ROOT%{hyphendir}
install -m 644 hyph*.dic $RPM_BUILD_ROOT%{hyphendir}
%oreon_autofiles hunspell-cs usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles hyphen-cs usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n hunspell-cs -f %{oreon_filedir}/hunspell-cs.list
%files -n hyphen-cs -f %{oreon_filedir}/hyphen-cs.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 20080822-27
- Prepare for Oreon 11 (RP1)
