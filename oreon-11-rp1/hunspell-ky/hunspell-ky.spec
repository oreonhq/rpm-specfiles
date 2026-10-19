%global source0_hash e10f2f25b44b71e30fa1ea9c248c04543c688845a734d0b9bdc65a2bbd16fb4f
%if 0%{?fedora} >= 36 || 0%{?rhel} > 9 || (0%{?oreon} >= 11)
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif
Name: hunspell-ky
Summary:        Kirghiz hunspell dictionaries
%global upstreamid 20090415
Version: 0.%{upstreamid}
Release:        1%{?dist}
Source0:        https://mirrors.kernel.org/gnu/aspell/dict/ky/aspell6-ky-0.01-0.tar.bz2
URL: https://ftp.gnu.org/gnu/aspell/dict/ky
License: GPL-2.0-or-later
BuildArch: noarch
Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-ky)
# oreon:deps
BuildRequires:  aspell
BuildRequires:  hunspell
BuildRequires:  hunspell-devel
# /oreon:deps
%description
Kirghiz hunspell dictionaries.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f"  | cut -d' ' -f1); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
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
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.20090415-36
- Import
