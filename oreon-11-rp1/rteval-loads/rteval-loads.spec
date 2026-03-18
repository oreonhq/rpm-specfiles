Name:		rteval-loads
Version:	6.17.7
Release:	2%{?dist}
Summary:	Source files for rteval loads
Group:		Development/Tools
License:	GPL-2.0-only
URL:		https://git.kernel.org/pub/scm/utils/rteval/rteval.git
Source0:	https://www.kernel.org/pub/linux/kernel/v6.x/linux-%{version}.tar.xz

BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:	noarch

%description
This package provides source code for system loads used by the rteval package

%prep

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
