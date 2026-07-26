%global source0_hash 792d494bba26cfe746ccb496d276d1130615831d16d3f3b171672ed0dd9dd01a

Name:           sepolicy_analysis
Version:        0.1
Release:        33%{?dist}
Summary:        SELinux policy analysis tool

# Automatically converted from old format: GPLv3 - review is highly recommended.
License:        GPL-3.0-only
URL:            https://github.com/vmojzis/sepolicy_analysis
#./setup.py egg_info --egg-base /tmp sdist
Source0:        https://github.com/vmojzis/sepolicy_analysis/releases/download/%{version}/%{name}-%{version}.tar.gz
Patch0:         0001-Update-to-work-with-setools-4.3.patch

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

Requires: python3-setools >= 4.0
Requires: python3-networkx >= 1.11
Requires: python3-matplotlib

%description
Tool designed to help increase the quality of SELinux policy by identifying
possibly dangerous permission pathways, simplifying regression testing and
providing policy visualization.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p 1

%build
%py3_build

%install
#mkdir -p % {buildroot}% {_mandir}/man1
%py3_install

%check
%if %{?_with_check:1}%{!?_with_check:0}
%{__python3} setup.py test
%endif

%files
%license COPYING
%{python3_sitelib}/*
%{_bindir}/seextract_cil
%{_bindir}/sebuild_graph
%{_bindir}/seexport_graph
%{_bindir}/segraph_query
%{_bindir}/sevisual_query
%dir %{_sysconfdir}/sepolicyanalysis
%config(noreplace) %{_sysconfdir}/sepolicyanalysis/domain_groups_cil.conf
%config(noreplace) %{_sysconfdir}/sepolicyanalysis/security_related.conf
%doc %{_mandir}/man1/se*

%changelog
%autochangelog
