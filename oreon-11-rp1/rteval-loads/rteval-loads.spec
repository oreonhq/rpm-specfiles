%global source0_hash ddf2ea0d4439e1d57136be3623102af9458f601f5b1cb77e83246e88aea09d0e

Name:		rteval-loads
Version:	6.17.7
Release:	2%{?dist}
Summary:	Source files for rteval loads
Group:		Development/Tools
License:	GPL-2.0-only
URL:		https://git.kernel.org/pub/scm/utils/rteval/rteval.git
Source0:        https://www.kernel.org/pub/linux/kernel/v6.x/linux-%{version}.tar.xz

BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:	noarch

%description
This package provides source code for system loads used by the rteval package

%prep

%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%build

%install
mkdir -p %{buildroot}%{_datadir}/rteval/loadsource
install -m 644 %{SOURCE0} %{buildroot}%{_datadir}/rteval/loadsource

%files
%defattr(-,root,root,-)
%dir %{_datadir}/rteval/loadsource
%{_datadir}/rteval/loadsource/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.17.7-2
- Prepare for Oreon 11 (RP1)
