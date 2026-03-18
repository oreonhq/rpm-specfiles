%if 0%{?fedora} >= 36 || 0%{?rhel} > 9
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
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.6-35
- Prepare for Oreon 11 (RP1)
