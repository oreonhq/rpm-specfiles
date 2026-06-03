%global source0_hash none

%if 0%{?fedora} >= 36 || 0%{?rhel} > 9 || (0%{?oreon} >= 11)
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: hunspell-ky
Summary: Kirghiz hunspell dictionaries
%global upstreamid 20090415
Version: 0.%{upstreamid}
Release: 36%{?dist}
Source0: https://ftp.gnu.org/gnu/aspell/dict/ky/aspell6-ky-0.01-0.tar.bz2
URL: http://ftp.gnu.org/gnu/aspell/dict/ky
License: GPL-2.0-or-later
BuildArch: noarch
BuildRequires: aspell hunspell-tools

Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-ky)

%description
Kirghiz hunspell dictionaries.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n aspell6-ky-0.01-0
export LANG=C.UTF-8
preunzip -d *.cwl
cat *.wl > kirghiz.wordlist
wordlist2hunspell kirghiz.wordlist ky_KG
cp -p ky_affix.dat ky_KG.aff

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p ky_KG.dic ky_KG.aff $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}

%files
%doc COPYING Copyright README doc/Crawler.txt
%{_datadir}/%{dict_dirname}/*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.20090415-36
- Import
