%global source0_hash 2b03b08ee2818029eb289a815f50197a97ec0b1ca00a674737fa98af6fb1efde
Name: mythes-eo
Summary:        Esperanto thesaurus
%global upstreamid 20180330
Version: 0.%{upstreamid}
Release:        1%{?dist}
Source0:        https://esperanto.mv.ru/Download/dict-eo.oxt
URL: http://esperanto.mv.ru/Download/
License: GPL-3.0-or-later
BuildArch: noarch
# oreon:deps

# /oreon:deps
%description
Esperanto thesaurus.

%package -n hyphen-eo
Summary: Esperanto hyphen rules
Requires: hyphen
Supplements: (hyphen and langpacks-eo)
%description -n hyphen-eo
Esperanto hyphenation rules.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p dictionaries/hyph_eo.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen/
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/mythes
cp -p dictionaries/th_eo.dat $RPM_BUILD_ROOT/%{_datadir}/mythes/th_eo.dat
cp -p dictionaries/th_eo.idx $RPM_BUILD_ROOT/%{_datadir}/mythes/th_eo.idx
%oreon_autofiles hyphen-eo usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n hyphen-eo -f %{oreon_filedir}/hyphen-eo.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.%{upstreamid}-18
- Prepare for Oreon 11 (RP1)
