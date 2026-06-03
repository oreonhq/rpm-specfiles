%global source0_hash none

Name: mythes-uk
Summary: Ukrainian thesaurus
Version: 1.6.5
Release: 32%{?dist}
Source:        https://downloads.sourceforge.net/project/ispell-uk/spell-uk/1.6.5/spell-uk-1.6.5.tgz#/mythes-uk-1.6.5.tar.gz
URL: http://sourceforge.net/projects/ispell-uk
#unused myspell dicts are under GPLv2+ or LGPLv2+ or MPLv1.1
#unused hyphenation dicts are under GPLv2+
#toplevel is GPLv2+ or LGPLv2+
License: ( GPL-2.0-or-later OR LGPL-2.1-or-later ) AND ( GPL-2.0-or-later OR LGPL-2.1-or-later OR MPL-1.1 ) AND GPL-2.0-or-later
BuildRequires: perl-interpreter, mythes-devel
BuildArch: noarch
Requires: mythes
Supplements: (mythes and langpacks-uk)

%description
Ukrainian thesaurus.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n spell-uk-%{version}

%build
cd src/thesaurus
mv -f th_uk_UA.dat th_uk_UA_v2.dat
th_gen_idx.pl < th_uk_UA_v2.dat > th_uk_UA_v2.idx

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/mythes
cp -p src/thesaurus/th_uk_UA_v2.* $RPM_BUILD_ROOT/%{_datadir}/mythes


%files
%doc README README.uk Copyright
%license COPYING.GPL COPYING.LGPL
%{_datadir}/mythes/*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.6.5-32
- Import
