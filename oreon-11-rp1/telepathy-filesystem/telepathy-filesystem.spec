%global source0_hash none

Name:           telepathy-filesystem
Version:        0.0.2
Release:        29%{?dist}
Summary:        Telepathy filesystem layout

# SPDX confirmed
License:        LicenseRef-Not-Copyrightable

BuildArch:      noarch
Requires:       filesystem

%description
This package provides some directories which are required by other
packages which comprise the Telepathy release.  

%prep

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/telepathy/managers
mkdir -p $RPM_BUILD_ROOT%{_datadir}/telepathy/clients
mkdir -p $RPM_BUILD_ROOT%{_includedir}/telepathy-1.0

%files
%dir %{_datadir}/telepathy
%dir %{_datadir}/telepathy/managers
%dir %{_datadir}/telepathy/clients
%dir %{_includedir}/telepathy-1.0

%changelog
%autochangelog
