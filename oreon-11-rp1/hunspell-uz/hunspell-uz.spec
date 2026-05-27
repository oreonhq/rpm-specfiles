%global source0_hash none

%if 0%{?fedora} >= 36 || 0%{?rhel} > 9 || 0%{?oreon}
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: hunspell-uz
Summary: Uzbek hunspell dictionaries
Version: 0.6
Release: 35%{?dist}
## Note that upstream is dead and there is no download link available
## so please don't report FTBFS bugs for this package.
Source0: http://www-user.uni-bremen.de/~kmashrab/uzbek-word-list/uzbek-wordlist-%{version}.tar.bz2
URL: http://www-user.uni-bremen.de/~kmashrab/uzbek-word-list
License: GPL-2.0-or-later
BuildArch: noarch

BuildRequires: make
Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-uz)

%description
Uzbek hunspell dictionaries.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -n uzbek-wordlist-%{version}

%build
pushd hunspell
make
cp -p README ../README.hunspell
popd

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p hunspell/uz_UZ* $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/


%files
%doc ChangeLog README README.hunspell TODO
%license COPYING Copyright
%{_datadir}/%{dict_dirname}/*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.6-35
- Import
