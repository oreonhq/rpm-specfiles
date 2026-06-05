%global source0_hash 22f2fd629a4410ce941262820e2ce13da074db7009fc24f49e7408ae0eee8f01

%if 0%{?fedora} >= 36 || 0%{?rhel} > 9
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: hunspell-lb
Summary: Luxembourgish hunspell dictionaries
%global upstreamid 20121128
Version: 0.%{upstreamid}
Release: 28%{?dist}
URL: http://spellchecker.lu
License: EUPL-1.1
BuildArch: noarch
Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-lb)

Source0:        http://downloads.spellchecker.lu/packages/OOo3/SpellcheckerLu.oxt

%description
Luxembourgish hunspell dictionaries.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -c

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p *.dic *.aff $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/mythes
cp -p th_lb_LU_v2.* $RPM_BUILD_ROOT/%{_datadir}/mythes

%files
%doc registration/README_lb_LU.txt
%{_datadir}/%{dict_dirname}/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.%{upstreamid}-28
- Prepare for Oreon 11 (RP1)
