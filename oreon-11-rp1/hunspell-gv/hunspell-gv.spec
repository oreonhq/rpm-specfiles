%global source0_hash none

%if 0%{?fedora} >= 36 || 0%{?rhel} > 9 || (0%{?oreon} >= 11)
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: hunspell-gv
Summary: Manx hunspell dictionaries
%global upstreamid 20040505
Version: 0.%{upstreamid}
Release: 37%{?dist}
Source0: https://mirrors.kernel.org/gnu/aspell/dict/gv/aspell-gv-0.50-0.tar.bz2#/aspell6-gv-0.50-0.tar.bz2
URL: https://ftp.gnu.org/gnu/aspell/dict/gv
License: GPL-1.0-or-later
BuildArch: noarch
BuildRequires: aspell hunspell hunspell-devel

Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-gv)

%description
Manx hunspell dictionaries.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | cut -d' ' -f1); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n aspell-gv-0.50-0
export LANG=C.UTF-8
preunzip -d *.cwl
cat *.wl > manx.wordlist
wordlist2hunspell manx.wordlist gv_GB
cp -p gv_affix.dat gv_GB.aff

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p gv_GB.dic gv_GB.aff $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}

%files
%doc COPYING Copyright README Crawler.txt
%{_datadir}/%{dict_dirname}/*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.20040505-37
- Import
